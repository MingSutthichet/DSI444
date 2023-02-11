#Dockerfile
#from python image
FROM python:3.7-alpine

#make a new directory
RUN mkdir /app
#copy code app.py and requirements.txt from current directory in host to /app in container
COPY app.py /app
COPY requirements.txt /app
#container change working directory to /app
WORKDIR /app

#install python model in requiremts.txt
RUN pip install -r requirements.txt
#allow network interface of container port 5000 to connect to the host network
EXPOSE 5000

#start the main process in container
CMD ["python","app.py"]