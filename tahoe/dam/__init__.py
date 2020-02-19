import falcon
import mongoengine as mongo

from dam.settings import dbcfg, middleware
##from dam.resources import *

dam = falcon.API(middleware=middleware)

db = mongo.connect(
    'development', # This will be the name of your database
    host=dbcfg['host'],
    port=dbcfg['port'],
    username=dbcfg['username'],
    password=dbcfg['password']
)

from dam.resources import *

dam.add_route('/register/', UserRegister)
dam.add_route('/login/', UserLogin)
