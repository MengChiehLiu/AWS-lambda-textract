"""
AWS lambda textract
Meng-Chieh, Liu
2022 March 11th 15:11
"""

import json
import boto3
import os
from urllib.parse import unquote_plus

# Get connection to AWS S3 and textract
s3 = boto3.resource('s3')
bucket_output = s3.Bucket("s3_bucket_name") # your output S3 bucket name
textract = boto3.client("textract")

# Transfer response into text line
def extract_text(response, extract_by="LINE"):
    line_text = ""
    for block in response["Blocks"]:
        if block["BlockType"] == extract_by:
            line_text += block["Text"]+"\n"
    return line_text

# Get textract response
def getTextractData(bucketName, filename):
    response = textract.detect_document_text(
        Document={
            "S3Object": {
                "Bucket": bucketName,
                "Name": filename,
            }
        }
    )
    detectedText = extract_text(response, extract_by="LINE")
    return detectedText

def lambda_handler(event, context):
    if event:

        # Get event infoemation
        file_obj = event["Records"][0]
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        filename = unquote_plus(str(file_obj["s3"]["object"]["key"]))

        # Get textract data
        detectedText=getTextractData(bucketname,filename)

        # Generate data path
        generateFilePath = os.path.splitext(filename)[0]+'.txt'

        # Put object on S3
        bucket_output.put_object(Body=detectedText, Key=generateFilePath)

        return {
            "statusCode": 200,
            "body": json.dumps("Document processed successfully!"),
        }

    return {"statusCode": 500, "body": json.dumps("There is an issue!")}
