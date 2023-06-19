from methodism import custom_response

from director.models import Korzina, Maxsulot


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
