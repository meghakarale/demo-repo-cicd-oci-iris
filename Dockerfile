#Mention base image

FROM continuumio/anaconda3:2022.05

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


