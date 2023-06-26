from methodism import custom_response, MESSAGE
from director.models import Maxsulot, Magazin
from director.models.savdo import savdo_oynasi
from director.models import Client


def savdo_ooynasi(request, params):
    if request.user.type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])

    return {
        "result": [x.xs_format() for x in savdo_oynasi.objects.all()]
    }


def maxsulotlar_onyasi(request, params):
    if request.user.type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])

    return {
        "result": [x.xm_format() for x in Magazin.objects.all()]
    }


def clent_oynasi(request, params):
    if request.user.type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])

    return {
        "result": [x.x_format() for x in Client.objects.all()]
    }


def buyurtma_oynasi(request, params):
    if not request.user.type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])

    if "name" not in params or "size" not in params or "color" not in params \
            or "soni" not in params or "ombor_id" not in params:
        return custom_response(False, message="Params toliq emas")

    ombor = Magazin.objects.filter(id=params["ombor_id"]).first()
    if not ombor:
        return custom_response(False, message={"bunday ID lik ombor yoq"})

    if ombor.maxsulot_soni < params["soni"]:
        return custom_response(False, message="Mahsulot yetarli emas")









    return {
        "succes": "ishladi"
    }
