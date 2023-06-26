from director.models.Xodim import Xodimlar
from methodism import custom_response, MESSAGE, error_params_unfilled



def add_xodim(request, params):
    if "name" not in params or "phone" not in params or "passport" not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])

    saves = Xodimlar.objects.get_or_create(name=params['name'], phone=params['phone'], passport=params['passport'])[0]



    return {
        "usrra": saves.employee_format()
    }