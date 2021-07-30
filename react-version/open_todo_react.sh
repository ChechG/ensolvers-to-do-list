#!/bin/bash
cat dump.sql | mysql -hlocalhost -uroot -p
python3 web/render.py