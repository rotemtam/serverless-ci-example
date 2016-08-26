#!/bin/bash

PATH_TO_AWS_CREDENTIALS=~/.aws/credentials
AWS_REGION=us-east-1

# build the image
docker build . -t apex-lambda-deployer

# run unit tests
docker run apex-lambda-deployer npm test

# deploy
docker run -e AWS_REGION=$AWS_REGION -v $PATH_TO_AWS_CREDENTIALS:/root/.aws/credentials apex-lambda-deployer
