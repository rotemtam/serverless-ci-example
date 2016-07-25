
import boto3
from json import dumps

client = boto3.client('apigateway', region_name='us-east-1')

class ApiGatewayDeployer:

    def __init__(self, **kw):
        self.project = kw['project']
        self.swagger = kw['swagger']

    def deploy(self):

        response = client.put_rest_api(
            restApiId=self.project.rest_api_id,
            mode='overwrite',
            failOnWarnings=True,
            parameters={
                'stageName': self.project.stage_name
            },
            body=bytes(dumps(self.swagger))
        )

        print response

        response = client.create_deployment(
            restApiId=self.project.rest_api_id,
            stageName=self.project.stage_name,
            stageDescription=self.project.stage_name,
            description=self.project.description
        )

        print response
