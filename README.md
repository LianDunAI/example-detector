Example of serving the detectors using HTTP APIs.

# Develop

Install requirements:

    pip install -r requirements.txt

Run the service:

    flask run --host=0.0.0.0 --port 8088


# Deploy

Build and save docker image:

    sudo docker build . -t detector-serve:latest
    sudo docker save -o detector-serve-latest.tar detector-serve:latest

Run (after the image is loaded):

    # sudo docker load -i detector-serve-latest.tar
    sudo docker run -p 8088:8088 --gpus all -d detector-serve:latest
