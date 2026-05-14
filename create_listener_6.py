import boto3

elb = boto3.client("elbv2")

elb.create_listener(
    LoadBalancerArn="arn:aws:elasticloadbalancing:ap-south-1:475432297908:loadbalancer/app/MultiTierALB/1fd6e9e31422c6a5",
    Protocol="HTTP",
    Port=80,
    DefaultActions=[{
        "Type":"fixed-response",
        "FixedResponseConfig":{
            "StatusCode":"200",
            "ContentType":"text/plain",
            "MessageBody":"Multi-tier App Running"
        }
    }]
)

print("Listener Created")