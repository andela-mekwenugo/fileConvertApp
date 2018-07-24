set-up:
	pip install -r requirements.txt

xml:
	python converter.py data/hotels.csv --output_file data/test.xml

json:
	python converter.py data/hotels.csv --output_file data/test.json

tests:
	nosetests

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  set-up      installs the dependencies found in requirements.txt"
	@echo "  xml     runs code to create xml file. It saves xml in data/test.xml"
	@echo "  json       Runs code to create xml file. It saves xml in data/test.json"
	@echo "  tests   runs unit tests"
