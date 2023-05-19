from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def home():
    csv_filename = r'C:\Users\ragon\filtered_list.csv'
    csv_data = []
    with open(csv_filename, 'r') as file:
        csv_reader = csv.reader(file)
        csv_data = list(csv_reader)

    return render_template('fantasy_practice_page.html', csv_data=csv_data, bigballs='fantasy XC for brokies')


if __name__ == '__main__':
    app.run()
