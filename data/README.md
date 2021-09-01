### Example input data

1. ``anthology.bib`` downloaded from https://www.aclweb.org/anthology/ on 1-02-2021. It can be downloaded directly from ACL by clicking the blue button `Full Anthology as BibTeX` on the website.

2. ``acl-titles.dat`` is an example input data file to the ``ORKGTitleParser``. It contains a list of 60,621 scholarly article titles from the ``anthology.bib`` file referenced in this repo.

	* The current version of the program parses 50,237 titles from 60,621 total titles.
	* It extracts: 19,799 **_research problem_**; 18,111 **_solution_**; 20,033 **_resource_**; 1,059 **_language_**; 6,878 **_tool_**; and 21,687 **_method_**. 

3. The script `extract_titles_from_acl_anthology.py` was used to convert ``anthology.bib`` to the desired input file ``acl-titles.dat`` that the ``ORKGTitleParser`` takes as input.
It is released additionally for converting an newer versions of ``anthology.bib`` to the ``ORKGTitleParser`` input file.