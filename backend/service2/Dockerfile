# Utilisez une image de base légère de Python
FROM python:3.8-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY app.py .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application Flask s'exécute
EXPOSE 5004

# Commande pour exécuter l'application
CMD ["python", "app.py"]
