import logging

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Harry's AWS Security Lab")
s3 = boto3.client("s3", region_name="us-east-1")

BUCKET = "example-security-lab-222222222222-data"
KEY = "hello.txt"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    try:
        response = s3.get_object(Bucket=BUCKET, Key=KEY)
        body = response["Body"]
        try:
            message = body.read().decode("utf-8")
        finally:
            body.close()
        return {"message": message}
    except (ClientError, BotoCoreError):
        logging.exception("Unable to read the lab object")
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve the lab file",
        )
