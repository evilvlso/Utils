def chrome():
	run('apt-get update',warn_only=True)
	run('apt-get install -y libxss1 libappindicator1 libindicator7',warn_only=True)
	run('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',warn_only=True)
	result=run('dpkg -i  google-chrome-stable_current_amd64.deb',warn_only=True)
	print(red('直接安装chrome失败'))
	if result.failed:
		run('apt-get install -y -f ')
		print(green('强安chrome ok'))
