#!/usr/bin/env python
import functions


def main():
    config = {}
    execfile("./ignore_files/project.conf", config)
    # print config["value1"]

    my_file = "/Users/bethnakamura/Projects/html_data_scraper/ignore_files/ge-sr-software-capabilty.txt"
    print functions.read_file(my_file)
    print "Main function ran"


if __name__ == "__main__":
    main()
