import boto3
import hashlib
import time

class RollingAsg(object):
    def __init__(self, new_ami, client):
        self.new_ami = new_ami
        self.client_asg = client

    def update(self):
        new_ami_hash = hashlib.md5(self.new_ami.encode()).hexdigest()[:8]
        client_asg = self.client_asg

        new_lc = 'app-lc-' + new_ami_hash
        client_asg.create_launch_configuration(
            LaunchConfigurationName=new_lc,
            ImageId=self.new_ami,
            InstanceType='t2.micro',
            AssociatePublicIpAddress=False,

        ) 

        client_asg.update_auto_scaling_group(
            AutoScalingGroupName='app-asg',
            LaunchConfigurationName=new_lc,
            MinSize=6,
            MaxSize=6
        )

        time.sleep(300) 

        client_asg.update_auto_scaling_group(
            AutoScalingGroupName='app-asg',
            LaunchConfigurationName=new_lc,
            MinSize=3,
            MaxSize=3
        )