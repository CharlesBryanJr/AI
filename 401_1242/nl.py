import re
import nltk
import matplotlib.pyplot as plt
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords, state_union
from nltk.tree import Tree
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.collocations import TrigramCollocationFinder
from wordcloud import WordCloud, STOPWORDS

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('state_union')
nltk.download('vader_lexicon')

stop_words = stopwords.words('english')


def create_tokens(text):
    # break text into sentences
    sentenceList = sent_tokenize(text)

    # iterate over sentences and tokenize
    for sentence in sentenceList:
        print(sentence)
        # get parts of speech for tokens in sentence
        print(pos_tag(word_tokenize(sentence)))
        print(' ')


def generate_wordcloud(text):  # optionally add: stopwords=STOPWORDS and change the arg below
    wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
                          width=800, height=400,
                          relative_scaling=1.0,
                          stopwords={'to', 'of'}  # set or space-separated string
                          ).generate(text)

    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
    ## Pick One:
    plt.show()
    # plt.savefig("wordcloud.png")


def process_sentence_for_ner(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    # Tag tokens with part-of-speech tags
    tags = pos_tag(tokens)
    # Chunk tagged tokens into named entity trees
    ne_chunks = ne_chunk(tags)

    # Print the entities and the type of ne_chunks
    print("\nNamed Entities:", ne_chunks)
    print("\nType of named entities:", type(ne_chunks))

    # Return the named entity chunks
    return ne_chunks


def extract_data_from_tree(tree):
    # Iterate through each subtree or leaf in the tree
    for idx in range(len(tree)):
        # If we have a subtree, which is a named entity
        if isinstance(tree[idx], Tree):
            label = tree[idx].label()  # Get the named entity type
            leaves = tree[idx].leaves()  # Get the words and tags within the entity
            for leaf in leaves:
                word, pos = leaf
                print(f"{label}\t{word}\t{pos}\t{type(leaf)}")
        else:
            # If it's not a subtree, then it's a leaf node
            word, pos = tree[idx]
            print(f"None\t{word}\t{pos}\t{type(tree[idx])}")


def find_most_common_trigrams(n):
    """
    Find the most common trigram collocations in the State of the Union corpus.

    Args:
    n (int): The number of most common trigrams to find.

    Returns:
    list: A list of tuples where each tuple contains a trigram and its frequency.
    """
    # Ensure that the necessary corpora are downloaded
    nltk.download('state_union')
    nltk.download('punkt')  # 'punkt' is for tokenization

    # Get words from the State of the Union corpus and filter out non-alphabetic tokens
    words = [w for w in state_union.words() if w.isalpha()]

    # Create a TrigramCollocationFinder from the words
    finder = TrigramCollocationFinder.from_words(words)

    # Find the 'n' most common trigram collocations
    return finder.ngram_fd.most_common(n)


def main():
    print()

    rawtext = "Rollo ran to the store. He paid $23.33 for a ring. He gave Marla the ring. She was happy."
    create_tokens(rawtext)
    print()

    text = "all your base are belong to us all of your base base base"
    generate_wordcloud(text)
    print()

    sentence = "William works at CNN in Dallas."
    tree = process_sentence_for_ner(sentence)
    print()

    extract_data_from_tree(tree)
    print()

    most_common_trigrams = find_most_common_trigrams(2)
    print(most_common_trigrams)
    print()

    sia = SentimentIntensityAnalyzer()
    sia.polarity_scores("Wow, NLTK is really powerful!")




# Check if this is the main script being run
if __name__ == '__main__':
    main()
