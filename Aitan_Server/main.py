from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import json

from BL.Rec_BL.growers_bl import Growers
# from BL.users_bl import Users
# from BL.members_bl import Members
# from BL.movies_bl import Movies
# from BL.subscriptions_bl import Subscriptions

app = Flask(__name__)
CORS(app)


#  **************************************************

growers_bl=Growers()

#  **************************************************
#  **************************************************
@app.route('/growers',methods=['GET'])
def get_growers():
    # resp= auth_bl.token_verification()  
    # if resp == "not authorized":
    #     return jsonify("The user is not autorized")
    # else:
        data=growers_bl.get_growers()
        return jsonify(data)


# @app.route('/users', methods= ['POST'])
# def add_user():
#         data = request.json
#         users_bl.add_user(data)
#         return jsonify("added user")



# @app.route('/users/<string:id>', methods= ['PUT'])
# def update_user(id):
#         data = request.json
#         users_bl.update_user(id, data)
#         return jsonify("updated user")
   

# @app.route('/users/<string:id>', methods= ['DELETE'])
# def delete_user_data(id):
#     users_bl.delete_user(id)
#     return jsonify("deleted user")


#  **************************************************




if __name__== '__main__':
    app.run(port=1000)
