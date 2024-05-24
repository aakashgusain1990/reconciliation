from distutils.log import Log
from flask import Blueprint, jsonify, request, make_response
from app.config import Routes, ResponseMessages, Logger
from app.dto.customer_dtos import CustomerDto
from app.services.identify_services import IdentifyService

base_path_blueprint = Blueprint(
    Routes.BASEPATH, __name__, url_prefix=Routes.BASEPATH)

@base_path_blueprint.route("/identify", methods=['POST'])
def purchase():
    try:
        request_body = CustomerDto(
                email=request.json["email"] if "email" in request.json else None,
                phone_number=request.json["phoneNumber"] if "phoneNumber" in request.json else None,
            ) 
        print("request reached here")
        if not request_body.email and not request_body.phone_number:
            return make_response(jsonify(ResponseMessages.BAD_REQUEST), 400)
        customer_details = IdentifyService.add_customer(request_body)
        return make_response(jsonify(customer_details), 201)
    except Exception as e:
        return make_response(jsonify("Error due to: {0}".format(e)), 500)