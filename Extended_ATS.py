
import os

import google.generativeai as genai
import PyPDF2
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model=genai.GenerativeModel(model_name='gemini-1.5-flash')
    response=model.generate_content([input])
    return response.text

def input_pdf_text(uploaded_file):
    if uploaded_file is not None:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += str(page.extract_text())
        return text
    else:
        raise FileNotFoundError('No file uploaded')

        
st.set_page_config(page_title='ATS Resume Expert')

st.header('ATS Tracking System')
jd=st.text_area('Job Description:',key='input')
uploaded_file=st.file_uploader('Upload Your Resume (PDF)...',type=['pdf'])

if uploaded_file is not None:
    st.write('PDF Uploaded Successfully')

submit1=st.button('Analyze')

input1 = '''
Act like a skilled and experienced ATS (Applicant Tracking System) with a deep understanding of tech fields such as software engineering, data science, data analytics, and big data engineering.

Your task is to evaluate the resume based on the job description.

The job market is highly competitive, so provide the best suggestions to improve the resume.

Assign a percentage match based on the JD and identify missing keywords with high accuracy.

Resume:
{text}

Job Description:
{jd}

Return the response in this format:
{{"JD Match":"% of matching", "Missing Keyword": [mention all missing keywords], "Profile Summary": "give a final summary"}}.
'''



if submit1:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file) 
        prompt = input1.format(text=text, jd=jd)
        response=get_gemini_response(prompt)
        st.subheader("The response is,")
        st.write(response)

    else:
        st.write("Please Upload the resume")








