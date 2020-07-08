#!/usr/bin/env python3
from zipfile import ZipFile
import os
from shutil import rmtree

rmtree("Builds", ignore_errors=True)
os.makedirs("Builds")

file = "manifest.json"
with ZipFile("Builds/firefox.zip", "w") as zf:
	zf.write(f"{file}", os.path.basename(file))

'''
with ZipFile("Builds/chrome.zip", "w") as zf:
	for file in glob("{folder}/*"):
		zf.write("{file}", os.path.basename(file))
	for icon in os.listdir("{folder}/icons"):  # add icons to archive
		zf.write("{folder}/icons/{icon}", "icons/{icon}")
'''
