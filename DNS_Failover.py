import boto3

# Initialize boto3 client
client = boto3.client("elbv2", region_name="ap-southeast-2")  # change region if needed

# Replace these ARNs with your actual values
LISTENER_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:listener/app/DNSAutomation/3be55bd9e1ec10c0/8b88ad7fa84aa985"
TG1_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/Targetgroup1/356f9014e7004059"
TG2_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/Targetgroup2/0f48205b9cf739c7"

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
    print("=== ALB Traffic Control ===")
    print("1. Route 100% to TargetGroup1")
    print("2. Route 100% to TargetGroup2")
    print("3. Route 50/50 between TG1 and TG2")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
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
