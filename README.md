# Aws-cloud-image-copy-project

#here's step by step tutorial on how to do this project:

# S3 to S3 Image Copy with AWS Lambda

This project uses AWS Lambda to automatically copy images from one S3 bucket to another when a new image is uploaded.

## Architecture
- **Source Bucket:** `aws-project-source-bucket12`
- **Destination Bucket:** `aws-project-destination-bucket12`
- **Trigger:** S3 `PUT` event
- **Permissions:** IAM policy attached to the Lambda function

## Setup Steps
1. Create two S3 buckets.
2. Create a Lambda function with a trigger on the source bucket.
3. Attach an IAM role with permissions for `s3:GetObject`, `s3:ListBucket`, and `s3:PutObject`.
4. Deploy the function and upload an image to see it copied automatically!

## Lambda Code
See [lambda_function.py](lambda_function.py).

## IAM Policy
See [iam-policy.json](iam-policy.json).

## How to Test
1. Upload an image to the source bucket.
2. Check the destination bucket for the copied image.

