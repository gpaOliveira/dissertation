import csv
import pdb

COLUMNS_TO_COUNT = ["Year", "INVEST : Independent","INVEST : Negotiable","INVEST : Valuable","INVEST : Estimable","INVEST : Small","INVEST : Testable","BABOK 3 : atomic","BABOK 3 : complete","BABOK 3 : consistent","BABOK 3 : concise","BABOK 3 : feasible","BABOK 3 : unambiguous","BABOK 3 : testable","BABOK 3 : prioritized","BABOK 3 : understandable","BABOK 2 : cohesion","BABOK 2 : completeness","BABOK 2 : consistency","BABOK 2 : correction","BABOK 2 : viability","BABOK 2 : adaptability","BABOK 2 : unambiguity","BABOK 2 : testability","Test As Requirement", "BABOK", "BABOK 3", "BABOK 2", "INVEST"]

def initialize_count_one_column_values_if_needed(value, column_values):
    if value not in column_values:
        column_values[value] = {}
        column_values[value]["count"] = 0
        column_values[value]["details"] = []

def count_partial_column_values(file, partial_column_to_count):
    column_values = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        initialize_count_one_column_values_if_needed("Total", column_values)
        for row in reader:
            discovered_column_to_count = [column for column in row.keys() if partial_column_to_count in column]
            for column_to_count in discovered_column_to_count:
                if len(row[column_to_count]) > 0:
                    to_add = row["ID Paper"] + " " + row["Title"]
                    initialize_count_one_column_values_if_needed(row[column_to_count], column_values)
                    if to_add not in column_values[row[column_to_count]]["details"]:
                        column_values[row[column_to_count]]["count"] += 1
                        column_values[row[column_to_count]]["details"].append(to_add)
                column_values["Total"]["count"] += 1
            
    return column_values
    
def print_each_row_data(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        for row in reader:
            print()
            print(row["ID Paper"], row["Title"])
            for column in row.keys():
                if column not in ["ID Paper", "Title"] and len(row[column]) > 0:
                    if row[column] == "Y":
                        print(">>>", column)
                    else:
                        print(">>>", column, "=", row[column])
                
def print_dict_per_line(dict, details=False, header=None):
    if header:
        print(header)
        
    for k in sorted(dict.keys()):
        print(k, dict[k]["count"])
        if details:
            print (" ".join(["\cite{" + d.split()[0] + "}" for d in dict[k]["details"]]))

if __name__ == "__main__":
    file = "mono_data.csv"
    for c in COLUMNS_TO_COUNT:
        print_dict_per_line(count_partial_column_values(file, c), True, c + " Count Details")
        print()
    print_each_row_data(file)