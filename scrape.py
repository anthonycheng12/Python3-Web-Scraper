import csv
import scrape_func

startNum = 0
target_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'

csv_header = scrape_func.getRow("ID", "Name", "Date", "Body")
outfile = open("./mikejordan.csv", "w")
writer = csv.writer(outfile)
writer.writerow([csv_header[0], csv_header[1], csv_header[2], csv_header[3]])
scrape_func.scrape(startNum, writer, target_url)
