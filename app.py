from aws_cdk import App
from fargate_stack.fargate_stack import FargateStack
app = App()

# skip making a cdk pipeline
FargateStack(app, "FargateStack")
app.synth()