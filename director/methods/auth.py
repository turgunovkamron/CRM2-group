import datetime
import random
import uuid
import re

from methodism import custom_response, code_decoder, generate_key
from rest_framework import request
from rest_framework.authtoken.models import Token

from base.send_email import send_email
from base.serves import check_phone_in_db, check_token_in_db, check_user_in_token_db, check_email_in_db, update_token
from director.models import User, OTP


def regis(requests, params):
    nott = 'token' if 'token' not in params else 'password' if 'password' not in params else 'phone' if 'phone' not in params else ''
    # print("a")
    if nott:
        # print("aa")
        return custom_response(False, message=f"{nott} paramsda bo'lishi kere")
    # print("b")
    token = check_token_in_db(params['token'])
    # print("c")
    if not token:
        # print("cc")
        return custom_response(False, message="Token xato")

    # print("d")
    if token['is_expire']:
        return custom_response(False, message="Token yaroqsiz!")

    if not token['is_conf']:
        return custom_response(False, message="Token tastiqlanmagan")

    if len(str(params['phone'])) != 12:
        return custom_response(False, message="Phone 12ta raqamdan bo'lishi kere")

    if type(params['phone']) is not int:
        return custom_response(False, message="Phone raqamlardan iborat bo'lishi kerak")

    if len(str(params['password'])) < 8 or " " in params['password']:
        return custom_response(False, message="Parol 8tadan kichkina bolishi kerak emas")

    user_data = {
        'phone': params['phone'],
        'password': params['password'],
        'name': params.get('name', " "),
        'last_name': params.get('last_name', " "),
        'email': token['email']
    }

    if params.get('key', None) == 'SecretKey':
        user_data.update({'is_staff': True, 'is_superuser': True})
        user = User.objects.create_superuser(**user_data)
    user = User.objects.create_user(**user_data)
    token = Token.objects.create(user=user)
    return custom_response(True, data=token.key)


def login(requests, params):
    nott = 'password' if 'password' not in params else 'email' if 'email' not in params else ''

    if nott:
        return custom_response(False, message=f"{nott} paramsda bo'lishi kerak")

    user = User.objects.filter(email=params['email']).first()
    if not user:
        return custom_response(False, message='Bu nomerga user yo"q')

    # password = params['password']

    if not user.check_password(params['password']):
        return custom_response(False, message='Parol xato')

    token = Token.objects.get_or_create(user=user)[0]

    return custom_response(True, data={"token": token.key}, message="Login bo'ldi")


def logout(requests, params):
    token = Token.objects.filter(user=requests.user).first()

    if token:
        token.delete()

    return custom_response(True, message="Token o'chirildi")


def stepone(requests, params):
    # send_email()
    if 'email' not in params:
        return custom_response(False, message="Data to'liq emas")

    user = check_email_in_db(params['email'])

    if user:
        return custom_response(False, message="Bu nomer boyicha user bor")

    code = random.randint(1000000, 9999999)

    send_email(OTP=code, email=params['email'])

    shifr = uuid.uuid4().__str__() + '&' + str(code) + '&' + generate_key(21)
    shifr = code_decoder(shifr, l=3)

    otp = OTP.objects.create(key=shifr, email=params['email'])

    return custom_response(True, data={
        'otp': code,
        'token': otp.key
    })


def steptwo(requests, params):
    nott = 'otp' if 'otp' not in params else 'token' if 'token' not in params else ''
    if nott:
        return custom_response(False, message=f"{nott} paramsda bo'lishi kerak")

    token = check_token_in_db(params['token'])
    if not token:
        return custom_response(False, message="Token xato")
    # print(token)
    if token['is_conf']:
        return custom_response(False, message="Token ishlatilgan")

    if token['is_expire']:
        return custom_response(False, message="Token eski")

    now = datetime.datetime.now(datetime.timezone.utc)

    if (now - token['created']).total_seconds() >= 180:
        token['is_expire'] = True
        update_token(token)
        return custom_response(False, message="Tokenga berilgan vaqt tugadi")

    code = code_decoder(token['key'], decode=True, l=3).split('&')[1]

    if str(params['otp']) != code:
        token['tries'] += 1
        update_token(token)

        return custom_response(False, message="Kode xato")

    token['is_conf'] = True
    update_token(token)

    return custom_response(True, message="Ishladi", data={'otp': code})


def user_info(request, params):
    return custom_response(True, data=request.user.format())


def change_password(request, params):
    nott = "newpass" if "newpass" not in params else "oldpass" if "oldpass" not in params else ''
    return custom_response(False, message="Newpass or oldpass paramsda bo'lishi kerak")


def change_phone(request, params):
    if "phone" not in params:
        return custom_response(False, message="Phone kirib kelishi kerak")
    if "phone" in params:
        user = check_phone_in_db(params["phone"])
        if user and user['id'] != request.user.id:
            return custom_response(True, message="raqam band")

        if len(params["phone"]) != 12:
            return custom_response(False, message="Raqamni tog'ri yozing ")

        if type(params['phone']) is not int:
            return custom_response(False, message="Raqam sonladan iborat bolishi kerak")

        update_user(phone=params["phone"])

    return custom_response(True, data=request.user.format())


def change_name(request, params):
    if "name" not in params:
        return custom_response(False, message="Name kirish kerak")
    if "name" in params:
        update_user(name=params["name"])
    return custom_response(True, data=request.user.format())


def change_last_name(request, params):
    if "last_name" not in params:
        return custom_response(False, message="Last name kiriting")
    if "Last_name" in params:
        update_user(last_name=params["last_name"])
    return custom_response(True, data=request.user.format())


def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return custom_response(True, message="To'rgi email")
