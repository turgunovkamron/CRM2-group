from methodism import custom_response

from director.models import Korzina, Maxsulot, Likes


def korzina_qoshish(request, params):
    if "product_id" not in params:
        return custom_response(False, message="Product id paramsda bolishi kerak")

    maxsulot = Maxsulot.objects.filter(id=params["product_id"]).first()
    if not maxsulot:
        return custom_response(False, message="Product topilmadi")

    savat = Korzina.objects.get_or_create(maxsulot=maxsulot, user=request.user)[0]
    savat.nechtaligi = params.get('quantity', savat.nechtaligi)
    savat.save()

    return custom_response(True, message="Savatga qoshildi")


def korzina_get(request, params):
    return custom_response(True, data={
        "result": [x.format() for x in Korzina.objects.filter(user=request.user, status=True)]})


def korzina_delete(request, params):
    if "maxsulot_id" not in params:
        return custom_response(False, message="Maxsulot id paramsda bolishi kere")

    maxsulot = Korzina.objects.filter(id=params["maxsulot_id"]).first()

    if not maxsulot:
        return custom_response(False, message="Bunaqa maxsulot yoq")

    maxsulot.delete()

    return custom_response(True, message="Maxsulot ochirildi")


<<<<<<< Updated upstream
=======
<<<<<<< HEAD
def likes(req, params):
    if "key" not in params or 'prod_id' not in params or params.get('key', "") not in ['like', 'dis']:
        return custom_response(False, message="data to'lliq emas")

    prod = Maxsulot.objects.filter(id=params['prod_id']).first()
    if not prod:
        return custom_response(False, message="bunaqasi yo")

    root = Likes.objects.get_or_create(prod=prod, user=req.user)[0]
    if root.like and params['key'] == "like":
        root.like = False
        root.dis = False
    elif root.dis and params['key'] == "dis":
        root.like = False
        root.dis = False
    else:
        root.like = True if params['key'] == 'like' else False
=======
>>>>>>> Stashed changes
def likes(requests ,params):
    if "key" not in params or "prod_id" not in params or params['key'] not in ['like' , 'dis']:
        return custom_response(False, message="Data to'liq emas")

    prod = Maxsulot.objects.filter(id=params['prod_id']).first()
    if not prod:
        return custom_response(False, message="Bunaqasi yo'q")

    root = Likes.objects.get_or_created(prod=prod , user=requests.user)[0]
    if root.like and params['key'] == 'like':
        root.like = False
        root.dis = False
    elif root.dis and params['dis'] == 'dis':
        root.like = False
        root.dis = False

    else:
        root.like = True if params['key'] == 'like ' else False
<<<<<<< Updated upstream
=======
>>>>>>> a0da34c78da6f5eae1dfdb72e54387c6341e0dcb
>>>>>>> Stashed changes
        root.dis = True if params['key'] == 'dis' else False

    root.save()

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    likelar = Likes.objects.filter(prod=prod, like=True).count()
    dislar = Likes.objects.filter(prod=prod, dis=True).count()

    return {
        "likes": likelar,
        "dis": dislar,
    }



=======
>>>>>>> Stashed changes
    likelar = Likes.objects.filter(prod=prod , like = True).count()
    dislar = Likes.objects.filter(prod=prod , dis = True).count()

    # return custom_response(True , message=f"{params['key']} bosildi")
    return {
        "likes":likelar,
        "dis":dislar 
<<<<<<< Updated upstream
    }
=======
    }
>>>>>>> a0da34c78da6f5eae1dfdb72e54387c6341e0dcb
>>>>>>> Stashed changes
