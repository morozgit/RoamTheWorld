#!/bin/bash
set -e

docker compose up --build -d
echo "Deployment completed successfully"
