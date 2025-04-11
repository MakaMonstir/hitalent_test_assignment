.PHONY: run up down build migrate test

run:
	docker-compose up --build

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

migrate:
	docker-compose exec api alembic upgrade head

test:
	docker-compose exec api pytest
