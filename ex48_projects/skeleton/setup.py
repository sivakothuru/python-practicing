try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "SivaReddy",
    "url":"URL to het it at",
    "Download_url": "where to download it",
    "author_email": "siva@agiliq.com",
    "version": "0.1",
    "install_requires": ["nose"],  
    "packages": ["NAME"], 
    "scripts": [],
    "name": "projectname"    
}

setup(**config)
