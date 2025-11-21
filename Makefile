.PHONY: build up down test lint

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	pytest

lint:
	flake8
