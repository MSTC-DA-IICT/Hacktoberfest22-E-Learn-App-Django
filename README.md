# Hacktoberfest22-E-Learn-App-Django
E-learning application in Django.  
This application aims to develop a platform wherein teacher can put up interactive quizes and polls for their students.   

## Installation and Getting Started:

#### Download the setup file of an IDE of your choice and install it on your machine. Recommended:  
Visual Studio Code (by Microsoft) - [LINK](https://code.visualstudio.com/download)  
PyCharm (by Jetbrains) - [LINK](https://www.jetbrains.com/pycharm/download/#section=windows)  

#### Download and install the latest version of Python from this [LINK](https://www.python.org/downloads/).  
Don’t forget to check the option which says **“Add Python to PATH”** in the installation wizard.

#### Open the folder in your IDE, wherein you want to build the project.  

#### Upgrade pip to the latest version using the command -
```py -m pip install --upgrade pip```

#### Set up a virtual environment (venv) by using the command -
```py -m venv <name_for_your_virtual_environment>```

#### Activate the venv using the command -
```.\<name_of_your_virtual_environment>\Scripts\activate```  
It’s a good practice to develop a project in a venv because it enables you to install all the project-specific packages locally.  
Use the command deactivate to deactivate the virtual environment.

#### Install Django on your machine using the command -
```pip install django```

#### Run the following command in terminal to clone the Repository in your local machine  
`git clone https://github.com/MSTC-DA-IICT/Hacktoberfest22-E-Learn-App-Django.git`  

#### Head to the project directory using the command -
```cd <name_of_your_project>```

Start the local server on your machine by using the command -
```py manage.py runserver```

These should be the last two lines displayed in your terminal -  
Starting development server at http://127.0.0.1:8000/  
Quit the server with CTRL-BREAK.  

##### If the above lines show up, you're ready to develop!


### File Structure:
ELearnApp, Teacher and Student are three different apps created to fulfill the functionality.  
ELearn is the main app which contains settings.py and urls.py for the project.  


