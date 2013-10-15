use "python compile_cx.py build" to build exe

use "python setup.py" to setup shortcut in right click menu

may need to change path in setup.py to point to the run.exe file in build folder just created by the first step 

need to create secret_setting.py in the top folder with:
gmail_account = '....'
gmail_password = '...'
default_reciever = '...'

will make the first step and third step automatic in the next version

this project needs the following modules: cx_Freeze 

