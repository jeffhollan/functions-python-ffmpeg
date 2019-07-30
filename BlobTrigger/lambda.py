import json
import ffmpy3
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    print("Python S3 trigger fired.")

    with open('input.mp4', 'wb') as f:
        s3.download_file(event['Records'][0]['s3']['bucket']['name'], event['Records'][0]['s3']['object']['name'], f)

    ff = ffmpy3.FFmpeg(
     executable='ffmpeg',
     inputs={'input.mp4': None},
     outputs={'output_%d.png': '-y -vf fps=1'}
    )
    ff.run()

    return {
        'statusCode': 200,
        'body': json.dumps('Created output file')
    }

