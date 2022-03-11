# AWS-lambda-textract

Upon uploding an image file onto selected S3 bucket this lambda function will be invoked, the function will automately detect text in images anb save it as a csv file into another selected S3 bucket.

There are some preprocessing needed to be setup:
1. Give lambda the access to S3 and textract in IAM Role (AmazonTextractFullAccess and AWSLambdaExecute)
Configuration --> Permissions --> Click your execution role --> add permissions --> attach policies --> AmazonTextractFullAccess and AWSLambdaExecute
![image](https://user-images.githubusercontent.com/77425545/157826588-a58b52a9-c17c-4eaa-a315-9eedd50e9136.png)
![image](https://user-images.githubusercontent.com/77425545/157826991-9805e42e-9e9c-4a5f-9f33-9c1a70f6c992.png)

3. Create two different S3 buckets (one for input and one for output)
4. Set the input S3 as the function trigger, chosse all objest create event
