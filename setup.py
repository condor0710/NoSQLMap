from setuptools import find_packages, setup


with open("README.md", encoding='utf-8') as f:
	setup(
			name = "NoSQLMap",
			version = "0.7",
			packages = find_packages(),
			scripts = ['nosqlmap.py', 'nsmmongo.py', 'nsmcouch.py', 'nsmscan.py', 'nsmweb.py', 'exception.py'],
			
			entry_points = {
				"console_scripts": [
					"NoSQLMap = nosqlmap:main"
					]
				},
			
			install_requires = [ "CouchDB>=1.2", "httplib2>=0.19.0", "ipcalc>=1.1.3",\
								 "pbkdf2>=1.3", "pymongo>=4.0.0",\
								 "requests>=2.25.0"],
	
			author = "tcstool",
			author_email = "codingo@protonmail.com",
			description = "Automated MongoDB and NoSQL web application exploitation tool",
			license = "GPLv3",
			long_description = f.read(),
			url = "http://www.nosqlmap.net",
			python_requires = ">=3.6"
		)
