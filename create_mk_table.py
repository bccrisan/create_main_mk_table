import os, json
from os import listdir
from os.path import isfile, join
from pprint import pprint
from datetime import datetime


def hg_timestamps_handler(timestamp, timezone):
    """
    This function handles the mercurial timestamps so that all of the modifications to be traceable in time, in
    concordance to one
    another and returns the date-time format.
    Part of Mercurial Wrapper
    Example :
        print(hg_timestamps_handler("1499225169.0", "-43200"))
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


def clear_file(file_name):
    f = open(file_name, 'w')
    base_table = '|      Repository      |                   Last commit               |    Deploy time       | \n' + \
                 '|:--------------------:|:-------------------------------------------:|:--------------------:| \n'
    f.write(base_table)
    f.close()


def write_main_mk_table(file_name, repository, last_commit, deploy_time):

    row = "|" + repository + \
          "|" + last_commit + \
          "|" + deploy_time + \
          "|" + '\n'
    write_file = open(file_name, "a")
    write_file.write(row)


def generate_main_mk_table():
    """
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/repositories") if isfile(join(dir_path + "/repositories", f))]
    # print(only_files)

    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]
    # print(json_files)

    for f in json_files:
        # print(f)
        file_path = "repositories/" + f
        # read_from_json = json.load(file_path.read())
        # print(read_from_json)
        with open(file_path) as json_files:
            data = json.load(json_files)
            # pprint(data)
            github_base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/repositories/"
            repository_name = "[" + f.rstrip().replace(".json", "") + "]" + "(" + github_base_link + f + ")"
            for test in data["changesets"]:
                commit_description = test["desc"]
                commit_description = commit_description.rstrip('\r\n').replace('\n', '')
                commit_date = test["date"][:1]
                tdz = test["date"][1:]
                test = str(commit_date).strip("[]")
                time_designator = str(tdz).strip("[]")
                data_push = hg_timestamps_handler(test, time_designator)
                commit_description = str(commit_description)
                write_main_mk_table("main_mk_table.md", repository_name, commit_description, data_push)
                break


if __name__ == "__main__":
    clear_file("main_mk_table.md")
    generate_main_mk_table()



