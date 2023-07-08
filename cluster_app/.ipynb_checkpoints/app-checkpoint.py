from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hs_codes = request.form.get('hs_codes')
        hs_codes = [int(i) for i in hs_codes.split(',')]  # assuming input is comma separated

        # Read the excel file
        
        #df = pd.read_excel('districts.xlsx')

        # Logic here, now that we have got both datasets and ITC HS needed
        
        filtered_df = None
        #filtered_df = df[df['hs_code'].isin(hs_codes)]

        # Perform your calculations here with the filtered data.
        
        
        # Let's assume you have a function that returns a list of dicts, 
        # with each dict having 'name', 'eci' and 'gain' keys.
        
        results = your_calculations(filtered_df)

        return render_template('index.html', results=results)

    return render_template('index.html')

def your_calculations(df):
    # TODO: implement your calculations here
    # return a list of dicts, for example:
    return [{'rank': "1", 'name': 'District1', 'eci': 1.2, 'gain': 0.1}, {'rank': '2', 'name': 'District2', 'eci': 1.3, 'gain': 0.2}]
    #pass

if __name__ == "__main__":
    app.run(debug=True)
