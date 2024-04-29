#build

pip install pyinstaller
pyinstaller --onefile your_script.py
pyinstaller --onefile --icon=your_icon.ico --noconsole your_script.py