import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import time
import re

cleanup_re = re.compile('[^a-z]+')


def cleanup(sentence):
    sentence = sentence.lower()
    sentence = cleanup_re.sub(' ', sentence).strip()
    return sentence


def f(b):
    start = round(time.time(),6)
    #sleep_time = args.get("time","50")
    df = pd.read_csv("/data/reviews{}mb.csv",format(n))

    df['train'] = df['Text'].apply(cleanup)

    tfidf_vector = TfidfVectorizer(min_df=100).fit(df['train'])

    train = tfidf_vector.transform(df['train'])

    model = LogisticRegression()
    model.fit(train, df['Score'])

    #model_file_path = "/dataout/reviews{}".format(n)
    #joblib.dump(model, model_file_path)
    end = round(time.time(),6)
    #print("{} {}, {}, {}, {}, {}".format(id_n, n, pred, start, end, end-start))
    #print(result)
if __name__ == "__main__":
    event = sys.argv[1]
    f(event)