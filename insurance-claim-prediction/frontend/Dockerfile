FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Streamlit app
COPY streamlit_app.py .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD [ "streamlit","run","streamlit_app.py","--server.address=0.0.0.0","--server.port=8501"]
