from .auth import regis, login, logout, stepone, steptwo, user_actions, user_info, delete_user
from .ombor import korzina_qoshish, korzina_get, korzina_delete, likes, all_ombor, add_ombor


unusable_variable = dir()


def all_methods(requests, params):
    mumkinmas = ["auth", "ombor"]
    return {
        "result": [x for x in unusable_variable if "__" not in x and x not in mumkinmas]
    }
