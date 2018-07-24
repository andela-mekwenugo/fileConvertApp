# File Converter

A Python tool that reads and converts data from a csv file and writes it's data into an xml or json file.

## Getting Started

### Installing Dependencies
Ensure that you can install python packages using pip.

```
$ pip install -r requirements.txt
```

## Running The Script

### Program Arguments
The following arguments can be specified when running the program on the terminal. The arguments that have required as True are compulsory.

|Args               |Notation                |Desc                          |Required|
|-------------------|------------------------|------------------------------|--------|
|inputFile          |  (Positional Argument) |The csv file to be read       |True    |
|delimiter          |`-d` `--delimiter`      |The delimiter used in the CSV |False   |
|output File        |`-o` `--output_file`    |The file to be written into   |True    |
|sort               |`-s` `--sort`           |Sort key to sort data         |False   |


### Program Command
The hotels.csv file is located inside the data folder.

To Convert the csv file into a json file, enter the following on your terminal. Substitute `test.json` for the name of your json output file.
```
$ python converter.py data/hotels.csv --output_file test.json -s stars
```

The above command will read the hotels.csv file, convert it to json, sort it's output by stars and write the sorted data into a file called test.json.


## Running the tests

```
$ nosetests
```

OR

```
python test.py
```

## Using the Make command to run program
I have created shorts cuts in the Makefile that will do all of the above with make commands

|Make commands    |What they do    |
|-----------------|----------------|
|$ make set-up    |Installs all packages in the requirements.txt file|
|$ make xml       |Converts hotels.csv to an xml file, data/test.xml|
|$ make json      |Converts hotels.csv to a json file, data/test.json|
|$ make tests     |Runs unit tests|
|$ make help      |List the various make commands and what they do|

## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-365/)

## Author

* **Mirabel Ekwenugo** - [Github](https://github.com/andela-mekwenugo) [LinkedIn](https://linkedin.com/in/mirabelekwenugo) [Email](mailto:mirabelkoso@gmail.com)

