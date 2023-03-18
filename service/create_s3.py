from fastapi import FastAPI, HTTPException
import boto3

# Create a Python script using boto3 that takes a 
# bucket name parameter and creates an S3 bucket with that name. 
# It’s safe to assume that we have our aws-cli configured and boto3 
# will use the aws_access_key_id and aws_secret_access_key from ~/.aws/credentials.

app = FastAPI(title="s3Service")

@app.get("/bucket/{bucket_name}")
def get_message(bucket_name: str):
    # Create a bucket using boto3 - how very non-cdk of us!
    s3_client = boto3.client('s3')
    try:
        # attempt to create bucket, raise exception on failure for this basic example
        response = s3_client.create_bucket(Bucket=bucket_name)
        # Response Syntax
        # {'Location': 'string' }
        return {"bucket_name": response['Location']}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to create bucket.")