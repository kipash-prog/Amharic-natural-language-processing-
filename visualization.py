import numpy as np
import matplotlib.pyplot as plt # type: ignore
from tabulate import tabulate
from statistics import mean
from nltk.probability import FreqDist
import math

def rank(preprocesseds):
    freqdist = FreqDist(preprocesseds)
    freqdist = sorted(freqdist.items(), key=lambda tup: tup[1], reverse=True)

    voc_size = len(freqdist)

    # print("Token Size: ", len(preprocesseds))
    # print("Vocanular Size: ", voc_size)
    
    upper = math.floor(voc_size * 9 / 100)
    lower = math.floor(voc_size * 60 / 100)
    # print("upper: ", upper,"lower: ", lower)

    # put word on rank based on frequency
    rows = []
    for i, word_freq in enumerate(freqdist):
        word, freq = word_freq
        
        rank = i+1

        if rank < upper:
           continue
        if rank > lower:
           break
        
        freq_rank = freq * rank 

        rows.append([rank, word, freq, freq_rank])
    return rows    


def table(preprocesseds):
    rows = rank(preprocesseds)
    print("Filtered Words")
    print(tabulate(rows , headers=["Rank", "Word", "Frequency", "Frequency x Rank"], tablefmt="grid"))



def plot_function_vs_rank(preprocesseds):
    rows = rank(preprocesseds)
    ranks = [row[0] for row in rows]  # Extract ranks from the data
    frequencies = [row[2] for row in rows]  # Extract frequencies from the data

    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    plt.plot(ranks, frequencies, marker='o', color='b', linestyle='-')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Function vs Rank Graph for Word Frequencies')
    plt.grid(True)
    plt.show()