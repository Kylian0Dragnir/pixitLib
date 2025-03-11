from setuptools import setup, find_packages

setup(
    name="pixitlib",  
    version="0.1",  
    packages=find_packages(), 
    install_requires=[],  
    author="Mermin Kylian",
    author_email="kylianmermin1@gmail.com",
    description="Une librairie pour se connecter à la console du jeu.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kylian0Dragnir/pixitLib", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)
