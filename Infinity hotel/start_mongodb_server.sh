#! /usr/bin/bash
sudo systemctl start mongod.service
mongosh
python3 inf_hotel/manage.py runserver > konsole
