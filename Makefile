NAME=app
LABEL=${NAME}
version=$(shell cat version)
PROJECT=rodrigorootrj/worker
TAG=${PROJECT}:app-proc-pepper-juice-${version}

build:
	@docker build . -t ${TAG}
run:build
	docker run -it ${LABEL}
push:build
	docker push ${TAG} 
echo:
	@echo ${TAG}
