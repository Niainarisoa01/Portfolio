@echo off
set "PYTHONPATH=%PYTHONPATH%;%CD%"
pytest tests/ -v --cov=app 