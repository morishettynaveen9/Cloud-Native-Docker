import boto3

ecr_client=boto3.client('ecr')

repository_name='my-cloud-native-repo'
response=ecr_client.create_repository(repositoryName=repository_name)

repository_uri=response['repository']['repositoryUri'] #repositoryUri (string) –

#The URI for the repository. You can use this URI for container image push and pull operations.
print(repository_uri)