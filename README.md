# Parser
>### CS50AI Week 6: An AI to parse sentences and extract noun phrases.

## Contents
1. [Project Synopsis](#project_synopsis)
2. [Project Resources](#project_resources)
3. [Setup and Usage](#setup)
4. [Demo](#video)


## <a id='project_synopsis'> Project Synopsis </a>
The aim of this coursework was to tackle a common task in natural language processing.

Having studied Context-Free Grammar, n-grams, tokenisation, Naive Bayes; looked at concepts such as Attention, and the training architecture of using Transformers in this week's lecture, this was a good opportunity to put this knowledge into practice.

We'd also looked at popular libraries such as word2vec, and nltk. In building this Parsing AI, I was able to explore nltk in more depth.

## <a id='project_resources'> Project Resources </a>
* [nltk](https://www.nltk.org/)
> NLTK is a leading platform for building Python programs to work with human language data.

## <a id='setup'> Setup and Usage </a>
#### [NOTE: Any lines of code included are intended for the command line]

### 1. Install prerequisites
a. Install [Python](https://www.python.org/) </br>
b. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
``` 
 pip install virtualenv
```
### 2. Setup virtual environment
* Create virtual environment </br>
```
# Run this line on the command line
# Replace 'env_name' with whatever your desired env's name is.

virtualenv env_name
```
* Start virtual environment
```
# This will activate your virtualenv.

source env_name/bin/activate
```
* Install required packages
```
# Running this in your command line will install all listed packages to your activated virtual environment

pip install -r requirements. txt
```
### 3. Change directory
* Change into the 'Parser' folder.

### 4. Run parser.py
```
# The usage is as below.

python parser.py [sentence]

# Alternatively, running the below will prompt an input sentence. Be aware that this will only work for sentences comprised of the words outlined in parser.py's TERMINALS list

python parser.py
```

## <a id='Example'> Demo </a>

A successul run of this python script should see command line output as such:

![success](https://github.com/user-attachments/assets/3c9e5338-dc33-4488-a96c-41be0cbd3f07)
