FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "bash", "run_airflow.sh" ]