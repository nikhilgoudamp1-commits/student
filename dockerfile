# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Default command to run your script
CMD ["python", "student.py"]