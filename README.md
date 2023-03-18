# cdk_fargate_s3

## Description

This repo leverages cdk to deploy an load balanced fargate service (using cached credentials), and includes a containerized script to create s3 buckets given an input parameter.

## Dependencies
[CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

[Python3](https://www.python.org/downloads/)

[Docker](https://www.docker.com/)


## Usage
### 1. Copy source code
  - Create a dir for the git repo
  ```
  git clone https://github.com/Aartichoke/cdk_fargate_s3.git
  ```
  - Enter directory
  ```
  cd cdk_fargate_s3
  ```
### 2. Environment setup
  - Create a new python venv
  ```
  cdk init --language python
  ```
  - Activate the virtual environment
  ```
  source .venv/bin.activate
  ```
  - Update pip
  ```
  pip install --upgrade pip
  ```
  - Install required python packages
  ```
  pip install .
  ```
### 3. Use CDK to deploy
  - Bootstrap cdk environment
  ```
  cdk bootstrap
  ```
  - Synth to check if cloudformation template can be generated without issue
  ```
  cdk synth
  ```
  - If successful, use deploy for the VPC and ECS
  ```
  cdk deploy
  ```
### 4. Run the job
  - Find the url for the fargate service from the cloudformation template
  ```
    FargateStackserviceServiceURL34815BBD:
    Value:
      Fn::Join:
        - ""
        - - http://
          - Fn::GetAtt:
              - FargateStackserviceLB2BAB169B

  ```
  - Send run command to fargate service endpoint
  ```
  curl -s http://<url>:80 | jq {"bucket_name":"im_a_bus"}
  ```
 
## Cleanup
```
cdk destroy
```
