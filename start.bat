cd venv1\Scripts
CALL activate.bat
cd..
cd..
pip install -r requirements.txt
cd MyCV
START manage.py runserver
timeout 10
start chrome "http://127.0.0.1:8000/person/1#page-top"
start chrome "http://127.0.0.1:8000/person/2#page-top"
timeout 10