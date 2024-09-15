
import requests

url = 'http://localhost:9696/predict'

customer = {
	 "gender": "male",
	 "seniorcitizen": 1,
	 "partner": "yes",
	 "dependents": "yes",
	 "phoneservice": "yes",
	 "multiplelines": "no",
	 "internetservice": "fiber_optic",
	 "onlinesecurity": "no",
	 "onlinebackup": "yes",
	 "deviceprotection": "no",
	 "techsupport": "no",
	 "streamingtv": "yes",
	 "streamingmovies": "yes",
	 "contract": "month-to-month",
	 "paperlessbilling": "yes",
	 "paymentmethod": "mailed_check",
	 "tenure": 32,
	 "monthlycharges": 93.95,
	 "totalcharges": 2861.45
}

response = requests.post(url, json=customer).json()

print(response)

if(response['churn']==True):
    print("Send promotion email to this customer")

else:
    print("Do not send email to this customer")

