@echo off

pip install -r requirements.txt
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| findstr /C:"Adresse IPv4"') do set "ip=%%i"
set ip=%ip:~1%
python3 admin/manage.py runserver 0.0.0.0:8000
start http://%ip%:8000