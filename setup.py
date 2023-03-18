import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="cdk_fargate_s3",
    version="0.0.1",

    description="A demo fargate service that creates s3 buckets",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="aartichoke",

    python_requires=">=3.7",

    install_requires=[
        "aws-cdk-lib",
        "constructs",
        "boto3",
    ],

)