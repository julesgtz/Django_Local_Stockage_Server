@echo off

pip install -r requirements.txt
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set NetworkIP=%%a
start http://%NetworkIP%:8000
python admin/manage.py makemigrations
python admin/manage.py migrate
python admin/manage.py runserver 0.0.0.0:8000
