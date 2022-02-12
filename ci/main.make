main:

.PHONY: ci
ci rt:
	docker-compose build $@
down logs ps restart create:
	docker-compose $@
push pull:
	docker-compose $@ ci rt
log:
	docker-compose logs -f ci
log-rt:
	docker-compose logs -f rt

R=docker-compose run --rm
run-rt:
	$R rt
run-ci:
	$R ci

run-sh:
	docker-compose run --rm ci bash
up:
	docker-compose up -d --force-recreate ci
up-rt:
	docker-compose up -d --force-recreate rt