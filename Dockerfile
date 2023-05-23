FROM python:3.8-slim-buster

WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


# sudo docker build -t flask_loan_app . 
# flask_loan_app: name of tag 

# sudo docker images  -- lists all the images available

# sudo docker run -p 8000:5000 -d flask_loan_app
# by default flask runs on 5000 port
# but we are saying run it on 8000 instead of 5000 port


# to list all running containers
# sudo docker container ls

# to detach / stop already running container
# sudo docker stop  name_of_container

# Now we need to put the image to docker hub
# for that signup to docker hub on browser
# then signin to docker hub in terminal
# sudo docker login
# sudo docker build -t 977695/flask_loan_app .
# sudo docker push 977695/flask_loan_app