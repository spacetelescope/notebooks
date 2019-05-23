#!/bin/bash

# vars for this script:
# REPO_URL - repo url to clone from (https or ssh)
# DEPLOY_BRANCH - branch to deploy to (normally gh-pages)
# WORKSPACE - where to copy files from to add to deploy commit (build location)
# BUILD_TAG - tag for deploy commit
# REMOTE_NAME - remote to push up to
# These can be set by using "export var=value" for manual deploy
# Or they are set in environment vars when used on CI

# set some defaults for the environment variables
if [[ -z "${REPO_URL}" ]]; then
  REPO_URL="."
else
  REPO_URL="${REPO_URL}"
fi
if [[ -z "${DEPLOY_BRANCH}" ]]; then
  DEPLOY_BRANCH="gh-pages"
else
  DEPLOY_BRANCH="${DEPLOY_BRANCH}"
fi
if [[ -z "${WORKSPACE}" ]]; then
  WORKSPACE="$PWD"
else
  WORKSPACE="${WORKSPACE}"
fi
if [[ -z "${BUILD_TAG}" ]]; then
  BUILD_TAG="manual build"
else
  BUILD_TAG="${BUILD_TAG}"
fi
if [[ -z "${REMOTE_NAME}" ]]; then
  REMOTE_NAME="origin"
else
  REMOTE_NAME="${REMOTE_NAME}"
fi

git clone -b ${DEPLOY_BRANCH} --single-branch ${REPO_URL} /out

cd /out

cp -aR ${WORKSPACE}/* .

git add .
git commit -m "Automated deployment to GitHub Pages: ${BUILD_TAG}" --allow-empty
git push $REMOTE_NAME $DEPLOY_BRANCH
git clean -dfx
