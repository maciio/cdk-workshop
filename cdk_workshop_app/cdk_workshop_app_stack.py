from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_ssm as ssm
    # aws_sqs as sqs,
)
from constructs import Construct
from config_loader import settings
from config_loader import ConfigurationLoader

class CdkWorkshopAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        test_param_id=ConfigurationLoader.build_simple_name("my-test-param")
        ssm_test_param = ssm.StringParameter(self, test_param_id, parameter_name=settings["ssm.new"],string_value=" My dummy value")
        
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkWorkshopAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
