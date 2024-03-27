#!/bin/bash
#A script that takes in a URL, and sends POST to the passed URL nad displays the body of the response
curl -X POST -d "email=$email$subject=$subject" -s "$1"
