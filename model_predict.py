from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from collections import Counter

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import re

from getDataFromTiki import fetch_data_from_tiki

# Load data
df = pd.read_csv('./data.csv')
df.dropna(subset=['content'], inplace=True)
df.isnull().sum()
df.drop_duplicates()
# Rename Columns
df.rename(columns={'content': 'Text', 'label': 'Label'}, inplace=True)
# Dropping the Index Colums
df.drop('start',axis=1,inplace=True)
df['Label'] = df['Label'].replace('POS',0)
df['Label'] = df['Label'].replace('NEG',1)
df['Label'] = df['Label'].replace('NEU',2)

df['Text'] = df['Text'].str.replace(r'http\S+', '', regex=True)
df['Text'] = df['Text'].str.replace(r'[^\w\s]', '', regex=True)
df['Text'] = df['Text'].str.replace(r'\s+', ' ', regex=True)
df['Text'] = df['Text'].str.replace(r'\d+', '', regex=True)
df['Text'] = df['Text'].str.lower()

def get_stopwords_list(stop_file_path):
    """load stop words """

    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

stop_path = "./vietnamese-stopwords.txt"
stop = get_stopwords_list(stop_path)

df["Text"] = df['Text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

X = df['Text']
y = df['Label']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tokenizer = Tokenizer(num_words=50000)

tokenizer.fit_on_texts(X_train)
tokenizer.fit_on_texts(X_test)
X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_test_sequences = tokenizer.texts_to_sequences(X_test)

X_train_padded = pad_sequences(X_train_sequences, maxlen=62, padding='post',)
X_test_padded = pad_sequences(X_test_sequences, maxlen=62, padding='post')

# Print the padded sequences for X_train and X_test
print("X_train_padded:")
print(X_train_padded)
print("\nX_test_padded:")
print(X_test_padded)


# Load model
model = load_model('model.h5')
print(model.summary())

def textToVector(text):

  tokenizer.fit_on_texts([text])
  dataNew = tokenizer.texts_to_sequences([text])

  dataNewPadded = pad_sequences(dataNew, maxlen=62, padding='post')
  return dataNewPadded


def textsToVector(text):
  tokenizer = Tokenizer(num_words=50000)



  tokenizer.fit_on_texts(text)
  dataNew = tokenizer.texts_to_sequences(text)

  dataNewPadded = pad_sequences(dataNew, maxlen=61, padding='post')
  return dataNewPadded


product_id = 217176777



def data_after_predict(product_id):
  data = fetch_data_from_tiki(product_id)
  print(data)
  
  predict_data  = []
  for x in data:
    line = re.sub(r'http\S+', "", x['content'])
    line = re.sub(r'[^\w\s]', "", x['content'])
    line = re.sub(r'\s+', "", x['content'])
    line = re.sub(r'\d+', "", x['content'])
    line = line.lower()
    ' '.join([word for word in line.split() if word not in (stop)])

    # x['content'].replace(r'http\S+', '', regex=True)
    # x['content'].replace(r'[^\w\s]', '', regex=True)
    # x['content'].replace(r'\s+', ' ', regex=True)
    # x['content'].replace(r'\d+', '', regex=True)
    # x['content'].lower()

    
    predict_data.append(x['content'])
  
  print(predict_data)

  # h = textsToVector(["sản phẩm này đẹp quá","sản phẩm kém chất lượng", "sai lầm khi mua ở đây","sản phẩm tốt","sản phẩm này đẹp quá","sản phẩm kém chất lượng", "sai lầm khi mua ở đây","sản phẩm tốt"])
  h = textsToVector(predict_data)

  print(h)
  predictions = model.predict(h)

  predicted_labels = predictions.argmax(axis=1)

  # Map label indices to class names
  class_mapping = {0: 'POS', 1: 'NEG', 2: 'NEU'}
  predicted_class_names = [class_mapping[label] for label in predicted_labels]


  counter = Counter(predicted_class_names)

  # print(predictions,counter)

  finalData = []

  for idx, x in enumerate(data):
    finalData.append((x['name'],x['content'],x['purchased'],predicted_class_names[idx]))
    x['predict']= predicted_class_names[idx]

  print(counter, finalData)

  return (counter, finalData)

# counter, finalData = data_after_predict(product_id)

# print(counter,finalData)