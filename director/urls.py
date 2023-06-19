from django.urls import path
from .views import Main
from director.methods.auth import user_actions
urlpatterns = [
    path("main/", Main.as_view()),
    path("user/actions/", user_actions.as_view()),
]
