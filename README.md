
# CL-TitleParser

### About

**``CL-TitleParser``** parses and types scientific entities from the titles of *C*omputational *L*inguistics scholarly articles written in English. 
Specifically, types the entities as one of six concepts: **_research problem_**, **_solution_**, **_resource_**, **_language_**, **_tool_**, and **_method_**.

It is developed as part of the [Open Research Knowledge Graph Project](https://www.orkg.org/) at [TIB](https://www.tib.eu/en/).

The code released in this repository is the standalone version of the parser.


### Usage

``ORKGTitleParser`` features a native Python implementation requiring minimal effort to set up. Please see usage instructions below.

* Requirements

	* Python (3.7 or higher)

Clone this repository locally and run the parser as follows:

`python parse_titles.py <input_file> <output_data_dir>`

where *input_file* is a file with the papers' titles to be parsed with a new title in each line and *output_data_dir* is a user-specified local directory where the parsed output from the program will be written.


*Additional information on running the parser can be found* [here](https://github.com/jd-coderepos/cl-titles-parser/blob/master/data/README.md)


### Citation

If you use the title parser in your work, please cite our [ICADL 2021 Short Paper](https://doi.org/10.1007/978-3-030-91669-5_31). Article [preprint](https://arxiv.org/abs/2109.00199) available.

```
@InProceedings{10.1007/978-3-030-91669-5_31,
author="D'Souza, Jennifer
and Auer, S{\"o}ren",
editor="Ke, Hao-Ren
and Lee, Chei Sian
and Sugiyama, Kazunari",
title="Pattern-Based Acquisition of Scientific Entities from Scholarly Article Titles",
booktitle="Towards Open and Trustworthy Digital Societies",
year="2021",
publisher="Springer International Publishing",
address="Cham",
pages="401--410",
isbn="978-3-030-91669-5"
}
```

### News

An updated version of the parser that extracts seven concepts from short titles is available [here](https://github.com/jd-coderepos/cl-shorttitles-parser).

