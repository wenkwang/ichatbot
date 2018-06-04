import dbutil
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from common import *

# CLASSIFICATION = NaiveBayesClassifier(open("resource/train_class.json", 'r'), format='json')
# CLASSIFICATION = NaiveBayesClassifier(train)


def generate_response(text):
    # blob = TextBlob(message, classifier=CLASSIFICATION)
    # text_type = blob.classify(message)
    blob = TextBlob(text)
    text_type = TEXT_STATEMENT
    nouns_str = get_key_nouns_str(blob)
    sentiment = blob.sentiment(text).polarity
    response = dbutil.find_chat_response(text, text_type, nouns_str, sentiment)
    return response


def get_key_nouns_str(blob):
    all_nouns = blob.noun_phrases
    frequency = []
    for noun in all_nouns:
        frequency.append(dbutil.get_word_count(noun))
    for i in range(3):
        for j in range(i + 1, len(all_nouns)):
            if frequency[j] > frequency[i]:
                tmp_freq = frequency[i]
                tmp_noun = all_nouns[i]
                frequency[i] = frequency[j]
                all_nouns[i] = all_nouns[j]
                frequency[j] = tmp_freq
                all_nouns[j] = tmp_noun
    words = [all_nouns[0], all_nouns[1], all_nouns[2]]
    words.sort()
    nouns_str = words[0] + ";" + words[1] + ";" + words[2]
    return nouns_str


