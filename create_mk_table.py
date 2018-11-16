import os, json
import re
import time
from os import listdir
from os.path import isfile, join
from datetime import datetime
from pprint import pprint


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
    """
    This function takes a file that clears the content and output's a base table header for a markdown file.
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    f = open(file_name, 'w')
    base_table = '|      Repository      |                   Last commit               |    Deploy time       | \n' + \
                 '|:--------------------:|:-------------------------------------------:|:--------------------:| \n'
    f.write(base_table)
    f.close()


def write_main_mk_table(file_name, repository, last_commit, deploy_time):
    """
    This function opens a file (that file should be already created and should contain a markdown table header) and
    appends to it a row that will contain the repository, the last commit and the deploy time.
    :param file_name: Name of the file in which the content is appended. (should also contain the path)
    :param repository: Repository name for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element of the table
    :param deploy_time: Time and Time designator used as the 3rd element of the table
    :return:
    """
    row = "|" + repository + \
          "|" + last_commit + \
          "|" + deploy_time + \
          "|" + '\n'
    write_file = open(file_name, "a")
    write_file.write(row)


def extract_hg_json(json_files):
    """
    Function that handles and adds mercurial content into the markdown table .
    The function starts looking into the /repositories folder after json files.
    Once those are found, and stored into list and after that we get every element from the list (each element being a
    json file name at this point) and used to open that file, and grab the commit description, commit date and the
    repository name that luckly is the same as the file name.
    The function also generates the github_base_link that is used as a link in the markdown table.
    :return:
    """
    for f in json_files:
        # print(f)
        file_path = "hg_files/" + f
        # read_from_json = json.load(file_path.read())
        # print(read_from_json)
        with open(file_path) as json_files:
            data = json.load(json_files)
            # pprint(data)
            github_base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/"
            repository_name = "[" + f.rstrip().replace(".json", "") + "]" + "(" + github_base_link + \
                              f.rstrip().replace(" ", "%20") + ")"

            for test in data["changesets"]:
                commit_description = test["desc"]
                replaced_commit_description = re.sub("[\n]", " ", commit_description)
                commit_date = test["date"][:1]
                tdz = test["date"][1:]
                test = str(commit_date).strip("[]")
                time_designator = str(tdz).strip("[]")
                data_push = hg_timestamps_handler(test, time_designator)
                replaced_commit_description = str(replaced_commit_description)
                write_main_mk_table("main_mk_table.md", repository_name, replaced_commit_description, data_push)
                # We are braking this for loop since we got the last commit.
                break


def extract_github_data(json_files):
    for f in json_files:
        # print(f)
        file_path = "git_files/" + f
        # read_from_json = json.load(file_path.read())
        # print(read_from_json)
        with open(file_path) as json_files:
            data = json.load(json_files)
            # pprint(data)
            github_base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/"
            repository_name = "[" + f.rstrip().replace(".json", "") + "]" + "(" + github_base_link + \
                              f.rstrip().replace(" ", "%20") + ")"
            for test in data["1"]:
                print(test)
                # commit_description = test[""]
                # print(commit_description)
                # replaced_commit_description = re.sub("[\n]", " ", commit_description)


                # write_main_mk_table("main_mk_table.md", repository_name, replaced_commit_description, data_push)

                # We are braking this for loop since we got the last commit.
                # break


def generate_main_mk_table():
    """
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    # hg_only_files = [f for f in listdir(dir_path + "/hg_files") if isfile(join(dir_path + "/hg_files", f))]
    # # print(only_files)
    #
    # # Pass filter only the ".json" objects
    # hg_json_files = [jf for jf in hg_only_files if ".json" in jf]
    # # print(json_files)
    # extract_hg_json(hg_json_files)

    git_only_files = [f for f in listdir(dir_path + "/git_files") if isfile(join(dir_path + "/git_files", f))]
    git_json_files = [jf for jf in git_only_files if ".json" in jf]
    extract_github_data(git_json_files)


if __name__ == "__main__":
    start_time = time.time()
    clear_file("main_mk_table.md")
    generate_main_mk_table()
    print("--- %s seconds ---" % (time.time() - start_time))