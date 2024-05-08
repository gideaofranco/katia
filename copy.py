import csv

QTD_WORDS = 60
FIELDS = ['x-id', 'tema', 'hashtags', 'cgpa']

with open('twitter-100-linhas.csv', 'r') as readFile:
    with open('twitter-new.csv', 'w') as writeFile:
        reader = csv.reader(readFile)
        writer = csv.writer(writeFile)
        writer.writerow(FIELDS)
        for readRow in reader:
            text_cel = readRow[7]
            words_count = text_cel.count(" ") + 1
            if (words_count >=  QTD_WORDS):

                tema_cel = readRow[0]
                hashtags_cel = readRow[1]
                xid_cel = readRow[2]
                links_json_cel = readRow[4]

                rowData =[]
                rowData.append("value1")
                rowData.append("value2")
                rowData.append("value3")
                rowData.append("value4")

            writer.writerow(rowData)
