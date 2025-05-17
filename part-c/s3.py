import boto3

s3 = boto3.client('s3')

# Create bucket
bucket_name = "aryanproject12345"
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket created: {bucket_name}")

# Upload a file
s3.upload_file("C:\\Users\\payal\\Downloads\\Placing a web server in a private s.txt", bucket_name, "test.txt")
print("File uploaded.")
