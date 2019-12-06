from zipfile import ZipFile
import os
from shutil import rmtree
from pathlib import Path
rmtree("Builds", ignore_errors=True)
os.makedirs("Builds")
folder = "Yaru Dark Theme"

with ZipFile(f"Builds/firefox.zip", "w") as zf:
	for file in Path(folder).rglob("*"):
		zf.write(f"{file}", os.path.basename(file))

'''
with ZipFile("Builds/chrome.zip", "w") as zf:
	for file in glob("{folder}/*"):
		zf.write("{file}", os.path.basename(file))
	for icon in os.listdir("{folder}/icons"):  # add icons to archive
		zf.write("{folder}/icons/{icon}", "icons/{icon}")
'''
