import nltk

def format_rows(docs):
    """Format the text field and strip special characters."""
    D = []
    for d in docs:  # Loop through each item in the Series
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def check_missing_values(df):
    """Check for missing values in DataFrame and return the count."""
    missing_count = df.isnull().sum().sum()  # Count total missing values
    return f"The total amount of missing records is: {missing_count}"

def tokenize_text(text):
    """Tokenize text using the nltk library."""
    tokens = []
    for sentence in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(sentence, language='english'):
            tokens.append(word)
    return tokens