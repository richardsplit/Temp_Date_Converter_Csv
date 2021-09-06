import csv
from tkinter import filedialog


def savefile(take_file):
    output = [{}]
    for item in take_file:
        output = item
        # print(f"{output}")

    # Outputting the file where the user wants  # Saving to CSV with headers

    filename = filedialog.asksaveasfilename(initialdir="C:/Downloads", defaultextension='.csv',
                                            title="Select where to save the output file",
                                            filetypes={("csv files", "*.csv"),
                                                       ("json files", ".json"),
                                                       ("txt files", ".txt"),
                                                       ("all files", "*.*")})

    csv_columns = ['city', 'date', 'temp']

    with open(filename, 'w', newline='') as file_output:

        writer = csv.DictWriter(file_output, delimiter=',', fieldnames=csv_columns)
        writer.writeheader()
        for data in take_file:
            writer.writerow(data)

        file_output.close()
