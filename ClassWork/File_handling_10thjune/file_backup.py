import os

source_file = input("Enter Source File Name : ")
destination_file = input("Enter Destination File Name : ")

if os.path.exists(source_file):

    # Read source file
    source = open(source_file, "r")
    content = source.read()
    source.close()

    # Write into destination file
    destination = open(destination_file, "w")
    destination.write(content)
    destination.close()

    print("\nFile copied successfully.")
    print("All contents from '{}' have been copied to '{}'.".format(
        source_file, destination_file))

else:
    print("Source file does not exist.")