#!/bin/bash

PROFILE="skyline"

aws --profile $PROFILE lambda update-function-code --function-name chestday-waveform-lambda --zip-file fileb://output/lambda_code.zip
