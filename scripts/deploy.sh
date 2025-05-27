#!/bin/bash

# Example EC2 deployment script
ssh -o StrictHostKeyChecking=no ec2-user@3.84.115.28 <<EOF
  docker pull myusername/myapp:latest
  docker stop myapp || true
  docker rm myapp || true
  docker run -d --name myapp -p 80:5000 myusername/myapp:latest
EOF
