# Use a base image of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies directly using pip
RUN pip install --no-cache-dir requests rich

# Define the entrypoint to execute the script with arguments
ENTRYPOINT ["python3", "/app/tool.py"]

# Optional CMD to provide default parameters (like -h)
CMD ["-h"]
