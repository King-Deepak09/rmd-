FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY Backend/requirements.txt /app/Backend/requirements.txt
RUN pip install --no-cache-dir -r /app/Backend/requirements.txt

# Copy all project files into the container
COPY . /app

# Set the working directory to Backend to run the application
WORKDIR /app/Backend

# Expose port 5000
EXPOSE 5000

# Run the backend server using gunicorn, binding to 0.0.0.0:5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
