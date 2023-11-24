#!/bin/bash

python3 -m venv my_venv
source my_venv/bin/activate
pip install pandas psycopg2-binary sqlalchemy
python3 create_data.py
