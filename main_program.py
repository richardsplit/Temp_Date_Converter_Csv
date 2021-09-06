from tkinter import filedialog
from dateutil import parser
import save_to_output_file
import temperature_conversion

# Select input file
file = filedialog.askopenfilename(initialdir="C:/Downloads", title="Select a file to convert from",
                                  filetypes=(("csv files", "*.csv"),
                                             ("json files", ".json"),
                                             ("txt files", ".txt"),
                                             ("all files", "*.*")))

new_data_test = []


def write_to_dict(csv_file):
    global new_data_test

    # Open the file to read

    with open(csv_file, "r") as my_file:
        data = my_file.read()

    # Convert the csv into a python dictionary

    rows = data.split("\n")

    order_dict = {}
    for row in rows:
        print(' ')

        # Split the row into info
        info = row.split(",")

        # Check if the row is the proper length
        if len(info) == 3:
            city = info[0]
            timezone_date = info[1]
            temperature = info[2]

            # Temperature conversion
            temperature_conversion.temp_conv(temperature)

            # Timezone Conversion
            converted_date = str(parser.parse(timezone_date))

            order_dict = {"city": city, "date": converted_date, "temp": temperature}

            new_data_test += [order_dict]

    return new_data_test


write_to_dict(file)

output_file = write_to_dict(file)

save_to_output_file.savefile(output_file)
