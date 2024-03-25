def decode_pyramid(message_file):
    # Opens the file, reads lines into a dictionary (keys: numbers and values: words)
    map = {}
    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.strip().split(' ', 1)
            map[int(number)] = word

    # Find the numbers needed at the end of each line
    end_numbers = []
    current_line_length = 1
    current_number = 1
    while current_number in map:
        end_numbers.append(current_number)
        current_line_length += 1
        current_number += current_line_length

    # Construct  decoded message with words at end line numbers
    decoded_message = ''
    for number in end_numbers:
        if decoded_message:  # If not empty, add a space before the next word
            decoded_message += ' '
        decoded_message += map[number]
    
    return decoded_message
    
message_file_path = 'coding_qual_input.txt'
decoded_message = decode_pyramid(message_file_path)
print(decoded_message)
