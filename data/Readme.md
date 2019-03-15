The dataset for this project is available 
[here](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)


There were some oddities with the download which I cleaned as follows:
- UNSW- is sometimes mistyped as NUSW : rename file to UNSW..
- The Full database: UNSW-NB15[1-3] : These files are supposed to be 700000 lines. They are 700001 lines. The last line of file N is the same as the first line of file N+1. Delete the duplicated line to get the value counts to match the LIST\_EVENTS file.
- Backdoor attacks are labeled both 'Backdoor' and 'Backdoors'. Merge these into one attack category. 
- The features file applies to the full dataset; the features for the 10 percent test/train sets are in the files themselves. 
- Within the features file, there is a column name name with a space that needs to be corrected if you are using this file as input to a program.  My headers are in headers.csv
- The training and testing sets are mixed up. Swap the names of the files. (The training set should be larger than the test holdout.)
