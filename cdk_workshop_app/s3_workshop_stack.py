from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct

class S3WorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        my_bucket = s3.Bucket(self, "my_clip_workshop_bucket", 
            bucket_name="dev-my-clip-techlead-serch-v2")