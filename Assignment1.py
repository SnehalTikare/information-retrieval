import glob
import os
import string
import nltk
from nltk.tokenize import word_tokenize
#Uncomment this when running the file for the first time
#nltk.download('all')
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#Reads all the files from the specified path and returns a list
#Argument: Empty list
#Return list containing information from all the files
def get_files(corpus):
    file_list = glob.glob(os.path.join(os.getcwd(), "/Users/snehaltikare/Documents/Information Retrieval/citeseer","*"))
    for file_path in sorted(file_list):
        with open(file_path) as f_input:
            corpus.append(f_input.read().replace('\n', '')) 
    return corpus 

#Function to preprocess the data
#Argument:list of strings
#Return tokenized lists
def preprocessing(corpus):
    corpus=[item.lower() for item in corpus]#convert the the words to lower case
    corpus=[s.translate(str.maketrans('', '', string.punctuation)) for s in corpus] #Remove the punctuations
    corpus=[s.replace('\n','').replace('\r','') for s in corpus] #Remove line breaks
    tokenized_corpus=[word_tokenize(item) for item in corpus] #Tokenize the sentences
    tokenized = [y for x in tokenized_corpus for y in x] #Convert lists of lists to single list containing the tokens
    return tokenized

#Function that returns total number of tokens in a list
#Argument tokenized list
#Returns the number of words in list
def numberOfWords(tokenized):
    return len(tokenized)

#Function that return the top K frequent words in a list
#Arguments: tokenized list, i: K (top k frequent word)
def getMostCommon(tokenized,i):
    frequency=Counter(tokenized) #Dictionary with words and their frequencies
    return frequency.most_common(i)

#Function that returns the number of words accounting for x% of total words
#Argument: tokenized list, percentage
def numberWordPercent(tokenized,per):
    count=0
    frequency=Counter(tokenized)
    token_set=frequency.most_common()
    word_acc=0
    i=0
    wordPercent=[]
    percent=(per*len(tokenized))/100 # x% of total words
    while(word_acc<percent):
        count=count+1
        word_acc=word_acc+token_set[i][1]
        wordPercent.append(token_set[i][0])
        i+=1       
    return count

#Function that returns the list of stop words in top K frequent words
#Arguments: list of top frequent words
def getStopWords(mostcommon):
    mc_stopwords=[]
    stopwords=stopWordList()
    for word in mostcommon:
        if(word[0] in stopwords):
            mc_stopwords.append(word[0])
    return mc_stopwords

#Function that returns list of stopwords
def stopWordList():
    stoplist=[]
    filestopword=open('/Users/snehaltikare/Documents/Information Retrieval/stopwords.txt')
    for line in filestopword:
        w = line.split()
        for word in w:
            stoplist.append(word)
    return stoplist

#Function to remove stopwords from the given tokens
#Argument : tokenized list
def removeStopWords(tokenized):
    stoplist=stopWordList()
    token_nostop=[i for i in tokenized if not i in stoplist ]
    return token_nostop

#Function to stem the list of tokens using porterStemmer of nltk library
#Argument: tokenized list containing no stop words 
def porterStemmer(token_nostop):
    stemmer=PorterStemmer()
    token_stemmed=[stemmer.stem(word) for word in token_nostop]    
    return token_stemmed

#Main function
def main():
    corpus=[]
    corpus=get_files(corpus)
    tokenized=preprocessing(corpus)
    print("\n1a)Total number of words in collections- "+ str(numberOfWords(tokenized)))
    print("1b)Vocabulary size(Number of unique words- "+ str(numberOfWords(set(tokenized))))
    print("1c)Top 20 words in the ranking")
    mostcommon=getMostCommon(tokenized,20)
    mostcommonwords=[]
    for words in mostcommon:
        mostcommonwords.append(words[0])
    print(mostcommonwords)
    print("1d)Stopwords in top 20 words- " + str(getStopWords(mostcommon)))
    print("1e)Number of words accounting for 15% of total words- "+ str(numberWordPercent(tokenized,15)))
    token_nostop=removeStopWords(tokenized)
    token_stemmed=porterStemmer(token_nostop)
    print()
    print("After stop words removal and stemming\n")
    print("2a)Total number of words in collections- "+ str(numberOfWords(token_stemmed)))
    print("2b)Vocabulary size(Number of unique words- "+ str(numberOfWords(set(token_stemmed))))
    mostcommon=getMostCommon(token_stemmed,20)
    mostcommonwords=[]
    for words in mostcommon:
        mostcommonwords.append(words[0])
    print(mostcommonwords)
    print("2d)Stopwords in top 20 words- " + str(getStopWords(mostcommon)))
    print("2e)Number of words accounting for 15% of total words- "+ str(numberWordPercent(token_stemmed,15)))


main()




