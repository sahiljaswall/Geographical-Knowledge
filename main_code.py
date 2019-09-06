from flask import Flask
from flask import request
from flask import render_template
import csv

app = Flask(__name__)


# attach HTML Document
@app.route('/')
def page_html():
    return render_template('input_doc.html')

@app.route('/', methods=['GET', 'POST'])
def page_work():
    if request.method == 'POST':
        input_country = request.form['html_input']
        updated_country = list(input_country.split(' '))
        for row in range(len(updated_country)):
            if (updated_country[row] == 'and'
                    or updated_country[row] == 'o'
                    or updated_country[row] == 'of'):
                continue
            else:
                updated_country[row] = updated_country[row].capitalize()
        final_country = " ".join(updated_country)
        with open('raw_data.csv') as newFile:
            data = csv.reader(newFile, delimiter=',')
            for row in data:
                if row[0] == final_country:
                    capital = row[1]
                    return render_template('input_doc.html', re=capital)

            return render_template('input_doc.html', re='Invalid Country / Spelling Error')


if __name__ == '__main__':
    app.run(debug=True)
