DOCKERFILE="docker/Dockerfile.dev"
GIN_CONFIG_LOC="config/config.gin"
ENV_VAR_FILE="config/env_vars.sh"

source $ENV_VAR_FILE

echo "Using Dockerfile: $DOCKERFILE"
echo "Building locally: $PROJECT_NAME"
echo "Using env vars in: $ENV_VAR_FILE"

docker build -t $PROJECT_NAME \
    -f $DOCKERFILE \
    --build-arg BASE_PATH=$BASE_PATH \
    --build-arg PYTHONPATH=$PYTHONPATH .