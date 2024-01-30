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
11. [IDE](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Integrated-Development-Environment-(IDE))
12. [Test Cases](https://github.com/ihemanthkarthik/MoneyTracker/blob/Master/README.md#Test-Cases)


# Prerequisites
The below the following programs has to be installed in order to use the application.
1. **[Python](https://www.python.org/)** - The application is developed and designed completely in Python.
2. **[SQL Lite](https://pypi.org/project/pysqlite3/)** - Relational Database in python used for storing data (module to be installed in python)

# Git Repository
The Git Repository is used for version control and cloud storage medium for application

**[GIT](https://github.com/ihemanthkarthik/MoneyTracker/blob/30ad2d3b4b54fe8c2696a948e18721880de1b115/)**

# Requirement-Engineering
I have used Jira and Trello for User Story Development and Task Management. Please find below the links for the same

**[JIRA](https://hemanthkarthikeyan.atlassian.net/jira/software/projects/MNYTRKR/boards/2/timeline)** - Used for creating user stories and tasks with requirements for developers

**[JIRA Board Screenshot](https://github.com/ihemanthkarthik/MoneyTracker/blob/f4e96d2517aa1cb38304ad67a14c57f708e18956/Jira%20Board.png)** 

**[Trello](https://trello.com/invite/b/XJw5llFB/ATTIa77460d9d92550be9044c4e82d5a9b8e713D89F9/moneytracker)**

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

![PyBuilder - Build Success.png](PyBuilder%20-%20Build%20Success.png)

# Functional Programming
My Code functionality is not based on the functional programming, but I have added an example of login functionality implementing the functional programming.

1. **[Only Final Data Structures](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L9)**
2. **[Side-Effect-Free Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L66)**
3. **[Use of Higher Order Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L12)**
4. **[Functions as parameters and return values](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L15)**
5. **[Usage of Closures / Anonymous Functions](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py#L29)**

**[Functional Programming File](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/funct_programming.py)**

# Clean Code Development

1. **[Modular Structure](https://github.com/ihemanthkarthik/MoneyTracker/blob/bc8ca2606e1ac479f47b5a2575682b1620aa54b0/src/main/python/connection.py)**
2. **[Descriptive Naming](https://github.com/ihemanthkarthik/MoneyTracker/blob/bc8ca2606e1ac479f47b5a2575682b1620aa54b0/src/main/python/controller.py#L111)**
3. **[Separation of Concerns](https://github.com/ihemanthkarthik/MoneyTracker/blob/bc8ca2606e1ac479f47b5a2575682b1620aa54b0/src/main/python/authentication.py)**
4. **[Consistent Formatting](https://github.com/ihemanthkarthik/MoneyTracker/blob/7dda87a03e65dcc9ff7b3c64cab89b3bdca318cc/src/main/python/bankintegrations.py)**
5. **[Comments for Clarity](https://github.com/ihemanthkarthik/MoneyTracker/blob/bc8ca2606e1ac479f47b5a2575682b1620aa54b0/src/main/python/controller.py#L17)**

**[Clean Code Developement - Cheat Sheet](https://github.com/ihemanthkarthik/MoneyTracker/blob/b6b8fad8af12495e325dfd94b7b57a68898c1462/CCD%20-%20Cheat%20Sheet.pdf)**

# Integrated Development Environment (IDE)
I used Pycharm for developing this application. I frequently use the below shortcuts when coding in Pycharm

1. Ctrl + /     -> Add/remove line or block comment
2. Alt + F7     -> Find Usages
3. Ctrl + F     -> Find
4. Ctrl + R     -> Replace
5. Shift + F6   -> Refactoring Rename

# Test Cases
![Test Cases.png](Test%20Cases.png)

**[Unit Testcase](https://github.com/ihemanthkarthik/MoneyTracker/blob/5f3e66ce3e858c518546623f8339c89ca24e4d1a/src/unittest/python/authentication_tests.py)**

