# Rolling updates for autoscaling group with python
Deploy script creates new launch configuration for the new ami id then updates autoscaling group to use it and doubles the desired instaces count, 
then it waits 4minutes for the instances to boot up and setup and scales down to original value. This way autoscaling group kills old instances with the old image.

# Run with docker
## Setup
First you have to run python container and all dependencies

    docker run -it -v $PWD:/app -w /app python:3-alpine sh
    pip install -r requirements.txt

Once we have all that, configure aws credentials
    
    aws configure 

## Run
### Prerequisits
I assume you have autoscaling group with the name 'app-asg'

    ./deploy oldimageid newimageid

## Test

    python -m unittest test.py