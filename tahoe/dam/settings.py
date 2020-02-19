import os
import falcon_auth
import falcon_jsonify


user_loader = lambda email, password: { 'email' : email }
jwt_auth_backend = falcon_auth.JWTAuthBackend(user_loader, secret_key="Asdf1234#")
jwt_auth_middleware = falcon_auth.FalconAuthMiddleware(jwt_auth_backend, exempt_routes=['/exempt'])


dbcfg = {
    'host': 'localhost', # or external server address
    'port': 27017,
    'username': os.environ.get('MONGO_USER'),
    'password': os.environ.get('MONGO_PASS'),
}


middleware = [
    falcon_jsonify.Middleware(help_messages=True),
    jwt_auth_middleware,
]