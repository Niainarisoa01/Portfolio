#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
export $(cat .env.test | xargs)
pytest tests/ -v --cov=app 