#!/bin/bash
#A script that takes in a URL an an argument, sends a GET request to the URL nad displays the response.
curl -X GET -H "X-School-User-Id: 98" -s "$1"
