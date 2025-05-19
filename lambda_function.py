import json
import boto3

def lambda_handler(event, context):
    # Initialize SageMaker runtime client
    sagemaker_client = boto3.client('sagemaker-runtime')

    # SageMaker endpoint name
    endpoint_name = 'huggingface-distilbert-endpoint'

    # Get input data from event
    try:
        input_data = event.get('inputs')
        if not input_data:
            raise ValueError("Missing 'inputs' in event")
        payload = {'inputs': input_data}
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Invalid input: {str(e)}')
        }

    # Invoke SageMaker endpoint
    try:
        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=json.dumps(payload)
        )
        result = json.loads(response['Body'].read().decode())
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Endpoint error: {str(e)}')
        }
