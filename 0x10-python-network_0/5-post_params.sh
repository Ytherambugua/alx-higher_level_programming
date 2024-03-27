#!/bin/bash
#A script that takes in a URL, and sends POST to the passed URL nad displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com=I will always be here for PLD"
