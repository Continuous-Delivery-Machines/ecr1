import boto3
import os
if __name__ == '__main__':
    print("hi")

    print('try 1')
    try:
        boto3_session = boto3.session.Session(region_name='us-east-1')
        print(boto3_session.client('sts').get_caller_identity())
    except Exception as e:
        print('e1')
        print(e)

    print('try ')
    try:
        boto3_session = boto3.session.Session()
        print(boto3_session.client('sts').get_caller_identity())
    except Exception as e:
        print('e2')
        print(e)

    print(os.environ)
