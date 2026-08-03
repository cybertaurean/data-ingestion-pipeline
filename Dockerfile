# 1. Use a lightweight, headless Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies and install them cleanly
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application source code
COPY src/ ./src/

# 5. Define how the container executes
CMD ["python", "src/app.py"]

