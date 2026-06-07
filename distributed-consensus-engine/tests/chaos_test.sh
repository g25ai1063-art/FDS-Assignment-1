#!/bin/bash

echo "Stopping node3"

docker stop node3

sleep 15

echo "Starting node3"

docker start node3

echo "Chaos test complete"
