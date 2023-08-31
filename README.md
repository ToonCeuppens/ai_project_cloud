# ai_project_cloud
# bouw de docker image
docker build -t my_training_image .
# lijst van images
docker images

# start docker container
docker run my_training_image

#testen

docker build -t my_inference_image -f DockerfileTest .

docker run my-inference_image
