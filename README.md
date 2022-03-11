# AWS-lambda-textract

Upon uploding an image file onto selected S3 bucket this lambda function will be invoked, the function will automately detect text in images anb save it as a csv file into another selected S3 bucket.

There are some preprocessing needed to be setup:
1. Give lambda the access to S3 and textract in IAM Role (AmazonTextractFullAccess and AWSLambdaExecute)
2. Create two different S3 buckets (one for input and one for output)
3. Set the input S3 as the function trigger, chosse all objest create event

![image](https://user-images.githubusercontent.com/77425545/157826119-e6a406d4-2f28-4bf2-bfc8-c4cbfe5bfdeb.png)

