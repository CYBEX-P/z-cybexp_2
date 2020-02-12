if __name__ == "__main__": from views_comm import *
else: from .views_comm import *

import os
import sys
sys.path.append(os.path.realpath('../../../..'))
from mal_url.action.action import ismalicious

from flask_restful import Resource, reqparse, inputs
from tahoe.report import Report
import pdb

p = reqparse.RequestParser()
p.add_argument('url', type=str)

class IsMaliciousURL(Resource):
    
    @jwt_required
    def post(self):
        req = p.parse_args()
        url = req.pop('url')
        if not url: return {"error" : "Post valid URL"}, 400

        proba = ismalicious(url)
        proba2 = ismalicious2(url)
        return {
            "benign" : proba[0]*100, "malicious" : proba[1]*100,
            "benign_2" : proba2[0]*100, "malicious_2" : proba2[1]*100,
            }, 200
        
        
        
