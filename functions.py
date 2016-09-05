from bs4 import BeautifulSoup
import csv


def process_html(input_file, output_file):
    filetext = read_file(input_file)
    soup = BeautifulSoup(filetext, 'html.parser')
    divs = soup.findAll("div", {"class": "cap-section-row-circle-outer"})
    data_content = []
    for item in divs:
        #data_content.append(item["data-content"])
        data_content.append((item["data-content"]).encode('utf-8', 'ignore'))

    i = 0
    while data_content:
        write_csv(output_file, data_content[0:5])
        data_content = data_content[5:]
        i = i +1
        print i


def read_file(my_file):
    f = open(my_file)
    filetext = f.read()
    f.close()
    return filetext


def write_txt(output, data):
    thefile = open(output, 'wa')
    for item in data:
        thefile.write(item)
    print "wrote to text file"

def write_csv(output, data):
    fp = open(output, 'a')
    a = csv.writer(fp)
    a.writerow(data)
    #a.writerow('\n')
    fp.close()
    print "wrote to csv file"


