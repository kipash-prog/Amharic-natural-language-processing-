# from preprocessor import remove_tags
# import math

# urls = {}


# def add_src():
#     url = input("Enter URL: ")
#     return add(url)



# def add(url):
#     documents = {}
#     pages = {}
#     urls[len(urls)] = url

    

#     content = remove_tags(url)
#     words = content.split()

#     #print(words)

#     max_words_per_document = 50
#     num_documents = math.ceil(len(words) / max_words_per_document)

#     page_content = []
#     page_path = "Doc/URL/" + str(len(urls))
#     for i in range(num_documents):
#         start_index = i * max_words_per_document
#         end_index = start_index + max_words_per_document
#         doc = words[start_index:end_index]

#         doc_path = page_path + "/" + str(i)
        
#         documents[doc_path] = " ". join(doc)
#         page_content.append(" ". join(doc))
                
#         # print(page_content)
#     page_content.append("URL: " + url)
#     pages[page_path] = page_content

#     return pages, documents

# # add_src()


import csv
import os
import math
from preprocessor import remove_tags

CSV_FILE_PATH = "urls.csv"
urls = {}
url_id = 0

def add_src():
    try:
        url = input("Enter URL: ")
        pages, documents = add(url)
        save_urls_to_csv(url)
        if pages and documents:
            print("Pages and documents have been processed successfully.")
        else:
            print("Failed to process the URL.")

        return pages, documents
    except Exception as e:
        print(f"An error occurred while reading your URL: {e}")
        add_src()
    

def add(url):
    documents = {}
    pages = {}
    url_id = len(urls)
    urls[url_id] = url

    try:
        content = remove_tags(url)
        words = content.split()

        max_words_per_document = 50
        num_documents = math.ceil(len(words) / max_words_per_document)

        page_content = []
        page_path = "Doc/URL/" + str(url_id)
        for i in range(num_documents):
            start_index = i * max_words_per_document
            end_index = start_index + max_words_per_document
            doc = words[start_index:end_index]

            doc_path = page_path + "/" + str(i)

            documents[doc_path] = " ". join(doc)
            page_content.append(" ". join(doc))

        page_content.append("URL: " + url)
        pages[page_path] = page_content

        return pages, documents
    except Exception as e:
        print(f"An error occurred while processing the URL: {e}")
        return None, None


def save_urls_to_csv(_url):
    try:
        with open(CSV_FILE_PATH, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            url_id = len(urls)            
            writer.writerow([url_id, _url])
    except Exception as e:
        print(f"An error occurred while saving URLs to CSV: {e}")



def load_urls_from_csv():
    if not os.path.exists(CSV_FILE_PATH):
        return

    try:
        csv_urls = []
        with open(CSV_FILE_PATH, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Ensure the row is not empty
                    #id = int(row[0])
                    url = row[1]
                    csv_urls.append(url)
                    
                    

        pages = {}
        documents = {}
        for val in csv_urls:
            page, document = add(val)
            # print("\n\n", val, ": \n")    

            pages.update(page)
            documents.update(document)
            
            # print(pages)
            
        return pages, documents
    except Exception as e:
        print(f"An error occurred while reading URLs from CSV: {e}")

# Main script execution


def add_txt():
    documents = {}
    pages = {}
    url_id = 1
    urls[url_id] = "additional_data_set"

    try:
        with open("additional_data_set.txt","r",encoding="utf-8") as my_file:
            data_set = my_file.read()
            words = data_set.split()

            max_words_per_document = 300
            num_documents = math.ceil(len(words) / max_words_per_document)

            page_content = []
            page_path = "Local/Doc1/" + str(url_id)
            for i in range(num_documents):
                start_index = i * max_words_per_document
                end_index = start_index + max_words_per_document
                doc = words[start_index:end_index]

                doc_path = page_path + "/" + str(i)

                documents[doc_path] = " ". join(doc)
                page_content.append(" ". join(doc))

            page_content.append("Path: " + "additional_data_set")
            pages[page_path] = page_content

        
        with open("additional_data_set1.txt","r",encoding="utf-8") as my_file1:
            data_set = my_file1.read()
            words = data_set.split()

            max_words_per_document = 300
            num_documents = math.ceil(len(words) / max_words_per_document)
            

            page_content = []
            page_path = "Local/Doc2/" + str(url_id)
            for i in range(num_documents):
                start_index = i * max_words_per_document
                end_index = start_index + max_words_per_document
                doc = words[start_index:end_index]

                doc_path = page_path + "/" + str(i)

                documents[doc_path] = " ". join(doc)
                page_content.append(" ". join(doc))

            page_content.append("Path: " + "additional_data_set")
            pages[page_path] = page_content

        # print("Num of documents: ", num_documents)

        return pages, documents
    except Exception as e:
        print(f"An error occurred while processing the URL: {e}")
        return None, None



#add_txt()
load_urls_from_csv()