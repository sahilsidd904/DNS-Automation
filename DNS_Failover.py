import boto3
import os

# Initialize boto3 client
client = boto3.client("elbv2", region_name="ap-southeast-2")  # change region if needed

# Replace these ARNs with your actual values
LISTENER_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:listener/app/lb/0e7d0e802887583f/dd6a61a61f5ab6ce"
TG1_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/tg1/5ec821881ea56bfc"
TG2_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/tg2/f59fe3e806da9967"

def modify_traffic(weight_tg1, weight_tg2):
    """Modify listener rule to set traffic weights."""
    response = client.modify_listener(
        ListenerArn=LISTENER_ARN,
        DefaultActions=[
            {
                "Type": "forward",
                "ForwardConfig": {
                    "TargetGroups": [
                        {"TargetGroupArn": TG1_ARN, "Weight": weight_tg1},
                        {"TargetGroupArn": TG2_ARN, "Weight": weight_tg2}
                    ]
                }
            }
        ]
    )
    print(f"✅ Traffic updated: TG1={weight_tg1}, TG2={weight_tg2}")
    return response

def main():
    choice=os.environ.get("traffic")
    
    if choice == "1":
        modify_traffic(1, 0)
    elif choice == "2":
        modify_traffic(0, 1)
    elif choice == "3":
        modify_traffic(1, 1)
    else:
        print("❌ Invalid choice, please run again.")

if __name__ == "__main__":
    main()
