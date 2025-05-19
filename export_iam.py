import boto3
import json
import datetime

# Initialize IAM client
iam_client = boto3.client('iam')

# Function to get all roles and their details
def export_iam_roles():
    roles_data = []
    
    # List all roles
    response = iam_client.list_roles()
    roles = response['Roles']
    
    # Handle pagination
    while 'Marker' in response:
        response = iam_client.list_roles(Marker=response['Marker'])
        roles.extend(response['Roles'])
    
    for role in roles:
        role_name = role['RoleName']
        role_arn = role['Arn']
        
        # Get role details
        role_details = iam_client.get_role(RoleName=role_name)['Role']
        
        # Get trust policy
        trust_policy = role_details.get('AssumeRolePolicyDocument', {})
        
        # Get attached managed policies
        attached_policies = []
        attached_response = iam_client.list_attached_role_policies(RoleName=role_name)
        for policy in attached_response.get('AttachedPolicies', []):
            attached_policies.append({
                'PolicyName': policy['PolicyName'],
                'PolicyArn': policy['PolicyArn']
            })
        
        # Get inline policies
        inline_policies = []
        inline_response = iam_client.list_role_policies(RoleName=role_name)
        for policy_name in inline_response.get('PolicyNames', []):
            policy_doc = iam_client.get_role_policy(
                RoleName=role_name,
                PolicyName=policy_name
            )['PolicyDocument']
            inline_policies.append({
                'PolicyName': policy_name,
                'PolicyDocument': policy_doc
            })
        
        # Get permission boundary (if any)
        permission_boundary = role_details.get('PermissionsBoundary', {}).get('PermissionsBoundaryArn', None)
        
        # Structure role data
        role_data = {
            'RoleName': role_name,
            'RoleArn': role_arn,
            'TrustPolicy': trust_policy,
            'AttachedPolicies': attached_policies,
            'InlinePolicies': inline_policies,
            'PermissionBoundary': permission_boundary,
            'CreatedDate': role_details['CreateDate'].isoformat(),
            'RoleId': role_details['RoleId']
        }
        roles_data.append(role_data)
    
    return roles_data