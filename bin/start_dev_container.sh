ENV_VAR_FILE="config/env_vars.sh"

source $ENV_VAR_FILE
echo "Using env vars in: $ENV_VAR_FILE"
echo "starting container $PROJECT_NAME"

# for gpu server
docker run -v $PWD:/work \
    -p 8888:8888 -itd $PROJECT_NAME
