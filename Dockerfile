 # our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

#mkdir
RUN mkdir -p /usr/bin/uploads
RUN chmod 775 /usr/bin/uploads

# run the application
CMD ["python", "./hw2.py"]
