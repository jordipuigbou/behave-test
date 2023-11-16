APIS_DIR = $(CURDIR)/apis
CRUD_DIR = $(CURDIR)/crud

.PHONY: help
help:	## Show a list of available commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: build-apis
build-apis: ## build apis testing
	docker compose -f $(APIS_DIR)/docker-compose.yml build

.PHONY: run-apis
run-apis: ## run apis testing
	docker compose -f $(APIS_DIR)/docker-compose.yml up

.PHONY: run-apis-coverage
run-apis-coverage: ## run apis coverage
	docker compose -f $(APIS_DIR)/docker-compose.yml build
	docker compose -f $(APIS_DIR)/docker-compose.yml run api bash -c "coverage run  -m pytest --junitxml=/root/_output/reports/junit-apis.xml /root/test.py && coverage xml -o /root/_output/reports/coverage.xml && coverage report"

.PHONY: clean-apis
clean-apis: ## clean apis
	docker compose -f $(APIS_DIR)/docker-compose.yml down

.PHONY: build-crud
build-crud: ## build crud
	docker compose -f $(CRUD_DIR)/docker-compose.yml build

.PHONY: run-crud
run-crud: ## run crud
	docker compose -f $(CRUD_DIR)/docker-compose.yml run backend

.PHONY: run-crud-tests
run-crud-tests: ## run crud tests
	docker compose -f $(CRUD_DIR)/docker-compose.yml down
	docker compose -f $(CRUD_DIR)/docker-compose.yml run test

.PHONY: crud-tests-dry-run
crud-tests-dry-run: ## run crud tests
	docker compose -f $(CRUD_DIR)/docker-compose.yml down
	docker compose -f $(CRUD_DIR)/docker-compose.yml run test bash -c "behave --dry-run"

.PHONY: run-crud-clean
clean-crud: ## build run crud
	docker compose -f $(CRUD_DIR)/docker-compose.yml down