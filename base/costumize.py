from rest_framework.authentication import TokenAuthentication


class BearerAuto(TokenAuthentication):
    keyword = "Bearer"

