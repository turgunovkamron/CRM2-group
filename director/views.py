from methodism import METHODISM
from director import methods


# Create your views here.
class Main(METHODISM):
    file = methods
    not_auth_methods = ['regis', 'login', 'stepone', 'steptwo']
