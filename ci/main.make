main:
	
# npm install watch-cli -g
# watch:
# 	watch -p 'src/**/*' -c 'make stop run-srv'
ver:
	docker run --rm -it -v `pwd`/.env:/src/.env $(REG)/ci/gulp:$(GULP) ver
.PHONY: ci
ci rt:
	time docker-compose build $@
down logs ps restart create:
	docker-compose $@
push pull:
	docker-compose $@ ci rt
log:
	docker-compose logs -f ci

R=docker-compose run --rm
run-rt:
	$R rt
run-ci:
	$R ci
run-c:
	docker run --runtime=nvidia --rm -it \
	-e CUDA_VISIBLE__DEVICES=-1 \
	--env-file = `pwd`/.env \
	-v `pwd`/src:/srv \
    -v `pwd`/test:/s \
    -v /mnt/datasets/sound/models:/models \
	--label "traefik.enable=true" \
	--label "traefik.frontend.rule=PathPrefixStrip:/$(SRV)/$(RT)/,/$(SRV)/,/m2/$(SRV)/,/master/$(SRV)/,/api/audio/,/mfc/api/audio/" \
	$(REG)/ci/$(SRV):$(CI)

run-sh:
	docker-compose run --rm ci bash
up:
	docker-compose up -d --force-recreate ci

ID=`docker-compose ps -q`
sh:
	docker exec -it $(ID) bash
diff:
	docker diff $(ID)