# Use Python 3.11.4 as base image
FROM python:3.11.9

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY Code /app

# Expose the default Streamlit port
EXPOSE 8502

# Run the Streamlit app
CMD ["python", "-m", "streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]

