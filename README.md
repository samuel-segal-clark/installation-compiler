Run
pip install -r requirements.txt
to install the dependencies necessary for the project.

Remember to have the install subdirectory for the files in order for the program
to work properly

Specify the target requirements in .\files\install\requirements.txt
Specify the Python install URL in .\files\install\config.ini
Note that these files must be present relative to the compiled exe during runtime

Build the project by either running the build.bat file,
or by running:
pyinstaller --onefile 