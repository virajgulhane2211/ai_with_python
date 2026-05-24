# NLP Tokenization and Keyword Classifier
text = "Congratulations you won a free prize click now"
spam_words = {"free","prize","win","won","click"}
tokens = text.lower().split()
hits = [w for w in tokens if w in spam_words]
print("Tokens:", tokens)
print("Class:", "Spam-like" if len(hits) >= 2 else "Normal")
