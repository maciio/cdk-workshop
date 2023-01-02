#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import (
    Environment
)

from cdk_workshop_app.cdk_workshop_app_stack import CdkWorkshopAppStack
from cdk_workshop_app.s3_workshop_stack import S3WorkshopStack
from cdk_workshop_app.lambda_workshop_stack import LambdaWorkshopStack
from config_loader import settings
from config_loader import ConfigurationLoader

environment = Environment(region=settings["aws_region"], account=settings["AWS_ACCOUNT"])
app = cdk.App()

workshop_stack_name=ConfigurationLoader.build_naming_convention("main")
CdkWorkshopAppStack(app, workshop_stack_name,
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    env=environment
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
# S3
s3_stack_name=ConfigurationLoader.build_naming_convention("s3")
s3_stack = S3WorkshopStack(app,s3_stack_name, env=environment)

# Lambda
lambda_stack_name=ConfigurationLoader.build_naming_convention("lambda")
LambdaWorkshopStack(app, lambda_stack_name).add_dependency(s3_stack)



app.synth()
