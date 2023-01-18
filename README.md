# Chain-rename
PyQt-based app to rename images more efficiently.

## Features
Enter the path of the folder containing the files to rename, then simply rename them one by one. The old name will be displayed alongside the image.
The placeholder.jpg file can be replaced with any other 500x500 image.

## Basic install
Just download the latest build in the releases, depending on your OS.

## Build
To build the app, you will need the following requirements:

### Debian/Ubuntu-based distro
Requirements:
```
sudo apt install python3 python3-pip
```
As well as the python modules:
```
pip install pyside6 cx_freeze
```
Then you can either run the app by running:
```
python3 main.py
```
Or create an executable by running:
```
python3 setup.py build
```
