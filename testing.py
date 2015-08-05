
from decouple import config

from tapioca_mandrill import Mandrill
from tapioca.exceptions import TapiocaException

api = Mandrill(key=config('KEY'))

try:
    r = api.users(method='ping').post()
except TapiocaException as e:
    print e.client().data()
    print e.client().response().status_code
