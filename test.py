import time
import hashlib
import unittest
from unittest.mock import patch, call, MagicMock
from src.asg import RollingAsg

hash = MagicMock()
hash.hexdigest.return_value = '47bce5c74f589f4867dbd57e9ca9f808'

class MyTestCase(unittest.TestCase):

    @patch('hashlib.md5', return_value=hash)
    @patch('time.sleep', return_value=None)
    def test(self, patched_time_sleep, patched_hashlib):
        new_ami='sampleami'
        new_lc = 'app-lc-47bce5c7'
        client = MagicMock()
        client.create_launch_configuration.return_value=None
        client.update_auto_scaling_group.return_value=None
        client.update_auto_scaling_group.return_value=None
        
        RollingAsg(new_ami, client).update()

        patched_hashlib.assert_called_once_with(new_ami.encode())
        hash.hexdigest.assert_called()
        patched_time_sleep.assert_called_once_with(300)
        client.assert_has_calls([
            call.create_launch_configuration(
                LaunchConfigurationName=new_lc,
                ImageId=new_ami,
                InstanceType='t2.micro',
                AssociatePublicIpAddress=False
            ),
            call.update_auto_scaling_group(
                AutoScalingGroupName='app-asg',
                LaunchConfigurationName=new_lc,
                MinSize=6,
                MaxSize=6
            ),
            call.update_auto_scaling_group(
                AutoScalingGroupName='app-asg',
                LaunchConfigurationName=new_lc,
                MinSize=3,
                MaxSize=3
            )
        ])
        
if __name__ == '__main__':
    unittest.main()