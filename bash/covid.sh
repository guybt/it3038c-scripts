#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
CURRENTLYHOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
CUMULATIVEHOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCumulative')
DEATH=$(echo $DATA | jq '.[0].death')

echo "On $TODAY, there were $POSITIVE positive COVID cases"
echo "As of $TODAY, there are currently $CURRENTLYHOSPITAL people hospitalized"
echo "A total of $CUMULATIVEHOSPITAL, have been hospitalized by COVID to date"
echo "As of $TODAY, $DEATH people have died to COVID"

