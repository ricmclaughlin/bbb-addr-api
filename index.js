'use strict'
require('es6-promise').polyfill()
require('isomorphic-fetch')

function CreateQueryUrl (q) {
  let URL = 'http://open.mapquestapi.com/nominatim/v1/search.php?key=axf2kU3ZHapARRIkFtVNEkkxwHEpWtbw&format=json&countrycodes=US&addressdetails=1&limit=1&q='
  return URL + encodeURIComponent(q)
}

function success (result) {
  return {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': '*', // Required for CORS support to work
      'Access-Control-Allow-Credentials': 'true' // Required for cookies, authorization headers with HTTPS
    },
    body: JSON.stringify(result)
  }
}

function internalServerError (msg) {
  return {
    statusCode: 500,
    headers: {
      'Access-Control-Allow-Origin': '*', // Required for CORS support to work
      'Access-Control-Allow-Credentials': true // Required for cookies, authorization headers with HTTPS
    },
    body: JSON.stringify({
      statusCode: 500,
      error: 'Internal Server Error',
      internalError: JSON.stringify(msg)
    })
  }
}

exports.handler = (event, context, callback) => {
  let operation = event.httpMethod
  let runData = {}

  switch (operation) {
    case 'GET':
      runData.rid = event.queryStringParameters.rid
      runData.q = event.queryStringParameters.q
      runData.Url = CreateQueryUrl(runData.q)
      runData.requestStartTime = Date.now()

      fetch(runData.Url)
        .then((resp) => resp.json())
        .then(function (json) {
          runData.requestCompleteTime = Date.now()
          runData.response = (json === []) ? 'not found' : json
        })
        .catch(function (err) {
          runData.requestCompleteTime = Date.now()
          runData.response = err
        })
        .then(function () {
          callback(null, success(runData.response))
        })
      break
    default:
      callback(null, {
        statusCode: 200,
        body: 'error'
      })
  }
}
