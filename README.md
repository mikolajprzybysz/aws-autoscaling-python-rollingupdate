# Deploy

# Run with docker
## Setup
First you have to run python container and all dependencies

    docker run -it -v $PWD:/app -w /app python:3-alpine sh
    pip install -r requirements.txt

Once we have all that configure aws credentials
    
    aws configure 

## Run
### Prerequisits


## Test

    python -m unittest test.py