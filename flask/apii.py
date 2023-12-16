from flask import Flask, jsonify, request , send_file
import pandas as pd
from model import predict_function , csv_to_model ,pie_chart , cluster_analysis , scatter_plot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/process_form', methods=['POST',])
def process_form():
    # Get the form data from the request
    form_data = request.json

    age = int(form_data['age'])
    income= int(form_data['annualIncome'])
    score = int(form_data['spendScore'])
    print(form_data)

    #Calling Prediction Function
    result = predict_function(age , income , score)
    print(result)

    # Return a JSON response
    response = result
    return (response)


@app.route('/upload', methods=['POST',])

def upload_file():
    # Get the form data from POST request
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'No file selected.', 400
        if file:
            df = pd.read_csv(file)
            # Calling Function csv_to_model , to load and train model
            data = csv_to_model(df)
            analysis = cluster_analysis(data)
            #Calling function pie_chart , to generate pie chart
            img = pie_chart(data)
            # Calling function scatter_plot , to generate scatter plot
            scatter_img = scatter_plot(df)
            response = analysis
            return jsonify(response)
    return "Done "



@app.route('/image_link', methods=['GET',])
def get_image_link():
    image_link = 'pie_chart.png'
    send = send_file(image_link, mimetype='image/png')
    return send



@app.route('/scatter_plot', methods=['GET',])
def get_image_link_scatter_plot():
    image_link = 'scatterplot.png'
    send = send_file(image_link, mimetype='image/png')
    return send


if __name__ == '__main__':
    app.run(debug=True)


#pip install flask_cors
#pip install numpy 
#pip install flask
