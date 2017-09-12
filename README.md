# bbb-addr-api

## Features

Accept GET requests only - other HTTP verbs are rejected with a "HTTP 405 - Method Not Allowed"

Requests without a Request ID and address are rejected with a "HTTP 400 - Bad Request"

Logging - All data is captured including the Lambda event (request), start and end time for the entire request-response cycle and each external call.

Python - the code is now all Python 3.6.2 and synchronous

Request IDs - each request must contain a request ID generated on the client when enables complete request tracking

Responses include the exact same data as is logged.

## Example Request

## Features to be Completed

Secure Environment configuration

API key 

Domain Name API using Route53

Real time log file analysis capability

