# DNS Automation – Blue/Green Deployment & AWS Traffic Management

This project automates application deployment and traffic management between two AWS EC2 instances behind an Application Load Balancer (ALB).  
It supports **Blue/Green deployments** and **zero-downtime rollouts** using **Python (boto3)** and **GitHub Actions**.

---

## Overview

- Deploys Python apps to EC2 servers via SSH.
- Updates ALB listener rules to switch traffic between Target Groups (TG1 & TG2).
- Supports manual approval and automated failover.
- Designed for reliable, repeatable CI/CD on AWS.

---

## Files & Structure

DNS-Automation/
│
├── app.py # Flask app or simple Python service
├── traffic_route.py # Manages ALB target group weights
├── dns_failover.py # Automates Blue/Green traffic shift
├── servers.json # Stores EC2 IPs for DC1 and DC2
├── requirements.txt # Python dependencies
│
└── .github/workflows/ # GitHub Actions workflows
├── deploy-ec2.yml
├── traffic-control.yml
└── dns-failover.yml

yaml
Copy code

---

## servers.json Example

```json
{
  "servers": {
    "DC1": "13.236.134.76",
    "DC2": "13.211.169.112"
  }
}
traffic_route.py Example
python
Copy code
import boto3, os

client = boto3.client("elbv2", region_name="ap-southeast-2")

LISTENER_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:listener/app/lb/0e7d0e802887583f/dd6a61a61f5ab6ce"
TG1_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/tg1/5ec821881ea56bfc"
TG2_ARN = "arn:aws:elasticloadbalancing:ap-southeast-2:820345161521:targetgroup/tg2/f59fe3e806da9967"

def modify_traffic(weight_tg1, weight_tg2):
    client.modify_listener(
        ListenerArn=LISTENER_ARN,
        DefaultActions=[{
            "Type": "forward",
            "ForwardConfig": {
                "TargetGroups": [
                    {"TargetGroupArn": TG1_ARN, "Weight": weight_tg1},
                    {"TargetGroupArn": TG2_ARN, "Weight": weight_tg2}
                ]
            }
        }]
    )
    print(f"✅ Traffic updated: TG1={weight_tg1}, TG2={weight_tg2}")

choice = os.environ.get("traffic")
if choice == "1":
    modify_traffic(1, 0)
elif choice == "2":
    modify_traffic(0, 1)
elif choice == "3":
    modify_traffic(1, 1)
else:
    print("❌ Invalid traffic value (use 1, 2, or 3)")
GitHub Secrets Required
Name	Description
AWS_ACCESS_KEY_ID	IAM access key
AWS_SECRET_ACCESS_KEY	IAM secret key
EC2_SSHKEY	PEM key for EC2 SSH

Requirements
nginx
Copy code
boto3
flask
Install locally:

bash
Copy code
pip install -r requirements.txt
Example GitHub Action Step
yaml
Copy code
- name: Route traffic
  env:
    traffic: "2"   # 1=TG1, 2=TG2, 3=50/50
  run: python3 traffic_route.py
Author
Sahil Siddharth
Cloud & DevOps Engineer
GitHub: @sahilsidd904

License
MIT License © 2025 Sahil Siddharth

yaml
Copy code

---

✅ **To use:**
1. Copy all text above.  
2. Paste into your `README.md`.  
3. Commit & push:
   ```bash
   git add README.md
   git commit -m "Add project README"
   git push origin main
