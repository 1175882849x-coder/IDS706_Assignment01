# IDS706_Assignment01

[![Python tests](https://github.com/1175882849x-coder/IDS706_Assignment01/actions/workflows/test.yml/badge.svg)](https://github.com/1175882849x-coder/IDS706_Assignment01/actions/workflows/test.yml)

## Project Description

This project is a simple Python application for practicing a basic data engineering development workflow. It uses Python, pytest, Make, Docker, and GitHub Actions.

## Main Function

The welcome_message(name) function takes a name as input and returns a welcome message for the Data Engineering course.

## Installation

Install the required dependencies:

make install
## Run the Application

Run the application:

make run

The program will ask the user to enter a name.

Example:

Enter your name: Tom
Tom, welcome to the Data Engineering course.
## Run Tests

Run tests locally:

make test

Run tests inside Docker:

make docker-test
## Docker

Build the Docker image:

make docker-build

Run the application inside Docker:

make docker-run
## Notes

GitHub Actions is configured to automatically run the tests and build the Docker image when changes are pushed to the repository.