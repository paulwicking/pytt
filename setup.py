from setuptools import find_packages, setup

with open("README.rst", "r") as in_file:
    long_description = in_file.read()

setup(
    name='pytt',
    version='2018.6.1.alpha2',
    packages=find_packages(),
    url='https://www.trainingtracker.io/',
    license='MIT',
    author='Paul Wicking',
    author_email='paulwicking@gmail.com',
    description='Py Training Tracker - Track your training progress.',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
