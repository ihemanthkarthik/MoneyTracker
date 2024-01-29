# MoneyTracker
![logo-light.png](images%2Flogo-light.png)

A simple application that will help you in keeping track on your credits and expenses daily, as well as providing in each expense category. This app will record credits and daily expenses in each category that the user inputs every day and will provide an overview of their spends in each category in the form of a pie chart.

# Table Of Content
1. [Prerequisites](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Prerequisites)
2. [Git Repository](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/)
3. [Requirements Engineering](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Requirement-Engineering)
4. [Project Analysis](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Project-Analysis)
5. [Domain-Driven-Design](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Domain-Driven-Design(DDD))
6. [Unified-Modelling-Language](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Unified-Modelling-Language(UML))
7. [Metrics](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Metrics)
8. [Build Management](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Build-Management)
9. [Functional Programming](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Functional-Programming)
10. [Clean Code Development](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Clean-Code-Development)
11. 


# Prerequisites
The below the following programs has to be installed in order to use the application.
1. **[Python](https://www.python.org/)** - The application is developed and designed completely in Python.
2. **[SQL Lite](https://pypi.org/project/pysqlite3/)** - Relational Database in python used for storing data (module to be installed in python)

# Git Repository
The Git Repository is used for version control and cloud storage medium for application

**[GIT](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/)**

# Requirement-Engineering
Understanding the requirements for building a software/application is the crucial part of being a software developer. It establishes a solid foundation for the development team to understand the business needs and expectation of users for the application to be built or developed.

**[JIRA](https://hemanthkarthikeyan.atlassian.net/jira/software/projects/MNYTRKR/boards/2/timeline)** - Used for creating user stories and tasks with requirements for developers

# Project Analysis

**[Analysis Document](https://github.com/ihemanthkarthik/MoneyTracker/blob/98d65a0ed3e93fe42b23130cbc4dd856d409171e/Analysis.pdf)**

# Domain-Driven-Design(DDD)

**[Domain-Driven-Design Document](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/DomainDrivenDesign%20Document.pdf)**

# Unified-Modelling-Language(UML)
Unified Modelling Language is a visual representation of how the software/application works. It helps users understand the workflow of the system both in technical and non-technical terms.

**[Database Objects Diagram](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/UML/DB%20Objects.png)**
**[Activity Diagram](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/UML/Activity%20Diagram.png)**
**[Class Diagram](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/UML/Class%20Diagram.png)**
**[Use Case Diagram](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/UML/Use%20Case%20Diagram.png)**

# Metrics
Sonar Cloud is used to analyze the project and code versatility and readability.

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=ihemanthkarthik_MoneyTracker&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=ihemanthkarthik_MoneyTracker)

Screenshot Reference for the Badge if the above link expires
![img.png](img.png)

# Build Management
Pybuilder is being used as build automation tool in this project.

![img.png](img.png)

# Functional Programming
My Code functionality is not based on the functional programming, but I have added an example of login functionality implementing the functional programming.

1. **[Only Final Data Structures](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L9)**
2. **[Side-Effect-Free Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L66)**
3. **[Use of Higher Order Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L12)**
4. **[Functions as parameters and return values](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L15)**
5. **[Usage of Closures / Anonymous Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L29)**

**[Functional Programming File](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py)**

# Clean Code Development

1. **[Modular Structure](https://github.com/ihemanthkarthik/MNYTRKR/blob/997960f3d891f462d400b1e7e7cd2ce9a58afbd4/src/connection.py)**
2. **[Descriptive Naming](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/python/controller.py#L111)**
3. **[Separation of Concerns](https://github.com/ihemanthkarthik/MNYTRKR/blob/997960f3d891f462d400b1e7e7cd2ce9a58afbd4/src/authentication.py)**
4. **[Consistent Formatting](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/python/bankintegrations.py)**
5. **[Comments for Clarity](https://github.com/ihemanthkarthik/MNYTRKR/blob/997960f3d891f462d400b1e7e7cd2ce9a58afbd4/src/controller.py#L17)**

**[Clean Code Developement - Cheat Sheet](https://github.com/ihemanthkarthik/MNYTRKR/blob/997960f3d891f462d400b1e7e7cd2ce9a58afbd4/src/controller.py#L17)**