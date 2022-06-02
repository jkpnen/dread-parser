# !/usr/bin/env python
import re

import bisect

import pandas as pd
from matplotlib import pyplot as plt


USER_DEFINED_COLUMNS = ['username', 'message', 'date']
USER_DEFINED_XLSX_FILE = 'DREAD-MESSAGES.xlsx'
USER_DEFINED_CSV_FILE = 'DREAD-MESSAGES.csv'


def sort_dict_by_value_len(dictionary):
    sorted_list = []
    for key, value in dictionary.items():
        bisect.insort(sorted_list, [len(value), key])
    return sorted_list


def convert_xlsx_to_csv():
    csv_files = {}
    sheets = pd.read_excel(USER_DEFINED_XLSX_FILE, sheet_name=None)
    for sheet in sheets:
        sheets[sheet].to_csv(USER_DEFINED_CSV_FILE, index=False)
        csv_file = pd.DataFrame(pd.read_csv(USER_DEFINED_CSV_FILE))
        csv_file.columns = USER_DEFINED_COLUMNS
        csv_files[sheet] = csv_file
    return csv_files


def plot_pie_chart(values, keys, header):
    fig, ax = plt.subplots()
    for value in list(values):
        if value == 0:
            del keys[values.index(value)]
            del values[values.index(value)]
    ax.pie(values, labels=keys, autopct='%1.1f%%')
    ax.title.set_text(header)
    ax.xaxis.set_label_position('bottom')
    ax.set_xlabel('N = {}'.format(sum(values)))
    plt.show()


def clear_string(text):
    string_wo_emojis = re.sub(
        '[(\U0001F600-\U0001F92F|\U0001F300-\U0001F5FF|\U0001F680-\U0001F6FF|\U0001F190-\U0001F1FF|\U00002702-'
        '\U000027B0|\U0001F926-\U0001FA9F|\u200d|\u2640-\u2642|\u2600-\u2B55|\u23cf|\u23e9|\u231a|\ufe0f)]+',
        '', text)
    string_wo_letters_and_numbers = re.sub(r"[^äöåa-zÄÖÅA-Z0-9]+", ' ', string_wo_emojis)

    return string_wo_letters_and_numbers
