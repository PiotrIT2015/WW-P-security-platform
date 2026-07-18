# WW-P Security Platform

## Table of Contents

- [Overview](#overview)
- [Components](#components)
- [Installation](#installation)
- [Running](#running)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Future Development](#future-development)

---

# Overview

**OS-WW-P-1: Security** is a lightweight operating system simulation environment with a graphical desktop interface.

The project combines multiple independent applications focused on:

- cybersecurity,
- information retrieval,
- data analysis,
- network monitoring,
- web technologies,
- automation.

The main goal of the project is to create a unified environment where different research and engineering prototypes can be executed and tested.

---

# Components

## 1. Web Explorer (WhiteDwarf)

**WhiteDwarf** is an advanced search engine project focused on web crawling, indexing, and information retrieval.

The project extends the initial Java prototype created during academic studies. The original version was developed as a proof-of-concept and presented at university and local technology conferences.

The current Python-based implementation focuses on:

- automated web crawling,
- website content analysis,
- search indexing,
- ranking algorithms,
- improved search relevance,
- scalable data processing.

The main purpose of the application is to automatically browse and analyze websites, creating a searchable knowledge base.

---

## 2. PCAAnalyzer

**PCAAnalyzer** is a web-based data analysis application created as part of a master's thesis.

The application allows users to:

- upload multiple datasets,
- analyze large collections of data,
- perform statistical processing,
- visualize results using charts.

Implemented functionality:

- Principal Component Analysis (**PCA**) algorithm,
- asynchronous communication,
- interactive data manipulation,
- visualization of multidimensional datasets.

The system demonstrates practical usage of statistical algorithms in web applications.

---

## 3. NetworkMonitor

**NetworkMonitor** is a network analysis and monitoring tool.

The project idea originated during university studies, where implementing such a solution in Java was one of the planned objectives.

The current version provides a simplified execution environment through a Java `.jar` application.

Main purpose:

- network diagnostics,
- monitoring experiments,
- security-related analysis.

---

# Installation and Running

## Microsoft Windows

### Requirements

- Windows operating system
- Python 3.10+
- XAMPP or equivalent Apache/MySQL environment
- Nmap

---

### Installation Steps

Install Python:

```
**MS Windows**

1. `winget install Python.Python.3.10`(via cmd)
2. add python to PATH
3. `pip install python-nmap` [po użyciu instalatora(plik nmap-setup.exe) z oficialnej strony]
4. configure Apache and MySQL on XAMPP/Cloud
5. double click on `install-require-libraries.bat`
6. double click on `wwp[security].bat`

**Linux**

1. `sudo apt install python3`
2. `sudo apt install nmap`
3. configure Apache and MySQL on XAMPP/Cloud
4. `./install-require-libraries.sh` (via bash)
5. `./wwp-security.sh` (via bash)
	
## Technologies
Project is created with:
* python version: 3.10
...,but project also use:

```

![image alt](https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-1.jpeg?raw=true)

![image alt](https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-2.jpeg?raw=true)

![image alt](https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-3.jpeg?raw=true)

![image alt]( https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-4.jpeg?raw=true )

![image alt]( https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-5.jpeg?raw=true )

![image alt]( https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-6.jpeg?raw=true )

![image alt]( https://github.com/PiotrIT2015/OS-WW-P/blob/master/screenshot-7.jpeg?raw=true )



