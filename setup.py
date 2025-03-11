from setuptools import setup, find_packages

setup(
    name="ma_lib",  # Nom de la librairie
    version="0.1",  # Version initiale
    packages=find_packages(),  # Recherche automatiquement les packages dans le dossier
    install_requires=[],  # Dépendances à ajouter si besoin
    author="Mermin Kylian",
    author_email="kylianmermin1@gmail.com",
    description="Une librairie pour se connecter à la console du jeu.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kylian0Dragnir/jeuPixel",  # Remplace par ton URL GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Version minimale de Python requise
)
