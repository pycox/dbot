#build

pip install pyinstaller
pyinstaller --onefile your_script.py
pyinstaller --onefile --icon=icon.ico --noconsole run.py
