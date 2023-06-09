import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_ec2_auto_stop_start.cdk_ec2_auto_stop_start_stack import CdkEc2AutoStopStartStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ec2_auto_stop_start/cdk_ec2_auto_stop_start_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEc2AutoStopStartStack(app, "cdk-ec2-auto-stop-start")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
