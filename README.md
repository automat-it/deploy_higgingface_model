# Hugging Face Model Deployment on AWS

This repository contains tools and scripts for deploying Hugging Face models on AWS using SageMaker and Lambda functions.

## Repository Contents

- **Deploy_HuggingFace_Model.ipynb**: Jupyter notebook for deploying Hugging Face transformer models to AWS SageMaker.
- **Lambda4SagemakerEndpoint.ipynb**: Jupyter notebook demonstrating how to create and configure Lambda functions to interact with SageMaker endpoints.
- **lambda_function.py**: Python script containing the AWS Lambda function code for invoking SageMaker endpoints.
- **export_iam.py**: Utility script for exporting and managing IAM roles and policies required for the deployment.

## Prerequisites

- AWS Account with appropriate permissions
- Python 3.x
- AWS CLI configured
- Required Python packages:
  - boto3
  - sagemaker
  - transformers
  - jupyter

## Setup Instructions

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install boto3 sagemaker transformers jupyter
   ```
3. Configure your AWS credentials:
   ```bash
   aws configure
   ```

## Deployment Process

1. **Prepare your Hugging Face model**:
   - Open `Deploy_HuggingFace_Model.ipynb` to prepare and deploy your model to SageMaker

2. **Set up Lambda function**:
   - Use `Lambda4SagemakerEndpoint.ipynb` to understand how to create a Lambda function
   - Customize `lambda_function.py` for your specific model and use case

3. **Configure IAM permissions**:
   - Run `export_iam.py` to set up the necessary IAM roles and policies

## IAM Requirements

The deployment requires specific IAM permissions:
- SageMaker execution role with S3 access
- Lambda execution role with permissions to invoke SageMaker endpoints
- Trust relationships between services

## Usage

After deployment, you can invoke your model through:
- Direct SageMaker endpoint calls
- Lambda function invocations
- API Gateway (if configured)

## Troubleshooting

Common issues:
- IAM permission errors: Ensure your roles have the correct policies and trust relationships
- S3 access issues: Verify your model artifacts are in the correct region and accessible
- Lambda timeout: Adjust timeout settings for larger models

## License

[Specify your license here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

        Too many current requests. Your queue position is 1. Please wait for a while or switch to other models for a smoother experience.# deploy_higgingface_model
