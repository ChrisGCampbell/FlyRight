#!/usr/bin/env bash
rsync -avz /Users/samcrane/Documents/GitLab/Icarus/webapp/icarus-web-app -e "ssh -i ../7305Key.pem" ubuntu@icarusmap.com:/home/ubuntu/ --exclude icarus-web-app/node_modules/ --exclude icarus-web-app/src/