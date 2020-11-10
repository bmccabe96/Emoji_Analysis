# Emoji_Analysis
Use NLP techniques to analyze emotions of election related tweets.

## Project Overview
The usage of certain emojis in social media tells a strong story regarding the emotion that the author of the tweet, blog, comment, etc is trying to convey. Paul Ekman, an American psychologist, held a theory that emotions can be broken into 6 classes: anger, disgust, fear, happiness, sadness and surprise. Using this as a baseline, along with a project released by the Instagram Data Science team which clustered emojis together, I chose to pick four of these emotions to attempt to train a classification model around (4 emotions I deemed had enough of a difference to train a model around given limited data): **anger, fear, happiness and sadness**.

![Image](pics/insta_2.png?raw=true) 

This project, due to time and data constraints, specifically picked out election related tweets, since I believed tweets on the election would likely evoke strong emotions. Assuming the trained model has good results, this could be highly useful for campaign managers to get emotional analysis regarding an election. The labeling of data is a very important task in the world of data analytics and data science, and to be able to appropriately classify tweets into emotions would be very useful to campaign managers (and other organizations too, assuming this model eventually expands outside the realm of election related tweets).

## Items of Note
 * **Analysis/**: Has notebooks detailing EDA, modeling, and initial "app". Analysis of results are discussed in respective notebooks.
 * **pics/**: All illustrations
 * **Scripts/**: Data gathering scripts

## Procedure

### Data Acquisition
 * Twython API
 * MySQL Database
 * Ran data gathering script for a week up to and slightly after the 2020 election
 * Roughly 1,000,000 tweets gathered, 82,000 with emojis, and 5,000 with my targeted emotional emoji classes
 
### EDA and Data Cleaning
 * Consolidate all tweets into just those tweets with our targeted emotional classes
 * Create wordclouds of each class (see EDA notebook)
 * Remove usernames, remove https, remove character repetitions, lowercase, lemmatization, tokenization
 * Analyze the differences in sentiment, subjectivity, use of capitalization, use of exclamation points, and use of profanity. A violin plot of sentiment scores is shown below, but the EDA notebook addresses all in detail.

![Image](pics/emoji_count_and_sentiment.png?raw=true)
![Image](pics/Sentiments.png?raw=true)


### Feature Engineering
 * Feature union of custom features mentioned above, TF IDF using unigrams and bigrams (stopwords have been removed), and TF IDF of bigrams through 10-grams (stopwords not removed) into a pipeline
 * Utilized custom functions, VADER Sentiment Analyzer, Textblob and standard NLTK functionalities

### Modeling
 * Addressed class imbalance with appropriate class weights in one notebook, and resampling methods in another
 * Logistic Regression, Support Vector Machine, Random Forest, Multinomial Bayes, Bernoulli Bayes, Passive Aggressive Classifier, XGBoost, Voting Classifier
 * **Best Model: XGBoost** with an accuracy score of roughly 80% and an F1-Score of 79%

![Image](pics/class_imbalance.png?raw=true) 
![Image](pics/model_performances.png?raw=true) 

## Conclusion




