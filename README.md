# CSV to BibTeX with Google Scholar

<img src="https://github.com/QifHE/CSV-to-BibTeX-with-Google-Scholar/blob/main/bibcover.jpg?raw=true" style="width:80%;margin-left:auto;margin-right:auto;" />

This repo provideds a tool that match lines from a CSV file and convert them to corresponding BibTeX items in Google Scholar with the highest ranking, and save in a bib file. It is useful when you want to re-organize your chaotic citaions in an MS WORD file.

## Prerequisite
- Python 3.x
- [venthur/gscholar](https://github.com/venthur/gscholar)
```
pip install gscholar
```
## Preparation
The code assumes that your CSV files look similar to the following:
| order | reference    |
|-------|--------------|
| 1     | PoinTr       |
| 2     | SnowflakeNet |

An CSV file example is provided in the repo. 

## Run the script

**Make sure that the path is properly set** in the code, and then
```
python csv2bib.py
```