FROM python:3.13-slim

WORKDIR /app
COPY . .

# Copy all project files
COPY . /app

# Default command to run your script
CMD ["python", "student.py"]