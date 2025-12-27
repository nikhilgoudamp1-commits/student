FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install pytest

# Run main program first, then run all test cases
CMD python student.py && pytest -s
