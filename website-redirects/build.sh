#!/bin/bash

docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

docker build -f Dockerfile -t danesjenovdan-website-redirects:latest .
docker tag danesjenovdan-website-redirects:latest rg.fr-par.scw.cloud/djnd/danesjenovdan-website-redirects:latest
docker push rg.fr-par.scw.cloud/djnd/danesjenovdan-website-redirects:latest
