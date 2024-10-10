import math
from preprocessor import *
from visualization import *
from add_dataset import add_src, urls, load_urls_from_csv, add_txt
from cosine import get_cosine
from bible_data_struct import read_bible


documents = {}
pages = {}
paths = {}
preprocessed = {}


# do all the preprocessing to the document added from (add_docs function)
def preprocess(content):
    cleaned = cleaner(content)
    word_tokenized = word_tokenize(cleaned) 
    stop_removed = remove_stop_words(word_tokenized) 
    stemmed_words = [stem_prefix_suffix(term) for term in stop_removed]

    return stemmed_words



# add documents

def add_docs(page, docs):
    # add additional doc to the document set(dictionary)
    documents.update(docs)
    pages.update(page)
    #print(pages)
    
    # process additional document
    _preprocessed = {}
    for path, document in docs.items():
        _preprocessed[path] = preprocess(document)
        #print(path, ": ", preprocessed[path])

    # add the additional processed document to preprecessed set(dictionary)
    preprocessed.update(_preprocessed)

    # get inverted index for the additional document
    invert_index(_preprocessed)



# visualization
def visualize_data():
    corpus = []
    for path, document in preprocessed.items():
        corpus.extend(document)

    table(corpus)
    plot_function_vs_rank(corpus)




# see the documents index and the content of the preprocessed documents 
# for doc_id,doc in enumerate(preprocessed):
#     print (f"document{doc_id + 1}: ",doc)



# Build inverted index
inverted_index = {}
def invert_index(_preprocessed):
    for path, document in _preprocessed.items():
        for term in document:
            if term not in inverted_index:
                inverted_index[term] = []
            inverted_index[term].append(path)



# get list of inverted index
# def get_indices():
#     print_upto = 'ወንድማች'

#     for k, v in inverted_index.items():
#         print(k, v)
#         if k == print_upto:
#             break



# Accept query from user
def query(keyword):
    # Preprocess the keyword
    query_terms = preprocess(keyword)

    # Perform the search
    matching_documents = []
    for term in query_terms:
        if term in inverted_index:
            matching_documents.extend(inverted_index[term])

    # Remove duplicates from matching documents
    matching_documents = list(set(matching_documents))

    # Rank the search results
    if matching_documents:
        rank_result(query_terms, matching_documents)
    else:
        print("No matching documents found. \n")

    return matching_documents



# rank result by relevancy using cosine
def rank_result(query_terms, matching_documents):
    scores = {}
    for doc_id in matching_documents:
        #print(query_terms, " ", documents[doc_id])
        scores[doc_id] = get_cosine(query_terms, preprocessed[doc_id])
    
    #sort based on score (cosine)
    ranked_docs = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    print("\nMatching documents: \n")
    ranked_paths = []
    for doc_id, score in ranked_docs:
        result = documents[doc_id]
        ranked_paths.append(doc_id)
        print(f"{len(ranked_paths)}. Document ID: {doc_id} - Score: {score} \nDocument: {result}\n")
        
    get_doc(ranked_paths)



def get_doc(ranked_paths):
    try:
        u_input = int(input("Enter Which Doc's Detail you Want to see: "))
        
        chapter_path =  '/'.join(ranked_paths[u_input-1].split('/')[:3])
        chapter_path = chapter_path.strip()
        chapter_content = pages[chapter_path]

        print("\n",chapter_path, "\n")
        for i in range(len(chapter_content)):
            print( (i+1),". " ,chapter_content[i], "\n")
    except Exception as e:
        print(f"An error occurred while getting the source: {e}")




# add default corpes(bible)  added before user 
bible_data = read_bible('bible')
add_docs(bible_data[0], bible_data[1])

# add from previously added urls from csv file
csv_doc = load_urls_from_csv()
add_docs(csv_doc[0], csv_doc[1])

# add from txt file
# text_dataset = add_txt()
# add_docs(text_dataset[0], text_dataset[1])

# print("Inverted Index Size: ", len(inverted_index))

# User Interaction
def navigation():
    u_input = input("Press '*1' to add more source \nPress '*2' to get Visualization \nPress '*3' to show added URL's \nPress '*4 to get the whole document'  \nPress '*5' to quit \nType your Keyword to search \n\nEnter: ")

    if u_input == '*1':
        try: 
            src = add_src()
            page = src[0]
            docs = src[1]
            add_docs(page, docs)
            navigation()
        except Exception as e:
            print(f"An error occurred while adding a source: {e}")
            navigation()
    elif u_input == '*2':
        try:
            visualize_data()
            navigation()
        except Exception as e:
            print(f"An error occurred while Visualizing: {e}")
            navigation()
    elif u_input == '*3':
        try:
            print("URL's: ", urls)
            navigation()
        except Exception as e:
            print(f"An error occurred while showing URL's: {e}")
            navigation()
    elif u_input == '*5':
        print("closing...")
    else:
        try:
            query(u_input)
            navigation()
        except Exception as e:
            print(f"An error occurred while searching for a query: {e}")
            navigation()

# Start User Interaction
navigation()