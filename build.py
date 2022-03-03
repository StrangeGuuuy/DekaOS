#!/usr/bin/env python3
if __name__ == '__main__':
	import os
	from tkinter import messagebox


	def windows() -> None:
		os.system(CMD_BUILD)
		os.system('rmdir /s /q build __pycache__')
		messagebox.showinfo('Congratulate!', 'Now you are able to start playing this game in case you choice it!')


	def linux_and_mac_osx() -> None:
		from subprocess import call
		call(CMD_BUILD)
		call('rm -rf build __pycache__')
		messagebox.showinfo('Congratulate!', 'Now you are able to start playing this game in case you choice it!')


	CMD_BUILD = '''pyinstaller -F -n butterfly_effect -I imgs/project_icon.png src/main.py'''
	if os.name == 'nt':
		windows()
	else:
		linux_and_mac_osx()
