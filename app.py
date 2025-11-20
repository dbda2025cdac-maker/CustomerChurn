import pandas as pd
from flask import Flask, render_template,request
import pickle


#Initialize the flask App
app = Flask(__name__)

#default page of the web-app
@app.route('/')
def loadPage():
    return render_template('testing.html', query="")

@app.route('/', methods=['POST'])
def prediction():
    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']

    modelRandomForest = pickle.load(open('random_forest_model.pkl', 'rb'))
    modelDecisionTree = pickle.load(open('decision_tree_model.pkl', 'rb'))


    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19]]
    
    new_df = pd.DataFrame(data, columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 
                                           'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
                                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                           'PaymentMethod', 'tenure'])
    


    columns = ['SeniorCitizen','Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
            'PaperlessBilling']
    
    for col in columns:
        # new_df[col].replace({'Yes': 1, 'No': 0}, inplace = True)
        new_df.loc[new_df[col] == 'Yes', col] = 1
        new_df.loc[new_df[col] == 'No', col] = 0
        new_df.loc[new_df[col] == 'No phone service', col] = 0
        new_df.loc[new_df[col] == 'No internet service', col] = 0

    new_df.loc[new_df['gender'] == 'Female', 'gender'] = 1
    new_df.loc[new_df['gender'] == 'Male', 'gender'] = 0
    # new_df['gender'].replace({'Female': 1, 'Male': 0}, inplace = True)
    
    if (inputQuery9 == 'DSL'):
        new_df['InternetService_Fiber optic'] = 0
        new_df['InternetService_No'] = 0
    
    if (inputQuery9 == 'Fiber optic'):
        new_df['InternetService_DSL'] = 0
        new_df['InternetService_No'] = 0

    if (inputQuery9 == 'No'):
        new_df['InternetService_DSL'] = 0
        new_df['InternetService_Fiber optic'] = 0

    if (inputQuery16 == 'Month-to-month'):
        new_df['Contract_One year'] = 0
        new_df['Contract_Two year'] = 0

    if (inputQuery16 == 'One year'):
        new_df['Contract_Two year'] = 0
        new_df['Contract_Month-to-month'] = 0

    if (inputQuery16 == 'Two year'):
        new_df['Contract_Month-to-month'] = 0
        new_df['Contract_One year'] = 0

    if (inputQuery18 == 'Bank transfer (automatic)'):
        new_df['PaymentMethod_Credit card (automatic)'] = 0
        new_df['PaymentMethod_Electronic check'] = 0
        new_df['PaymentMethod_Mailed check'] = 0

    if (inputQuery18 == 'Credit card (automatic)'):
        new_df['PaymentMethod_Bank transfer (automatic)'] = 0
        new_df['PaymentMethod_Electronic check'] = 0
        new_df['PaymentMethod_Mailed check'] = 0

    if (inputQuery18 == 'Electronic check'):
        new_df['PaymentMethod_Bank transfer (automatic)'] = 0
        new_df['PaymentMethod_Credit card (automatic)'] = 0
        new_df['PaymentMethod_Mailed check'] = 0

    if (inputQuery18 == 'Mailed check'):
        new_df['PaymentMethod_Bank transfer (automatic)'] = 0
        new_df['PaymentMethod_Credit card (automatic)'] = 0
        new_df['PaymentMethod_Electronic check'] = 0


    df1 = pd.get_dummies(data = new_df, columns = ['InternetService','Contract','PaymentMethod'], dtype='int')
    


    column = ['SeniorCitizen', 'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'PaperlessBilling']
    
    for cols in column:
        df1[cols] = df1[cols].astype('int64')


    colu = ['MonthlyCharges', 'TotalCharges', 'tenure']

    for cols in colu:
        df1[cols] = df1[cols].astype('float')

    colum_dummies = ['InternetService_DSL', 'InternetService_Fiber optic',
       'InternetService_No', 'Contract_Month-to-month', 'Contract_One year',
       'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    
    for cols in colum_dummies:
        df1[cols] = df1[cols].astype('uint8')

    df1.loc[:, 'MonthlyCharges'] = round((float(df1.loc[0]['MonthlyCharges']) - 18.25)/100.5, 6)
    df1.loc[:, 'TotalCharges'] = round((float(df1.loc[0]['TotalCharges']) - 18.8)/8666, 6)
    df1.loc[:, 'tenure'] = round((float(df1.loc[0]['tenure'])-1.0)/71.0, 6)

    column_order = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
       'InternetService_DSL', 'InternetService_Fiber optic',
       'InternetService_No', 'Contract_Month-to-month', 'Contract_One year',
       'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    
    df1 = df1[column_order]
    

    outputRF = modelRandomForest.predict([df1.loc[0]])

    outputDF = modelDecisionTree.predict([df1.loc[0]])


    if outputRF == 1:
        oRF = 1
    else:
        oRF = -1

    if outputDF == 1:
        oDF = 1
    else:
        oDF = -1

    return render_template('testing.html', outputRF=oRF, outputDF = oDF)

app.run(debug=False)
