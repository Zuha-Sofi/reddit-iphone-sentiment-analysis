import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

class RedditProcessing:
    """
    This class is used to pre-process Reddit posts. This centralizes the processing to one location.
    Feel free to add or edit.
    """

    def __init__(self, tokeniser, lStopwords, lemmatizer):
        """
        Initialise the tokeniser, stopwords, and stemmer to use.

        @param tokeniser: Tokenizer to use for splitting text into tokens.
        @param lStopwords: List of stopwords to remove from text.
        @param lemmatizer: Lemmatizer to use for reducing words to their root forms.
        """
        self.tokeniser = tokeniser
        self.lStopwords = lStopwords
        self.lemmatizer = lemmatizer

    def process(self, text):
        """
        Perform the processing.

        @param text: The text (post) to process.

        @returns: List of (valid) tokens in text.
        """
        # Convert text to lowercase
        text = text.lower()

        # Tokenize
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]

        # Define regex patterns
        regexDigit = re.compile(r"^\d+(\.\d+)?$")
        regexHttp = re.compile(r"http")
        regexNonAscii = re.compile(r'[^\x00-\x7F]+')

        # Process tokens
        processed_tokens = [
            self.lemmatizer.lemmatize(tok) for tok in tokensStripped
            if tok not in self.lStopwords and len(tok) > 2  and not regexDigit.match(tok) and not regexHttp.match(tok) and not regexNonAscii.match(tok)
        ]

        return processed_tokens
