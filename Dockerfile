# Gebruik een basisimage met TensorFlow en Python
FROM tensorflow/tensorflow:2.3.0

# Werkdirectory instellen
WORKDIR /app

# Installeer benodigde Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer je trainingscode naar de container
COPY train_model.py .

# Commando om je model te trainen
CMD ["python", "train_model.py"]
