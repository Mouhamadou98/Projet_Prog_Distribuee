# Utilisez une image de base avec Python
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt /app/
COPY app.py /app/

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application Flask fonctionnera
EXPOSE 5003

# Commande pour exécuter l'application quand le conteneur démarre
CMD ["python", "app.py"]