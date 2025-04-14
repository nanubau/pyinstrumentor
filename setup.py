from setuptools import setup, find_packages

setup(
    name="pyinstrumentor",
    version="0.1.0",
    description="Automatic instrumentation for Python functions using Prometheus",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "prometheus_client>=0.16.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)