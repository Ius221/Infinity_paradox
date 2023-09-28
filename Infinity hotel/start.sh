#! /usr/bin/bash
if ! pgrep -x mongod > /dev/null
then
	sudo systemctl start mongod.service
	python3 inf_hotel/manage.py runserver
else
	python3 inf_hotel/manage.py runserver
fi
