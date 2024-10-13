## Day 2

Use the following steps instead (This is for Windows 11)

#### 1. Install the python version of your choice
- Python 3.12 from Windows Installer
&emsp;[**Link to python installer**](https://www.python.org/downloads/windows/)
- Then install this version of python under a custom path
```python
   "C:\Python\Python3.12"
```
- Install without checking the ADD TO PATH option. If you check this everytime all the python versions installed will be added to PATH and this will cause a mess.

#### 2. Setup virtualenv
- Go to VScode and add terminal from **View -> Terminal**
- Now cd to the path where you have created the folder for python project
```python
   cd "C:\Users\Pranjal Verlekar\Documents\VisualStudioCode\PythonProjects\PyMotivator"
```
- Install virtualenv using the below command
```python
   C:\Python\Python3.12\Scripts\pip3.exe install virtualenv
```
**Note**: Don't include quotes in the pip3.exe path as it failed with quotes for the first time
This will install the virtualenv utility under **C:\Python\Python3.12\Scripts** in this case
	
#### 3. Create virtualenv with the name env
- Use the below command to install virtualenv called "env" under the python project:**"C:\Users\Pranjal Verlekar\Documents\VisualStudioCode\PythonProjects\PyMotivator"**
```python
   C:\Python\Python3.12\Scripts\virtualenv.exe -p python3.12 env
```
-  Once this gets installed, now you can see some folders and scripts under **"C:\Users\Pranjal Verlekar\Documents\VisualStudioCode\PythonProjects\PyMotivator"** folder	

#### 4. Activate the virtualenv
- In order to activate the virtualenv go to the root of the project if you are not there
```python
   cd "C:\Users\Pranjal Verlekar\Documents\VisualStudioCode\PythonProjects\PyMotivator"
```
- Instead of using source command which doesn't work in Windows for some reason, you need to cd to the scripts folder and just the activate file directly to activate the virtualenv
```python
   cd .\env\scripts
   .\activate
```
The command prompt will switch to (env) before the start of path indicating that it is using the newly activated virtualenv
- Check whether the python version is as desired by using the below command
```python
   (env) PS C:\Users\Pranjal Verlekar\Documents\VisualStudioCode\PythonProjects\PyMotivator\env\Scripts> python --version
   Python 3.12.6
```

#### 5. Exit the virtualenv
- In order to deactivate the virtualenv and exit it completely, use the keyword deactivate instead of executing the deactivate.bat file
```python	
   deactivate
```
