from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as cdk_lambda
)
from constructs import Construct
from config_loader import settings
from config_loader import ConfigurationLoader


class LambdaWorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_name=ConfigurationLoader.build_simple_name("my-first-lambda")
        my_lambda = cdk_lambda.Function(self, lambda_name,
        runtime=cdk_lambda.Runtime.PYTHON_3_9,
        code=cdk_lambda.Code.from_asset("lambda"),
        handler="hello.handler")
