# Project Title

Prototype payroll web application that takes uploaded csv files with predefined formats and calculates payroll per employee per pay period.

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

### Installation

A step by step series of examples that tell you how to get a development env running

<b> GIT - Install Git </b>

```bash
#Install git
sudo apt install git
```

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
#Check if user 'srpub' is already added to MySQL database
SELECT user FROM mysql.user;

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
SHOW GRANTS FOR 'srpub'@'localhost';
```

<b> PYTHON - Install/Configure Python </b>

Install the following Python packages

```python
sudo apt-get install python-dev
sudo apt-get install python-pip python-virtualenv
```

Check installed Python version, should say "Python 2.7.1x"

```python
python --version

#Check which version of Python are installed
ls -l /usr/bin/python*

```

NOTE: 
If Python is not installed, then install as follows

```python
sudo apt-get update
sudo apt-get install python3.7
sudo apt-get install software-properties-common

#Use ‘deadsnakes’ PPA to install Python 3.7
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update
sudo apt-get install python3.7

#Verify Python 3.7+ has been installed
python3.7 --version
```

Create a directory called vEnvPython in the home directory & navigate into it.

```python
mkdir ~/projects/py/venv
```

Check Python installation
 
```python
#Check Python installation path (should be: '/usr/bin/python')
which python

#Check Python Virtual Environment installation path (should be: '/usr/bin/virtualenv')
which virtualenv 
```

Create environment variable

```python
Create Python virtual environment - Python 3.7
virtualenv --python=python3.7 venv-py3.7

	OR
		#Alternative method using absolute paths
		virtualenv ~/projects/py/venv/venv-py3.7 --python=/usr/bin/python3.7

	#NOTE: Alternatively, to create Python 2.7 virtual environment
	virtualenv --python=python2.7 venv-py2.7 
```

Activate new python virtual environment

```python
Activate Python 3.7
source ~/projects/py/venv/venv-py3.7/bin/activate

	#NOTE: Alternatively, to activate Python 2.7
	source ~/projects/py/venv/venv-py2.7/bin/activate
```

Check version of pip & update if necessary

```python
#Check version
pip --version

#Update pip
pip install --upgrade pip
```



<b> FLASK - Install/Configure Flask </b>

Install following necessary dependencies

```python
#Python 3.7+
sudo apt-get install python3.7-dev

#Install Flask
pip install -U Flask

pip install mysqlclient

	#NOTE: For Python 2.7.x
	sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev

#Make sure the following dependency is installed successfully (might require 'sudo')
pip install flask-mysqldb
		
#Install using pip
pip install Flask-SQLAlchemy

#Install and update using pip
pip install -U Flask-SQLAlchemy

```

Navigate to project directory
Execute provided 'Requirements.txt' file to install all necessary Python dependancies to run the 'Payroll Report' application 
(NOTE: within activated virtual env)

```python
pip install -r requirements.txt
```

## Usage

```python

```



## Running the tests

Explain how to run the automated tests for this system

To run specific test case classes, execute the relevant unit test class one level above the project package parent directory as follows
ie.
	~/projects/s_git/gitHub/projects/s$ python -m unittest -v payroll.tests.un.classesTC_un.test_tc_payroll


```bash
#To run test suite composed of multiple test classes
python -m unittest -v payroll.tests.un.run_un_ts_main

#To run test case class directly 
python -m unittest -v payroll.tests.un.classesTC_un.test_tc_payroll
```
 
## Deployment

##Troubleshooting

Incomplete termination of previous instance(s) of web app

```python
#Check if multiple processes of the app are active
ps aux | grep "main"

#Kill unwanted instances of web app
kill [process-id]

```

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used


## Authors

* **Sutharsan Rajaratnam** - *Project owner & primary contributor* - [servo00](https://github.com/servo00)


## General Comments 
 - Leverages Bootstrap CSS framework, some custom CSS and Javascript.
 - Uses Python 'unittest' test framework 

 
## Acknowledgments

