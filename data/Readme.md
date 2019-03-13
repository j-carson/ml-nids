The dataset for this project is available 
[here](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)


There were some oddities with the download which I cleaned as follows:
- UNSW- is sometimes mistyped as NUSW : rename file to UNSW..
- The Full database: UNSW-NB15[1-3] : These files are supposed to be 700000 lines, they are 700001 lines. The last line of file N is the same as the first line of file N+1. Delete the duplicated lines to get the value counts in the LIST\_EVENTS file
- Backdoor attacks are labeled both 'Backdoor' and 'Backdoors'. Merge these into one attack category. 
- The features file applies to the full dataset, the training/testing data files have slightly different columns. There is a header line in training/testing files. 
- For the full dataset, the headers are in the features file, but there was a column name with a space that needs to be corrected if you are using this file as input to a program. 
My header are in headers.csv
