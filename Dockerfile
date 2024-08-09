#Mention base image

FROM us-ashburn-1.ocir.io/idrues0zhwlo/us-ashburn-1-dop-1-ocir-1/python:3.8-bookworm

#Copy the current folder structure and content to docker container file system folder

COPY  .  /usr/ML/app

# Expose the port within docker container
EXPOSE 8501

# Set current working directory
WORKDIR /usr/ML/app

# Install the required libraries
RUN pip install -r  requirements.txt

# within the container the application startup command 
CMD streamlit run appRequest.py


