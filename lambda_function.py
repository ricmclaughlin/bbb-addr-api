from __future__ import print_function

import json
import geocoder
from smartystreets import Client

def lambda_handler(event, context):
  return_json = {}
  my_address = str('12497 Leopard St, 78410')
  g = geocoder.mapquest(my_address, key='sUvF9V4WHStjrHH3eL6u9NiTmotJLZTs')
  return_json["mapquest"] = g.json
  client = Client('3caeed59-a8a0-b5b6-add7-ee40f7e9fc79', 'Sd1njQ5fN2zN3cXbr3T7')
  m = client.street_address(my_address)
  return_json["smartystreets"] = m
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


  

# for mapquest
# http://geocoder.readthedocs.io/providers/MapQuest.html
# pip install geocoder
# pip install mapq
# i have both packages installed, geocoder may be the only one necessary 



# print(g.json['lat'])
# print(g.json['lng'])
# print(g.json['raw']['street'])
# print(g.json['city'])
# print(g.json['state'])
# print(g.json['raw']['postalCode'])

# for smarty streets
# https://pypi.python.org/pypi/smartystreets.py
# pip install smartystreets.py


# client = Client('3caeed59-a8a0-b5b6-add7-ee40f7e9fc79', 'Sd1njQ5fN2zN3cXbr3T7')

# m = client.street_address(my_address)
# print(m)