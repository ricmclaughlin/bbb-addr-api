'use strict'
require('es6-promise').polyfill()
require('isomorphic-fetch')

let URL = 'http://open.mapquestapi.com/nominatim/v1/search.php?key=5Vb6GgAU6Syvx0cGys6CHSh0aDb9vAg3&format=json&format=json&q=windsor+[castle]&addressdetails=1&limit=3&viewbox=-1.99%2C52.02%2C0.78%2C50.94&exclude_place_ids=41697'
exports.handler = (event, context, callback) => {
  let operation = event.httpMethod

  switch (operation) {
    case 'GET':
      callback(null, success('hi, alive'))
      break
    case 'POST':
      fetch(URL)
      .then((resp) => resp.json())
      .then(function (json) {
        callback(null, success(json))
      })
      .catch(function (err) {

      })
      break
    default:
      callback(null, {
        statusCode: 200,
        body: 'error'
      })
  }
}

// http://open.mapquestapi.com/nominatim/v1/search.php?key=5Vb6GgAU6Syvx0cGys6CHSh0aDb9vAg3&format=json&q=windsor+[castle]&addressdetails=1&limit=3&viewbox=-1.99%2C52.02%2C0.78%2C50.94&exclude_place_ids=41697
// {
//   "city": "San Diego",
//   "input_id": "2",
//   "state": "CA",
//   "street": "4747 Viewridge Ave #200",
//   "zipcode": "92123-1688"
// }

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
