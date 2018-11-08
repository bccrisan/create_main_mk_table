import os, json
from os import listdir
from os.path import isfile, join


def generate_main_mk_table():
    """
    """

    base_table = '|      Repository      |                   Last commit               |    Deploy time       | \n' + \
                 '|:--------------------:|:-------------------------------------------:|:--------------------:| \n'
    # data = "Something"
    # for key in data:
    #     row = "|" + commit_number + \
    #           "|" + commiter + \
    #           "|" + message + \
    #           "|" + "[URL](" + url + ")" + \
    #           "|" + date + '\n'
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/repositories") if isfile(join(dir_path + "/repositories", f))]
    print(only_files)

    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]
    print(json_files)

    # Write to md file
    md_file_name = "main_mk_table.md"
    md_file = open(md_file_name, 'w')
    md_file.write(base_table)
    md_file.close()


if __name__ == "__main__":
    generate_main_mk_table()
