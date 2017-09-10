from datetime import datetime
import json
import geocoder
from smartystreets import Client
import logging

def lambda_handler(event, context):
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  return_json = {}
  return_json["meta"] = {}
  return_json["meta"]["request_start"] = time_stamp()
  return_json["meta"]["event"] = event
  
  if event["httpMethod"] != "GET":
    return_json["meta"]["request_end"] = time_stamp()
    return method_not_allowed_response(return_json)

  try:
    request_id = event["queryStringParameters"]["rid"]
    address = event["queryStringParameters"]["q"]
  except KeyError:
    return_json["meta"]["request_end"] = time_stamp()
    return bad_request_response(return_json)

  else:
    return_json["meta"]["mapquest_start"] = time_stamp()
    return_json["mapquest"] = mapquest(address)
    return_json["meta"]["mapquest_end"] = time_stamp()

    return_json["meta"]["smartystreets_start"] = time_stamp()
    return_json["smartystreets"] = smartiestreets(address)
    return_json["meta"]["smartystreets_end"] = time_stamp()

    return_json["meta"]["request_end"] = time_stamp()
    ## create response
    ## append response to log
    ## send response
    write_log(logger, return_json)
    return response(200, return_json)

def write_log(log_obj, log_entry):
  log_obj.info('{}'.format(log_entry))

def time_stamp():
  return datetime.now().strftime('%S%f')

def method_not_allowed_response(return_json):
  return_json["error"] = "405 Error - API only supports GET HTTP verb"
  return response(405, return_json)

def bad_request_response(return_json):
  return_json["error"] = "400 Error - Both address (q=) and request id (rid=) must be specified"
  return response(400, return_json)

def response(status_code, response_body=None):
  return {
    'statusCode': status_code,
    'body': json.dumps(response_body) if response_body else json.dumps({}),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
  }

def mapquest(addr):
  return geocoder.mapquest(addr, key='sUvF9V4WHStjrHH3eL6u9NiTmotJLZTs').json

def smartiestreets(addr):
  client = Client('3caeed59-a8a0-b5b6-add7-ee40f7e9fc79', 'Sd1njQ5fN2zN3cXbr3T7')
  return client.street_address(addr)
