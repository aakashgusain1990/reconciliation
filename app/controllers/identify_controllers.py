from distutils.log import Log
from flask import Blueprint, jsonify, request, make_response
from app.config import Routes, ResponseMessages, Config
from app.dto.customer_dtos import CustomerDto
from app.services.identify_services import IdentifyService

base_path_blueprint = Blueprint(
    Routes.BASEPATH, __name__, url_prefix=Routes.BASEPATH)

@base_path_blueprint.route("/identify", methods=['POST'])
def purchase():
    try:
        #Retrieve request body
        request_body = CustomerDto(
                email=request.json["email"] if "email" in request.json else None,
                phone_number=request.json["phoneNumber"] if "phoneNumber" in request.json else None,
            ) 
        Config.LOGGER.info("Request to add customer: {0}".format(request_body))
        
        #Validate request body
        if not request_body.email and not request_body.phone_number:
            Config.LOGGER.error("Missing mandatory fields: email, phone number")
            return make_response(jsonify(ResponseMessages.BAD_REQUEST), 400)
        
        customer_details = IdentifyService.add_customer(request_body)
        return make_response(jsonify(customer_details), 201)
    except Exception as e:
        Config.LOGGER.error("Could not create event due to ERROR: "+str(e))
        return make_response(jsonify("Error due to: {0}".format(e)), 500)