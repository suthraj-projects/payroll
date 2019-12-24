# Project Title

Simple payroll web application that takes uploaded csv files with predefined formats and calculates payroll per employee per pay period.

## Getting Started


### Prerequisites

Application built and tested in the following environments
* LINUX Ubuntu ( 16.04 / 18.04 )
* Tested with Python versions 2.7.12 / 2.7.15+
* Built using Flask

Update Linux (Ubuntu)

```bash
sudo apt-get update        
sudo apt-get upgrade       
sudo apt-get dist-upgrade  
```

Install git

```bash
sudo apt install git
```

### Installation

A step by step series of examples that tell you how to get a development env running


<b> DATABASE - Install/Configure MySQL </b>

Install MySQL

```bash
sudo apt-get install mysql-server
```

Login into MySQL

```bash
sudo mysql -p -u root
```

Create following database

```mysql
CREATE DATABASE  payroll;
```

Check if new 'payroll' database has been created

```mysql
SHOW DATABASES;
```

Add following db user access to new database

```mysql
CREATE USER 'srpub'@'localhost' IDENTIFIED BY 'mysql111';
GRANT ALL PRIVILEGES ON payroll.* TO 'srpub'@'localhost';
```

NOTE: If you get password 'current policy requirements' violation error, lower the password policy to 'LOW' as follows:

```mysql
SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password_policy=LOW;
```


Double check new user <i> suthraj </i> has access to <i> payroll </i> database

```mysql
SHOW GRANTS FOR '<user_name>'@'localhost';
```

## Usage

```python

```



## Running the tests

Explain how to run the automated tests for this system
 
## Deployment

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used


## Authors

* **Sutharsan Rajaratnam** - *Project owner & primary contributor* - [servo00](https://github.com/servo00)


## General Comments 
 - Leverages Bootstrap CSS framework, some custom CSS and Javascript.
 - Uses Python 'unittest' test framework 

 
## Acknowledgments

