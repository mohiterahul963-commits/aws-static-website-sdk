import boto3
import json

REGION = "ap-south-1"
BUCKET_NAME = "rahul-aws-static-website-2026-98765"

s3 = boto3.client("s3", region_name=REGION)

print("Setting S3 bucket policy...")

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }
    ]
}

s3.put_bucket_policy(
    Bucket=BUCKET_NAME,
    Policy=json.dumps(bucket_policy)
)

print("Public read policy applied successfully!")