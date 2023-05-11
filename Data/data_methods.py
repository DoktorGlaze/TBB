import re
import pandas as pd

def bad_word_count(job_ads):
    '''Summerar antal dåliga ord i datasetet och skapar en sorterad df med antal förekomster av 
    respektive ord'''

    # List of words to count occurrences for
    target_words = []

    with open("Data/ordlista.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        words = line.split()
        for word in words:
            target_words.append(word)

    # Count occurrences of target words
    word_counts = {}
    for index, ad in job_ads.iterrows():
        ad_text = ad['description.text'].lower().replace('.', ' ')
        for target_word in target_words:
            count = len(re.findall(r'\b{}\b'.format(target_word), ad_text))
            if target_word in word_counts:
                word_counts[target_word] += count
            else:
                word_counts[target_word] = count


    # Create a dictionary with the counts of target words
    target_word_counts = {target_word: count for target_word, count in word_counts.items()}

    
    # Sort the dictionary by its values in descending order
    sorted_dict = dict(sorted(target_word_counts.items(), key=lambda x: x[1], reverse=True))

    df = pd.DataFrame.from_dict(sorted_dict, orient='index', columns=['Count'])
    df = df.reset_index()
    df.columns = ['Ord', 'Antal']
    '''
    df.set_index('Ord', inplace=True)'''

    return df

def bad_ads_and_words(job_ads):
    '''Räknar antal annonser som innehåller dåliga ord, summerar antalet dåliga ord
    och räknar ut ett genomsnitt på antal dåliga ord per dålig annons samt procentsats'''
    bad_ads = 0
    total_bad_words = 0

    for index, ad in job_ads.iterrows():
        if ad['Bad_words'] != 0:
            bad_ads += 1
            total_bad_words += ad['Bad_words']
        else:
            continue

    # Count the average amount of bad words for each job ad
    average_bad_words = total_bad_words / bad_ads
    # Count the percentage of bad ads from total ads
    percentage_bad_ads = str(int(bad_ads / len(job_ads) * 100)) + '%'

    # Create a Pandas DataFrame with the results
    df2 = pd.DataFrame({
        "Snitt dåliga ord per annons": [average_bad_words],
        "Andel dåliga annonser": [percentage_bad_ads]
    })

    return df2

def filter_years_and_occ_group(df):
    '''funktion för filtrering av data enligt de interaktiva element vi har'''
    return

def bar_chart_st(job_ads):
    red_ads = 0
    yellow_ads = 0
    green_ads = 0

    for index, ad in job_ads.iterrows():
        if ad['Bad_words'] == 0:
            green_ads += 1
        elif ad['Bad_words'] == 1:
            yellow_ads += 1
        elif ad['Bad_words'] > 1:
            red_ads += 1
        else:
            continue

    return green_ads, yellow_ads, red_ads

    
