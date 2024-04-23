.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: docker-build
docker-build:	## Build project with compose
	docker-compose build

.PHONY: docker-up
docker-up:	## Run project with compose
	docker-compose up --remove-orphans