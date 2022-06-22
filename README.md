# CO2 and The Internet: a quantitative study on environmental impact
This repository is a companion page for the following thesis:
> Ivan Ivanov. 2022. CO2 and The Internet: a quantitative study on environmental impact

It contains all the material required for replicating the study, including: Python source code, `.ipynb` files, and gathered data.

## Quick start
Quick Links
---------------

* [Thesis](documentation/thesis.docx)
* [HTTP GET Requests Code](src/get_requester.py)
* [Python Notebook For Managing the Data and Generating Graphs](src/get_requester.py)

### Getting started
To run this, you will need to have Python 3 installed. 
Additionally, you will need to use a `.ipynb` notebook. 
To use it you can either download Anaconda Navigator or use VSCode and the Jupyter Notebook extension for it.

1. Install the needed dependencies. For that you can either use the following command:

```bash
$ python3 -m pip install -r requirements.txt
```
Or install the ones you need manually with:

```bash
$ pip install yourpackagename
```

List of dependencies for the IPYNB:
```
pandas
numpy
matplotlib
pathlib
warnings
re
os
tld
```

List of dependencies for the Python Code:
```
asyncio
aiohttp
csv
asyncio_throttle
```

2. Open the `get_requester.py` and `notebook.ipynb.`

   The python file is strictly used for collecting and parsing `JSON` data. All of the data has already been collected in `/data/csv/`. The notebook is only used for data wrangling and generating graphs.

3. Run the `.py` and `ipynb.`.

   `Py`: Run with either
   ```bash
   $ python3 get_requester.py
   ```
   Or if you're using VSCode with `Ctrl + F5` or the `Run` button in the upper right corner.

   `IPYNB`: Run with either VSCode or Anadonda Navigator.

## Repository Structure
This is the root directory of the repository. The directory is structured as follows:

    bachelor-project
    ├── documentation/
    │   └── thesis.docx # Main thesis deliverable.
    ├── src/
    │   ├── data/
    │   │   ├── csv/ # Contains all of the collected websites in .csv format.
    │   │   │   ├── database0-500.csv
    |   |   |   ...
    │   │   ├── datasets/ # Contains datasets used in the making of this project.
    │   │   │   ├── main.csv
    │   │   │   ├── tables.xlsx
    │   │   │   ├── test_data.csv
    │   │   │   └── top-1m.csv
    │   │   └── images/
    │   │       ├── graphs/ # Contains graphs used in the thesis.
    │   │       └── other/ # Miscelanious images.
    │   ├── charts.ipynb
    │   ├── get_requester.py # Python HTTP GET Requests Code.
    │   └── notebook.ipynb # Notebook used to modify the collected data.
    ├── .gitattributes
    ├── .gitignore
    ├── README.md
    └── requirements.txt