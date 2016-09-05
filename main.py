#!/usr/bin/env python
import functions


def main():
    config = {}
    execfile("./ignore_files/project.conf", config)

    functions.process_html(''.join(config["input"]).encode('utf-8').strip(), ''.join(config["output"]).encode('utf-8').strip())
    print "Main function ran"


if __name__ == "__main__":
    main()
