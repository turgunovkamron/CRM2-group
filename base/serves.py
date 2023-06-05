from contextlib import closing

from django.db import connection


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = []
    for i in cursor.description:
        columns.append(i[0])
    a = cursor.fetchall()
    img = None
    if "img" in columns:
        img = columns.index("img")
    natija = []
    for i in a:
        i = list(i)
        if img:
            i[img] = "http://127.0.0.1:8000/media/" + i[img]
        b = dict(zip(columns, i))
        natija.append(b)
    return natija


def check_phone_in_db(phone):
    sql = f"""
        SELECT phone from director_User t
        where t.phone like '{phone}'
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)

        return result


def check_token_in_db(token):
    sql = f"""
        SELECT key from director_OTP t
        where t.key like '{token}'
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchone(cursor)

        return result

def check_user_in_token_db(user):
    sql = f"""
        SELECT key from director_Token t
        where t.user like '{user}'
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)

        return result