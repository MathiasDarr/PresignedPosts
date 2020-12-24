#!/bin/bash


bucketname=dakobed-sqs-transform-bucket
aws s3 rb s3://${bucketname} --force

if [[ -z $2 ]]
then
  stackname=serverles-transcriptions-api-stack
else
  stackname=$2
fi

aws cloudformation delete-stack --stack-name ${stackname}
