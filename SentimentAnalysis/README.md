# Task Details:
Create a text classification corpus or your choice. Suggestions
1. Download reviews from various sites and annotating each review as either positive,
negative or neutral sentiment
2. Download documents of different topics and annotate each document with the relevant
topic e.g. sports, history etc.
Save your corpus as one .csv file with each document in a cell and the corresponding label in the
adjacent cell.

**Text Classification**
1. Preprocess your text and document the steps you took to preprocess your documents
2. Vectorize your texts with one of the document representation echniques discussed in class.
3. Train and test a classification model using the corpus you have created e.g. Naïve bayes or
SVM or Decision tree or KNN
4. Use precision, recall and f-score to measure your model performance

**Clustering**
- Using the same corpus (without the labels):
1. Preprocess your text documents
2. Perform clustering on the document for find clusters
3. Compare the clusters found vs the true class labels of the documents. Have documents with
the same class label been put in the same cluster?
4. Comment on your results.


# IMDb Movies Reviews
I'll be using the IMDb dataset available on the Stanford AI Group website for my task.

**Step 1**:

We use the `os` library to iterate over the text files in the train and test directories, and load the contents into dataframes. We then save the dataframes to CSV files using the to_csv method. The resulting CSV files will have two columns, "Sentiment" and "Label", where "Sentiment" contains the text of the reviews and "Label" contains either "pos" or "neg" to indicate the sentiment of each review.
