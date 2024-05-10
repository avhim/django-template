#!/bin/sh

until cd /app/src
do
    echo "Waiting for server volume..."
done

celery -A chargik worker --loglevel=info --concurrency 1 -E