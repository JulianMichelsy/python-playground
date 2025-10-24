from collections import Counter

def count_words(text):
    """
    input text and returns every word and its count 
    """
    words = text.lower().split()
    return dict(Counter(words))

def top_n_words(text, n):
    """
    Returns most frecuent n (unique) words in the text
    """
    words = text.lower().split()
    counter = Counter(words)
    return counter.most_common(n)

# --- Test ---
if __name__ == "__main__":
    text = "hi hi world world world"
    assert count_words(text) == {"hi": 2, "world": 3}
    assert top_n_words(text, 1) == [("world", 3)]
    print("string and collections.py Works properly")
