# AWS-lambda-textract

Upon uploding an image file onto selected S3 bucket this lambda function will be invoked, the function will automately detect text in images anb save it as a csv file into another selected S3 bucket.

There are some preprocessing needed to be setup:
1. Give lambda the access to S3 and textract in IAM Role

Configuration --> Permissions --> Click your execution role --> add permissions --> attach policies --> Add AmazonTextractFullAccess and AWSLambdaExecute

![image](https://user-images.githubusercontent.com/77425545/157827168-a5107177-c6d2-4903-90cc-f90baef4087a.png)

2. Create two different S3 buckets (one for input and one for output)
3. Set the input S3 as the function trigger, chosse all objest create event

![image](https://user-images.githubusercontent.com/77425545/157827280-6ccdd120-4e8d-4192-9c1a-6c175b3af30a.png)

