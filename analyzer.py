import dbutil
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


CLASSIFICATION = NaiveBayesClassifier(open("train_class.json", 'r'), format='json')


def generate_response(message):
    blob = TextBlob(message, classifier=CLASSIFICATION)
    text_type = blob.classify(message)
    nouns = get_key_nouns(blob)
    sentiment = blob.sentiment(message).polarity
    response = dbutil.find_chat_response(message, text_type, nouns, sentiment)
    return response


def get_key_nouns(blob):
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
    nouns = [all_nouns[0], all_nouns[1], all_nouns[2]]
    return nouns
