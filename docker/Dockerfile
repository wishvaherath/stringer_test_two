FROM continuumio/miniconda

# Install conda libs
RUN apt-get update && apt-get install -y build-essential

# Make the input/output directories
RUN mkdir -p /app/in /app/out

# add the execution script
WORKDIR /app
COPY power.py .
RUN ["chmod", "+x", "./power.py"]

ENTRYPOINT ["./power.py"]
