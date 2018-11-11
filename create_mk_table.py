import os, json
from os import listdir
from os.path import isfile, join
from pprint import pprint
import  datetime

def hg_timestamps_handler(timestamp, timezone):
    """
    This function handles the mercurial timestamps so that all of the modifications to be traceable in time, in
    concordance to one
    another and returns the date-time format.
    Part of Mercurial Wrapper
    Example :
        print(handle_timestamps("1499225169.0", "-43200"))
    Output:
        07-05-2017 15:26:09
    :param timestamp: Timestamp in unix systems (an unique time represented in how many seconds past a certain event)
    :param timezone: Timezone of the timestamp
    :return: Returns "YYYY-MM-DD HH:MM:SS"
    """
    if "-" in timezone:
        ts = int(timestamp[:-2]) - int(timezone)
    else:
        ts = int(timestamp[:-2]) + int(timezone)
    return datetime.utcfromtimestamp(ts).strftime("%m-%d-%Y %H:%M:%S")


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

    # for f in json_files:
    #     json_test = json.load("repositories/" + f)
    #     pprint(json_test)

    json_data = open("repositories/Mozharness.json").read()

    data = json.loads(json_data)
    pprint(data["node"])
    for test in data["changesets"]:
        print("Mozharness")
        print(test["desc"])
        data_comitului = test["date"][:1]
        tdz = test["date"][1:]
        print(str(data_comitului) + " " + str(tdz))

        break

    # Write to md file
    md_file_name = "main_mk_table.md"
    md_file = open(md_file_name, 'w')
    md_file.write(base_table)
    md_file.close()


if __name__ == "__main__":
    generate_main_mk_table()
