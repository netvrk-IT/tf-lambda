import json
import boto3

config_client = boto3.client('config')
def lambda_handler(event, context):
    
    # Get non compliant resources from AWS Config, based on Config rules
    
    response = config_client.get_compliance_details_by_config_rule(
    ConfigRuleName='s3-bucket-server-side-encryption-enabled',
    ComplianceTypes=['NON_COMPLIANT'],
    )
    non_compliant=json.loads(json.dumps(response, default=str))
    #return response
    eval_result=non_compliant.get('EvaluationResults')
    for e in eval_result: 
        non_comp_rsc = e.get('EvaluationResultIdentifier').get('EvaluationResultQualifier').get('ResourceId')
        
    # encrypt s3 bucket
    s3_client = boto3.client('s3')
    response = s3_client.put_bucket_encryption(
    Bucket=non_comp_rsc,
    ServerSideEncryptionConfiguration={
        'Rules':[
            {
                'ApplyServerSideEncryptionByDefault':{
                    'SSEAlgorithm': 'AES256'
                }
            },
        ]
    }
)

    # Send SNS Notification to AWS Team about Non-Compliant-resources
    sns_client = boto3.client('sns')
    response = sns_client.publish(
    TopicArn='arn_ID',
    Message='Hello, this is a message generated by Lambda because there were some Unencrypted S3 Buckets in your AWS Account, I have remediated these resources for you. Nothing for you to do!' + non_comp_rsc,
    Subject='Unencrypted S3 Buckets'
)
print('It Works')
