import requests
import csv
import os
from bs4 import BeautifulSoup

url = "https://www.tfrrs.org/results/xc/21234/NCAA_Division_I_Cross_Country_Championships"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table_bodies = soup.find_all("tbody")

body_list = []
for table_body in table_bodies:
    row_list =[]
    rows = table_body.find_all("tr")
    for row in rows:
        elements_list = []
        cells = row.find_all("td")
        for cell in cells:
            elements_list.append(cell.text.replace('\n',''))
            #print(cell.text)
        row_list.append(elements_list)
    body_list.append(row_list)
    
filtered_list = []

for p in body_list[3]:
    name = p[1]
    school = p[3]
    score = p[0]
    if score != "0":
        filtered_list.append([name, school, score])
    
folder_path = r'C:\Users\ragon\OneDrive\Desktop\learning_python'
csv_filename = 'filtered_list.csv'
csv_file_path = os.path.join(folder_path, csv_filename)

csv_filename = 'filtered_list.csv'
with open(csv_filename,  'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','School', 'Score'])
    writer.writerows(filtered_list)

print(f"CSV file '{csv_filename}' has been created.")



    









