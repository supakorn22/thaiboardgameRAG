compose-all:
	docker compose up -d --build

down-compose-all:
	docker compose down

compose-dev-all:
	docker compose -f docker-compose.dev.yml up -d --build

down-compose-dev-all:
	docker compose -f docker-compose.dev.yml down
