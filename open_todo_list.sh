#!/bin/bash
cat dump.sql | mysql -uroot -p
python3 web/render.py
