import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'aws-project-source-bucket12'
    file_name = 'test-image.jpg'
    file_content = b'Hello, this is a test image'  # Replace with actual image bytes

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    print(f"{file_name} uploaded successfully to {bucket_name}")
