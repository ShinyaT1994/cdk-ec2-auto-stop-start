from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_events as events,
    aws_events_targets as targets
)
from constructs import Construct

class CdkEc2AutoStopStartStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # VPC creation with private subnets
        vpc = ec2.Vpc(
            self, "VPC",
            max_azs=2,  # default is all AZs in the region
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name="Private",
                    cidr_mask=24,
                )
            ],
        )

        # Create an EC2 instance
        instance = ec2.Instance(
            self, "Instance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
        )
        
        # Create stop rule
        stop_rule = events.Rule(
            self, 'StopRule',
            schedule=events.Schedule.cron(minute='0', hour='10'),   # 日本時間の19時
            targets=[
                targets.AwsApi(
                    service='EC2',
                    action='stopInstances',
                    parameters={
                        'InstanceIds': [instance.instance_id]
                    },
                )
            ],
        )
        
        # Create start rule
        stop_rule = events.Rule(
            self, 'StartRule',
            schedule=events.Schedule.cron(minute='0', hour='0'),   # 日本時間の9時
            targets=[
                targets.AwsApi(
                    service='EC2',
                    action='startInstances',
                    parameters={
                        'InstanceIds': [instance.instance_id]
                    },
                )
            ],
        )
