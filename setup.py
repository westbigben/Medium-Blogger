#!/usr/bin/env python

"""
Setup script for Medium Automation project.
"""

from setuptools import setup, find_packages

setup(
    name="devto-automation",
    version="0.1.0",
    description="Automated Dev.to article creation and publishing system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nitin S Bharadwaj",
    author_email="nitin.satyan@gmail.com",
    url="https://github.com/westbigben/devto-automation",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "aiohttp>=3.9.1",
        "pyyaml>=6.0.1",
        "beautifulsoup4>=4.12.2",
        "python-dotenv>=1.0.0",
        "redis>=5.0.1",
        "asyncio>=3.4.3",
        "perplexity>=0.3.1",
        "medium-api>=0.5.0",
        "selenium>=4.16.0",
        "playwright>=1.40.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-asyncio>=0.23.2",
            "pytest-mock>=3.12.0",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "isort>=5.12.0",
            "pylint>=3.0.2"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "medium-automation=src.pipeline:main"
        ]
    }
)