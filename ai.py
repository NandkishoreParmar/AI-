


import google.generativeai as genai

api_key = "AIzaSyAYEhjbyYTQITrav1wzB161oYwvYMgYJlg";
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("you are creating a  shayri for me mirzapur season 3 in jail in front of lala");
print(response.text)