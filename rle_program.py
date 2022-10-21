import console_gfx


def count_runs(flatData: list[int]):  # Counts the amount of times a value is repeated
    runs = 1
    check = flatData[0]
    for value in flatData:
        if value == check:
            continue
        else:
            check = value
            runs += 1

    return runs


def to_hex_string(data: list[int]):  # Converts to a hex string
    string = ""
    index = 0

    while index < len(data):
        if data[index] > 15:
            value = data[index]

            while value > 15:
                string += "f"
                if data[index + 1] > 9:
                    if data[index + 1] == 10:
                        string += "a"
                    elif data[index + 1] == 11:
                        string += "b"
                    elif data[index + 1] == 12:
                        string += "c"
                    elif data[index + 1] == 13:
                        string += "d"
                    elif data[index + 1] == 14:
                        string += "e"
                    elif data[index + 1] == 15:
                        string += "f"
                else:
                    string += str(data[index + 1])
                value = value - 15
                if value < 15:
                    if value == 10:
                        string += "a"
                    elif value == 11:
                        string += "b"
                    elif value == 12:
                        string += "c"
                    elif value == 13:
                        string += "d"
                    elif value == 14:
                        string += "e"
                    elif value == 15:
                        string += "f"
                    else:
                        string += str(value)

                    if data[index + 1] == 10:
                        string += "a"
                    elif data[index + 1] == 11:
                        string += "b"
                    elif data[index + 1] == 12:
                        string += "c"
                    elif data[index + 1] == 13:
                        string += "d"
                    elif data[index + 1] == 14:
                        string += "e"
                    elif data[index + 1] == 15:
                        string += "f"
                    else:
                        string += str(data[index + 1])
        else:
            if data[index] == 10:
                string += "a"
            elif data[index] == 11:
                string += "b"
            elif data[index] == 12:
                string += "c"
            elif data[index] == 13:
                string += "d"
            elif data[index] == 14:
                string += "e"
            elif data[index] == 15:
                string += "f"
            else:
                string += str(data[index])

        index += 1

    return string


def encode_rle(flatData: list[int]):  # Encode the flat data into RLE format (into bytes)
    counter = 0
    check = flatData[0]
    data = []
    x = 0

    while x < len(flatData):
        if flatData[x] == check:
            counter += 1
            x += 1
            if x + 1 == len(flatData):
                data.append(counter + 1)
                data.append(check)
                break

        else:
            data.append(counter)
            data.append(check)
            check = flatData[x]
            counter = 1
            x += 1

    return bytes(data)


def get_decoded_length(rle_data: list[int]):  # Returns the length of the decoded RLE data
    index = 0
    total = 0

    while index < len(rle_data):
        total += rle_data[index]
        index += 2

    return total


def decode_rle(rle_data: list[int]):  # Decodes the RLE data into bytes
    flatData = []
    index = 0

    while index < len(rle_data):
        x = 0

        while x < int(rle_data[index]):
            flatData.append(rle_data[index + 1])
            x += 1

        index += 2

    return bytes(flatData)


def string_to_data(data_string: str):  # Converts a string into a byte array
    string_array = []
    index = 0
    value = 0

    while index < len(data_string):
        string_array.append(data_string[index])
        index += 1

    while value < len(string_array):
        if not string_array[value].isnumeric():

            if string_array[value] == "A" or string_array[value] == "a":
                string_array[value] = 10
            elif string_array[value] == "B" or string_array[value] == "b":
                string_array[value] = 11
            elif string_array[value] == "C" or string_array[value] == "c":
                string_array[value] = 12
            elif string_array[value] == "D" or string_array[value] == "d":
                string_array[value] = 13
            elif string_array[value] == "E" or string_array[value] == "e":
                string_array[value] = 14
            elif string_array[value] == "F" or string_array[value] == "f":
                string_array[value] = 15
        else:
            string_array[value] = int(string_array[value])

        value += 1

    return bytes(string_array)


def to_rle_string(rleData: list[int]):  # Converts RLE data into a string
    total_length = ""
    index = 0

    while index < len(rleData):
        value = rleData[index]
        if value > 15:
            while value > 15:
                total_length += "15"
                if 9 < rleData[index + 1] <= 15:
                    if rleData[index + 1] == 10:
                        total_length += "a"
                    elif rleData[index + 1] == 11:
                        total_length += "b"
                    elif rleData[index + 1] == 12:
                        total_length += "c"
                    elif rleData[index + 1] == 13:
                        total_length += "d"
                    elif rleData[index + 1] == 14:
                        total_length += "e"
                    elif rleData[index + 1] == 15:
                        total_length += "f"
                else:
                    total_length += str(rleData[index + 1])

                if not index + 2 == len(rleData):
                    total_length += ":"

                value = value - 15
                if value < 15:
                    total_length += str(value)
                    if 9 < rleData[index + 1] <= 15:
                        if rleData[index + 1] == 10:
                            total_length += "a"
                        elif rleData[index + 1] == 11:
                            total_length += "b"
                        elif rleData[index + 1] == 12:
                            total_length += "c"
                        elif rleData[index + 1] == 13:
                            total_length += "d"
                        elif rleData[index + 1] == 14:
                            total_length += "e"
                        elif rleData[index + 1] == 15:
                            total_length += "f"
                    else:
                        total_length += str(rleData[index + 1])

                    if not index + 2 == len(rleData):
                        total_length += ":"
        else:
            total_length += str(value)
            if 9 < rleData[index + 1] <= 15:
                if rleData[index + 1] == 10:
                    total_length += "a"
                elif rleData[index + 1] == 11:
                    total_length += "b"
                elif rleData[index + 1] == 12:
                    total_length += "c"
                elif rleData[index + 1] == 13:
                    total_length += "d"
                elif rleData[index + 1] == 14:
                    total_length += "e"
                elif rleData[index + 1] == 15:
                    total_length += "f"
            else:
                total_length += str(rleData[index + 1])

            if not index + 2 == len(rleData):
                total_length += ":"

        index += 2

    return total_length


def string_to_rle(rleString: str):  # Converts a string into RLE data
    rleData = []

    pieces = rleString.rsplit(":")

    for value in pieces:
        rleData.append(int(value[0:len(value) - 1]))

        if value[len(value) - 1] == "A" or value[len(value) - 1] == "a":
            rleData.append(10)
        elif value[len(value) - 1] == "B" or value[len(value) - 1] == "b":
            rleData.append(11)
        elif value[len(value) - 1] == "C" or value[len(value) - 1] == "c":
            rleData.append(12)
        elif value[len(value) - 1] == "D" or value[len(value) - 1] == "d":
            rleData.append(13)
        elif value[len(value) - 1] == "E" or value[len(value) - 1] == "e":
            rleData.append(14)
        elif value[len(value) - 1] == "F" or value[len(value) - 1] == "f":
            rleData.append(15)
        else:
            rleData.append(int(value[len(value) - 1]))

    return bytes(rleData)


def print_menu():  # Prints the main menu
    print(
        "\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex "
        "String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. "
        "Display Hex Flat Data\n"
    )


def main():  # Main method
    x = 0
    file_to_display = []

    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.TEST_RAINBOW)
    print("")

    while x < 1:
        print_menu()

        option = input("Select a Menu Option: ").strip()

        if not option.isnumeric():
            print("Error! Invalid input.")
        elif int(option) < 0 or int(option) > 9:
            print("Error! Invalid input.")
        else:
            if int(option) == 0:

                quit()

            elif int(option) == 1:
                file = input("Enter name of file to load: ")

                if str(file) != "testfiles/gator.gfx" or str(file) != "testfiles/lsu.gfx" or str(file) != "testfiles" \
                                                                                                          "/fsu.gfx" \
                        or str(file) != "testfiles/uga.gfx" or str(file) != "testfiles/ut.gfx" or str(file) != "gatoreng.gfx":
                    print("")
                else:
                    file_to_display = list(console_gfx.load_file(file))

            elif int(option) == 2:
                file_to_display = console_gfx.TEST_IMAGE
                print("Test image data loaded.")

            elif int(option) == 3:
                rleString = input("Enter an RLE string to be decoded: ")
                file_to_display = decode_rle(list(string_to_rle(rleString)))

            elif int(option) == 4:
                hexString = str(input("Enter the hex string holding RLE data: "))

                if not hexString.isalnum():
                    print("Error! Some values may be invalid.")
                else:
                    print("RLE decoded length: " + str(get_decoded_length(list(string_to_data(hexString)))))

            elif int(option) == 5:
                flatData = str(input("Enter the hex string holding flat data: "))

                if not flatData.isalnum():
                    print("Error! Some values may be invalid.")
                else:
                    print("Number of runs: " + str(count_runs(list(string_to_data(flatData)))))

            elif int(option) == 6:
                print("Displaying image...")

                try:
                    console_gfx.display_image(file_to_display)
                except IndexError:
                    print("")

            elif int(option) == 7:

                try:
                    to_rle_string(list(encode_rle(file_to_display)))
                except IndexError:
                    print("RLE representation: ")
                else:
                    print("RLE representation: " + to_rle_string(list(encode_rle(file_to_display))))

            elif int(option) == 8:

                try:
                    to_hex_string(list(encode_rle(file_to_display)))
                except IndexError:
                    print("RLE hex values: ")
                else:
                    print("RLE hex values: " + to_hex_string(list(encode_rle(file_to_display))))

            elif int(option) == 9:
                totalFlatValues = ""
                try:
                    for value in file_to_display:
                        if str(value) == "10":
                            totalFlatValues += "a"
                        elif str(value) == "11":
                            totalFlatValues += "b"
                        elif str(value) == "12":
                            totalFlatValues += "c"
                        elif str(value) == "13":
                            totalFlatValues += "d"
                        elif str(value) == "14":
                            totalFlatValues += "e"
                        elif str(value) == "15":
                            totalFlatValues += "f"
                        else:
                            totalFlatValues += str(value)
                except IndexError:
                    print("")
                else:
                    print("Flat hex values: " + totalFlatValues)


if __name__ == '__main__':  # Runs the program
    main()

