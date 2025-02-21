from setuptools import setup, find_packages

setup(
    name="kd-poke-sdk",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.32.3",
    ],
    python_requires=">=3.11",
    author="Ken Delsere",
    author_email="kenneth.delsere@gmail.com",
    description="A Python SDK for the Pokemon API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kendelsere/se-poke-api",
    classifiers=[
        "Development Status :: 1.0",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
) 