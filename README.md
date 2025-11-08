# DNS Automation – Blue/Green Deployment & AWS Traffic Management

Automates EC2 deployments and manages AWS ALB traffic using GitHub Actions and Python (boto3).
Supports Blue/Green rollouts, failover, and zero-downtime updates.

---

## Overview

This project automates:
- Deploying Python apps to AWS EC2 servers via SSH.
- Managing ALB listener rules to shift traffic between Target Groups.
- Performing Blue/Green deployments between DC1 and DC2.
- Optional manual approval in GitHub Actions before switching live traffic.

---

## Repository Structure

DNS-Automation/
├── app.py
├── dns_failover.py
├── traffic_route.py
├── servers.json
├── requirements.txt
└── .github/workflows/
├── deploy-ec2.yml
├── traffic-control.yml
└── dns-failover.yml


---

## Setup

### Requirements
- Python 3.9+
- boto3
- flask
- AWS IAM user with ELB & EC2 permissions

Install dependencies:
```bash
pip install -r requirements.txt

GitHub Secrets
Secret	Description
AWS_ACCESS_KEY_ID	AWS IAM access key
AWS_SECRET_ACCESS_KEY	AWS IAM secret key
EC2_SSHKEY	PEM private key for EC2
servers.json Example
{
  "servers": {
    "DC1": "13.236.134.76",
    "DC2": "13.211.169.112"
  }
}

Usage
Control ALB Traffic Routing
traffic	Description	TG1	TG2
1	100% to TG1	1	0
2	100% to TG2	0	1
3	50/50 split	1	1

Run locally:

export traffic=2
python3 traffic_route.py

Example GitHub Action
name: Update Traffic Routing
on: [workflow_dispatch]

jobs:
  update-traffic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install boto3
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-southeast-2
      - name: Run traffic route
        env:
          traffic: "2"
        run: python3 traffic_route.py

Author

Sahil Siddharth
Cloud & DevOps Engineer
GitHub: @sahilsidd904

License

MIT License © 2025 Sahil Siddharth


---

✅ **Now commit it:**

If on GitHub web UI → just click **“Commit changes”**  
If locally:

```bash
git add README.md
git commit -m "Add full project documentation"
git push origin main


Done!
