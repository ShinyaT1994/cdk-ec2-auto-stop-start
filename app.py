#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_ec2_auto_stop_start.cdk_ec2_auto_stop_start_stack import CdkEc2AutoStopStartStack


app = cdk.App()
CdkEc2AutoStopStartStack(app, "CdkEc2AutoStopStartStack")

app.synth()
