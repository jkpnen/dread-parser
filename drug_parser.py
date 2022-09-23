import tkinter

import matplotlib

from xlsxwriter import Workbook

from consts import STOPWORDS, DRUGS, DRUG_CATEGORIES
from general_functions import sort_dict_by_value_len, convert_xlsx_to_csv, plot_pie_chart, clear_string

matplotlib.use('TkAgg')  # For plotting

# File conversion that makes it easier to handle the data
csv_files = convert_xlsx_to_csv()

# Empty dicts
found_drugs = {}
all_drugs = {}

# Initialize dictionaries based on the user defined set
for drug in list(DRUGS.keys()):
    found_drugs[drug] = []
    all_drugs[drug] = []

# Sort by date
for csv_file in csv_files:
    sorted_by_date = csv_files[csv_file].sort_values('date', ascending=False)
    csv_files[csv_file] = sorted_by_date

# Make a dataframe based on the messages from the given csv-file
user_defined_column = 'message'
for city in csv_files:
    messages = csv_files[city][user_defined_column]
    messages_df = messages.to_frame().reset_index()

    for drug in list(DRUGS.keys()):
        found_drugs[drug] = []

    words_total = 0
    messages = messages_df[user_defined_column]
    for message in messages:
        if type(message) is not str:
            message = str(message)

        drugs_copy = DRUGS.copy()

        message = clear_string(message)
        message = message.lower()
        words = message.split()

        for i in range(len(words)):
            words_total += 1
            for key, value in list(drugs_copy.items()):
                if any(substring in words[i] for substring in STOPWORDS):
                    continue
                else:
                    if words[i].startswith(tuple(value)):
                        found_drugs[key].append(words[i])
                        all_drugs[key].append(words[i])
                        del drugs_copy[key]  # Only one found drug per message

    found_drugs_sorted = sort_dict_by_value_len(found_drugs)

    found_drugs_keys_sorted = []
    found_drugs_values_sorted = []
    for drug in found_drugs_sorted:
        found_drugs_keys_sorted.append(drug[1])
        found_drugs_values_sorted.append(drug[0])

    # Plot city by city
    plot_pie_chart(found_drugs_values_sorted, found_drugs_keys_sorted, city)

# Sort
found_drugs_keys_sorted = []
found_drugs_values_sorted = []
for key, value in all_drugs.items():
    found_drugs_keys_sorted.append(key)
    found_drugs_values_sorted.append(len(all_drugs[key]))

# Plotting
pie_title = "KOKO SUOMI"
plot_pie_chart(found_drugs_values_sorted, found_drugs_keys_sorted, pie_title)


# List all found strings (drugs) by category
def drugs_to_xlsx():
    filename = "DRUGS-BY-CATEGORY.xlsx"
    wb = Workbook(filename)
    ws = wb.add_worksheet("DRUGS")
    first_row = 0
    for header in DRUG_CATEGORIES:
        col = DRUG_CATEGORIES.index(header)  # Keeps the order
        ws.write(first_row, col, header)  # The first row which is also the header of the worksheet

    for drug_keys, drug_values in all_drugs.items():
        row = 1
        for drug_value in drug_values:
            col = DRUG_CATEGORIES.index(drug_keys)
            ws.write(row, col, drug_value)
            row += 1

    wb.close()


drugs_to_xlsx()
