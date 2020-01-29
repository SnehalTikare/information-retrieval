## Information-retrieval
Course assignments and projects based on text processing
Filename :  Assignment1.py

__Environment:__ <br />
Python version: Python 3 and above

__Libraries :__ <br />
Install the below libraries<br />
- pip install -U nltk <br />
- sudo python -m nltk.downloader all
 
 
__Instructions to run the program:__<br />
1. Using Terminal<br />
	1) Open the command prompt<br />
   		1) Windows -> win+r -> cmd->’enter’ <br />
   		2) Mac OS -> cmd+shift+space -> type ‘terminal’ -> ‘enter’<br />
   		3) Ubuntu -> ctrl+alt+t<br /><br />
	 
	2) Steps to run the file
   		1) Type 'Python3 /path where the file is stored/Assigment1.py' <br />

Once the command prompt/terminal is open <br />
Type ‘python’ to check the version of python installed<br />
__Note: some of the functionalities used in the program are compatible with only python 3 and above.__<br />
__Please use python 3 and above to run the program__<br />



2. Using any IDE

	a) Open the IDE, file -> open the folder where the given files are saved<br />
	b) Open assignment1.py, right click-> choose ‘Run python file in terminal’<br />


__Functionalities of each module of the program__<br />
1) def get_files<br />
Reads all the files from the specified path and returns a list<br />
Argument: Empty list<br />
Return list containing information from all the files<br /> 

2) def preprocessing(corpus):<br />
Function to preprocess the data<br />
Argument:list of strings<br />
Return tokenized lists <br />

3) def numberOfWords(tokenized):<br />
Function that returns total number of tokens in a list<br />
Argument tokenized list<br />
Returns the number of words in list<br />

4) def getMostCommon(tokenized,i):<br />
Function that return the top K frequent words in a list<br />
Arguments: tokenized list, i: K (top k frequent word)<br />

5) def numberWordPercent(tokenized,per):<br />
Function that returns the number of words accounting for x% of total words<br />
Argument: tokenized list, percentage<br />

6) def getStopWords(mostcommon):<br />
Function that returns the list of stop words in top K frequent words<br />
Arguments: list of top frequent words<br />

7) def stopWordList():<br />
Function that returns list of stopwords<br />

8) def removeStopWords(tokenized):<br />
Function to remove stopwords from the given tokens<br />
Argument : tokenized list<br />

9) def porterStemmer(token_nostop):<br />
Function to stem the list of tokens using porterStemmer of nltk library<br />
Argument: tokenized list containing no stop words <br />



__Before stop words removal and stemming__

1a) Total number of words in collections- 476263<br />
1b) Vocabulary size(Number of unique words- 19885<br />
1c) Top 20 words in the ranking<br />
['the', 'of', 'and', 'a', 'to', 'in', 'for', 'is', 'we', 'that', 'this', 'are', 'on', 'an', 'with', 'as', 'by', 'data', 'be', 'information']
<br />
1d) Stopwords in top 20 words- ['the', 'of', 'and', 'a', 'to', 'in', 'for', 'is', 'we', 'that', 'this', 'are', 'on', 'an', 'with', 'as', 'by', 'be']
<br />
1e) Number of words accounting for 15% of total words- 4<br />

__After stop words removal and stemming__<br />

2a) Total number of words in collections- 265776<br />
2b) Vocabulary size(Number of unique words- 13556<br />
['system', 'data', 'agent', 'inform', 'model', 'paper', 'queri', 'user', 'learn', 'algorithm', '1', 'approach', 'problem', 'applic', 'present', 'base', 'web', 'databas', 'comput', 'method']<br />
2d) Stopwords in top 20 words- []<br />
2e) Number of words accounting for 15% of total words- 22


