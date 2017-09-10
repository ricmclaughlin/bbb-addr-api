from datetime import datetime
import json
import geocoder
from smartystreets import Client
import logging

def lambda_handler(event, context):
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  response_body = {}
  response_json = {}
  response_body["meta"] = {}
  response_body["meta"]["request_start"] = time_stamp()
  response_body["meta"]["event"] = event
  
  if event["httpMethod"] != "GET":
    response_body["meta"]["request_end"] = time_stamp()
    response_json = method_not_allowed_response(response_body)
    write_log(logger, response_json)
    return response_json

  try:
    request_id = event["queryStringParameters"]["rid"]
    address = event["queryStringParameters"]["q"]
  except KeyError:
    response_body["meta"]["request_end"] = time_stamp()
    response_json = bad_request_response(response_body)
    write_log(logger, response_json)
    return response_json

  else:
    response_body["meta"]["mapquest_start"] = time_stamp()
    response_body["mapquest"] = mapquest(address)
    response_body["meta"]["mapquest_end"] = time_stamp()

    response_body["meta"]["smartystreets_start"] = time_stamp()
    response_body["smartystreets"] = smartiestreets(address)
    response_body["meta"]["smartystreets_end"] = time_stamp()

    response_body["meta"]["request_end"] = time_stamp()

    write_log(logger, response_body)
    return response(200, response_body)

def write_log(log_obj, log_entry):
  log_obj.info('{}'.format(log_entry))

def time_stamp():
  return datetime.now().strftime('%S%f')

def method_not_allowed_response(body):
  body["error"] = "405 Error - API only supports GET HTTP verb"
  return response(405, body)

def bad_request_response(body):
  body["error"] = "400 Error - Both address (q=) and request id (rid=) must be specified"
  return response(400, body)

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
