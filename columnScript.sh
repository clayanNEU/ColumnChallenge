#!/bin/bash

# Get path to the CSV
csv_file="Employee_Information.csv"

output_file="parsed_data.txt"
log_file="script.log"

# help log message
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$log_file"
}

# Function to read and parse CSV
parse_csv() {
    # we need to check that file exists
    if [ ! -f "$csv_file" ]; then
        log_message "CSV not found"
        return 1
    fi


    # write to output
    > "$output_file"
    # if found read line by line, Internal Field Separator
    while IFS=',' read -r firstname lastname department; do
        # Skip the header
        if [ "$firstname" != "First Name" ]; then

            # check for empty fields
            if [ -z "$firstname" ] || [ -z "$lastname" ] || [ -z "$department" ]; then
                log_message "Error: Missing data in one of the fields"
                continue
            fi

            # validate the data
            if ! [[ $firstname =~ ^[A-Za-z]+$ ]] || ! [[ $lastname =~ ^[A-Za-z]+$ ]]; then
                log_message "Error: Invalid data or characters in name fields"
                continue
            fi

            # get the first character of the first name
            first_char=$(echo $firstname | cut -c 1)
            # make the email address
            email="${first_char}${lastname}@column30.com"
            # clean the email by converting to lowercase
            email=$(echo "$email" | tr '[:upper:]' '[:lower:]')
            echo "$firstname,$lastname,$email,$department" >> "$output_file"
        fi
    done < "$csv_file"

    log_message "CSV parsing completed. Output written to $output_file"
}

parse_csv