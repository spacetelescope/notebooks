#!/usr/bin/env bash

set -e
# Only runs on master
if [ -z "${CIRCLE_PULL_REQUEST}" ]; then
    git config --global user.email devnull@circleci.com
    git config --global user.name CircleCI
    mkdir -p ~/.ssh
    echo 'Host * ' >> ~/.ssh/config
    echo '  StrictHostKeyChecking no' >> ~/.ssh/config
    # Deploy gh-pages
    git clone -b gh-pages --single-branch ${CIRCLE_REPOSITORY_URL} /tmp/out
    cd /tmp/out
    git add .
    git commit -m 'Automated deployment to Github Pages: ${BUILD_TAG}' -a || true
    git push origin gh-pages
    git clean -dfx
fi
exit 0
