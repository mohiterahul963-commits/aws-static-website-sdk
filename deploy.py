import boto3
import json
import os
from botocore.exceptions import ClientError

# ============================================================
# AWS Static Website Deployment using Python + Boto3
# ============================================================

BUCKET_NAME = "rahul-aws-static-website-2026-98765"
REGION = "ap-south-1"
WEBSITE_FILE = os.path.join("website", "index.html")


# ------------------------------------------------------------
# Create S3 client
# ------------------------------------------------------------
s3 = boto3.client("s3", region_name=REGION)


# ------------------------------------------------------------
# Check if bucket exists
# ------------------------------------------------------------
def bucket_exists():
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
        return True

    except ClientError as error:
        error_code = error.response["Error"]["Code"]

        if error_code in ["404", "NoSuchBucket"]:
            return False

        raise


# ------------------------------------------------------------
# Create bucket
# ------------------------------------------------------------
def create_bucket():
    print("Creating S3 bucket...")

    try:
        if REGION == "us-east-1":
            s3.create_bucket(Bucket=BUCKET_NAME)
        else:
            s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={
                    "LocationConstraint": REGION
                }
            )

        print("S3 bucket created successfully!")

    except ClientError as error:
        error_code = error.response["Error"]["Code"]

        if error_code in ["BucketAlreadyOwnedByYou"]:
            print("Bucket already exists.")

        else:
            raise


# ------------------------------------------------------------
# Upload website
# ------------------------------------------------------------
def upload_website():
    print("Uploading index.html...")

    s3.upload_file(
        WEBSITE_FILE,
        BUCKET_NAME,
        "index.html",
        ExtraArgs={
            "ContentType": "text/html"
        }
    )

    print("index.html uploaded successfully!")


# ------------------------------------------------------------
# Enable static website hosting
# ------------------------------------------------------------
def enable_website_hosting():
    print("Configuring static website hosting...")

    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {
                "Suffix": "index.html"
            }
        }
    )

    print("Static website hosting enabled!")


# ------------------------------------------------------------
# Disable S3 Block Public Access
# ------------------------------------------------------------
def disable_block_public_access():
    print("Configuring public access settings...")

    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False
        }
    )

    print("Public access settings configured!")


# ------------------------------------------------------------
# Apply public-read bucket policy
# ------------------------------------------------------------
def apply_bucket_policy():
    print("Setting S3 bucket policy...")

    policy = {
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
        Policy=json.dumps(policy)
    )

    print("Public read policy applied successfully!")


# ------------------------------------------------------------
# Display website URL
# ------------------------------------------------------------
def show_website_url():
    website_url = (
        f"http://{BUCKET_NAME}.s3-website."
        f"{REGION}.amazonaws.com"
    )

    print("\n" + "=" * 60)
    print("DEPLOYMENT COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    print(f"\nWebsite URL:")
    print(website_url)

    print("\nBucket:")
    print(BUCKET_NAME)

    print("\nRegion:")
    print(REGION)

    print("=" * 60)


# ------------------------------------------------------------
# Main deployment process
# ------------------------------------------------------------
def main():

    print("=" * 60)
    print("AWS STATIC WEBSITE DEPLOYMENT")
    print("Python + Boto3 + Amazon S3")
    print("=" * 60)

    # Check website file
    if not os.path.exists(WEBSITE_FILE):
        print(f"\nERROR: {WEBSITE_FILE} not found.")
        print("Make sure index.html is inside the website folder.")
        return

    # Step 1: Check/Create bucket
    print("\n[1/6] Checking S3 bucket...")

    if bucket_exists():
        print("S3 bucket already exists!")
    else:
        create_bucket()

    # Step 2: Upload website
    print("\n[2/6] Uploading website...")
    upload_website()

    # Step 3: Enable website hosting
    print("\n[3/6] Enabling static website hosting...")
    enable_website_hosting()

    # Step 4: Configure public access
    print("\n[4/6] Configuring public access...")
    disable_block_public_access()

    # Step 5: Apply bucket policy
    print("\n[5/6] Applying bucket policy...")
    apply_bucket_policy()

    # Step 6: Show website URL
    print("\n[6/6] Generating website URL...")
    show_website_url()


# ------------------------------------------------------------
# Run application
# ------------------------------------------------------------
if __name__ == "__main__":
    main()