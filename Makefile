setup:
	pip install -r requirements.txt
	@./manage.py makemigrations core
	@./manage.py migrate
	@./manage.py createsuperuser --username='admin' --email=''
	@./manage.py loaddata fixtures.json
	@echo "Django instalado com sucesso."
	@echo "Rodando a app, favor entrar no site."
	./manage.py runserver