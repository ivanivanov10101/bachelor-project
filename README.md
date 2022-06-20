# bachelor-project
 
This is a repository hosting code for my BSc Computer Science Project.

It contains an ASYNC implementations for HTTP GET requests and a multi-file JSON to CSV converter.

## Instructions:
Simply run the async_alternate.py with a .csv that contains a single column with every row being a website.

The script will do a HTTP 'GET' request to the API and awat a .json file which will be appended to a .csv file.

The csv file is stored in the /csv folder.

The data is then managed by CSV.ipynb

# CO2 and websites: a quantitative study on environmental impact.
This repository is a companion page for the following thesis:
> Ivan Ivanov. 2022. CO2 and websites: a quantitative study on environmental impact.

It contains all the material required for replicating the study, including: the source code, ipynb files, and gathered data.

## Quick start
Here a documentation on how to use the replication material should be provided.

### Getting started

1. Provide step-by-step instruction on how to use this repository, including requirements, and installation / script execution steps.

2. Code snippets should be formatted as follows.
   - `git clone https://github.com/S2-group/template-replication-package`

3. Links to specific folders / files of the repository can be linked in Markdown, for example this is a link to the [src](src/) folder.

## Repository Structure
This is the root directory of the repository. The directory is structured as follows:

    template-replication-package
     .
     |
     |--- src/                             Source code used in the thesis / paper
     |
     |--- documentation/                   Further structured documentation of the replication package content
     |
     |--- data/                            Data used in the thesis / paper 
            |
            |--- additional_subfolder/     Subfolders should be further nested to increase readability                 
  

Usually, replication packages should include:
* a [src](src/) folder, containing the entirety of the source code used in the study,
* a [data](data/) folder, containing the raw, intermediate, and final data of the study
* if needed, a [documentation](documentation/) folder, where additional information w.r.t. this README is provided. 

In addition, the replication package can include additional data/results (in form of raw data, tables, and/or diagrams) which were not included in the study manuscript.

## Replication package naming convention
The final name of this repository, as appearing in the published article, should be formatted according to the following naming convention:
`<short conference/journal name>-<yyyy>-<semantic word>-<semantic word>-rep-pkg`

For example, the repository of a research published at the International conference on ICT for Sustainability (ICT4S) in 2022, which investigates cloud tactics would be named `ICT4S-2022-cloud-tactics-rep-pkg`