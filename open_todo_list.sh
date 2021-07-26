#!/bin/bash
cat dump.sql | mysql -hlocalhost -uroot -proot
python3 web/render.py
