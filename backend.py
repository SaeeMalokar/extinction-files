from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset with error handling for bad lines
try:
    data = pd.read_csv(r'C:\Users\Admin\Downloads\microproject\jaanwar.csv', on_bad_lines='skip')
except pd.errors.ParserError as e:
    print("Error reading CSV:", e)
    data = pd.DataFrame()  # Load an empty DataFrame if the file cannot be parsed

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the mammals route
@app.route('/mammals')
def mammals():
    # Filter the data for mammals (assuming there's a column named 'type' in your dataset)
    mammals_data = data[data['type'] == 'mammal'].to_dict(orient='records')
    return render_template('mammals.html', mammals=mammals_data)

if __name__ == '__main__':
    app.run(debug=True)
