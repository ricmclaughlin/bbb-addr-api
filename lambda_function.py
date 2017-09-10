from __future__ import print_function
from datetime import datetime
import json
import geocoder
from smartystreets import Client
import logging

def lambda_handler(event, context):
  return_json = {}
  call_timestamps = {}
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  my_address = str('12497 Leopard St, 78410')
  
  call_timestamps["mapquest_start"] = datetime.now().strftime('%S%f')
  g = geocoder.mapquest(my_address, key='sUvF9V4WHStjrHH3eL6u9NiTmotJLZTs')
  return_json["mapquest"] = g.json
  call_timestamps["mapquest_end"] = datetime.now().strftime('%S%f')

  call_timestamps["smartystreets_start"] = datetime.now().strftime('%S%f')
  client = Client('3caeed59-a8a0-b5b6-add7-ee40f7e9fc79', 'Sd1njQ5fN2zN3cXbr3T7')
  m = client.street_address(my_address)
  return_json["smartystreets"] = m
  call_timestamps["smartystreets_end"] = datetime.now().strftime('%S%f')
  return_json["timing"] = call_timestamps
  return_json["event"] = event
  logger.info('{}'.format(return_json))
  return response(200, return_json)

def response(status_code, response_body=None):
  return {
    'statusCode': status_code,
    'body': json.dumps(response_body) if response_body else json.dumps({}),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
  }
