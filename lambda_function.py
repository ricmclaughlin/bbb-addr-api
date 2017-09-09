from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
  # print("Received event: " + json.dumps(event, indent=2))
  # print("value1 = " + event['key1'])
  # print("value2 = " + event['key2'])
  # print("value3 = " + event['key3'])
  # return event['key1']  # Echo back the first key value
  # message = 'Hello {} {}!'.format(event['first_name'], 
  #                                 event['last_name'])  
  return response(200, event['queryStringParameters']['first_name'])

def response(status_code, response_body=None):
  return {
    'statusCode': status_code,
    'body': json.dumps(response_body) if response_body else json.dumps({}),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
  }