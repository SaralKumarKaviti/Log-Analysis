# Log-Analysis
### By Saral Kumar Kaviti

Logs Analysis Project, Part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is

A Reporting page that prints out reports in a plain text format based on the data in the database

## What it does

This reporting tool is python program using the `psycopg2` moudle to connect to the database.

## Software Requirements

* Python3
* VirtualBox
* Vagrant
* Git
* PostgreSQL
* Text Editor(Sublime text)

## Project Contents

In this project consists for following files:

* logs.py - It is a main file to run Logs Analysis Reporting Tool

* log_output.txt - It is a output file that will shown on the git bash

* README.md - It is an Instructions to install this reporting tool

## Installation

There are some urls and a few instructions on how to run the project

## URL's

- [Git](https://git-scm.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/)
- [Vagrantfile](https://https://github.com/udacity/fullstack-nanodegree-vm)
- [Sublime Text](https://www.sublimetext.com/3)

## Installation Process

* Install Git, Sublime text, VirtualBox and Vagrant
* Clone the Udacity Vagrantfile
* Goto Vagrant dictory and download the zip file and place here 
* Open terminal or git
* Launch the Vagrant VM(`vagrant up`)
* Run Vagrant VM(`vagrant ssh`)
* Now change the directory into vagrant folder i.e., `cd /vagrant`

## How to Run Project

Download the project zip file and unzip the file now copy unzip file inside `vagrant/log-analysis`

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command.

```
$ vagrant up
```
2. Now log into vagrant using below command

```
$ vagrant ssh
```


