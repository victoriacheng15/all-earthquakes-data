.PHONY: init format csv db exec

init:
	python3 -m venv env
	env/bin/activate
	pip install -r requirements.txt

format:
	black main.py utils

csv:
	python3 main.py csv

db:
	python3 main.py db

exec:
	docker exec -it earthquakes-postgres psql -U postgres