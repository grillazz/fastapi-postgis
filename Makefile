.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: docker-build
docker-build:	## Build project with compose
	docker compose build

.PHONY: docker-up
docker-up:	## Run project with compose
	docker compose up --remove-orphans

.PHONY: docker-alembic-create
docker-alembic-create:  ## Create new alembic database migration aka database revision.
	docker compose up -d db | true
	docker compose run --no-deps app alembic revision --autogenerate -m "$(msg)"

.PHONY: docker-alembic-migrate
docker-alembic-migrate: ## apply alembic migrations to database/schema
	docker compose run --rm app alembic upgrade head

.PHONY: docker-clean
docker-clean: ## Clean Reset project containers and volumes with compose
	docker compose down -v --remove-orphans | true
	docker compose rm -f | true
	docker volume rm postgis_data | true

.PHONY: docker-test
docker-test: ## Run tests with compose
	#docker compose run --rm app pytest --inline-snapshot=fix
	#docker compose run --rm app pytest -vv
	docker compose run --rm app pytest