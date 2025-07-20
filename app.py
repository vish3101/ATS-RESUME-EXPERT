import base64
import io
import os

import google.generativeai as genai
import pdf2image
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel(model_name='gemini-1.5-flash')
    response=model.generate_content([input,pdf_content,prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        image = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = image[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_part = {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        }
        return pdf_part  # not a list anymore
    else:
        raise FileNotFoundError('No file uploaded')
        
st.set_page_config(page_title='ATS Resume Expert')

st.header('ATS Tracking System')
input=input_text=st.text_area('Job Description:',key='input')
uploaded_file=st.file_uploader('Upload Your Resume (PDF)...',type=['pdf'])

if uploaded_file is not None:
    st.write('PDF Uploaded Successfully')

submit1=st.button('Tell Me About the Resume')

submit2=st.button('How can I Improvise my skills')

submit3=st.button('What are the keywords that are missing?')

submit4=st.button('percentage match')

input1='''
You are an experinced HR with Tech Experince in the field of any one job role like data science or Full stack or web development or big data engineer or DEVOPS or data analyst.
your task is to review the provide resume againts the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns  the role.
Highlight the stregths and weakness of the applicant in relation to the specified job requirements.'''

input4='''
You are an ATS (Applicant Tracking System) scanner with deep understanding of data science, Full stack, web development, big data engineer, DEVOPS, data analyst. and deep ATS
Functionality, your task is to evaluate the resume against the provided job description.give me the percentage match the resume matches
the job description.First th output should come as percentage and then strong keyword and then keywords missing.
'''

input3 = '''
You are an AI-powered resume optimization tool specialized in identifying missing keywords when comparing resumes with job descriptions.
Your task is to analyze the resume and job description and return a list of important keywords (technical skills, soft skills, tools, role-specific terms) that are present in the job description but missing in the resume.
Do not suggest keywords that are already covered in the resume. Also, avoid generic advice — only list relevant, role-specific missing keywords.
'''

input2 = '''
You are an experienced career coach with expertise in technical roles such as data science, web development, full-stack development, big data engineering, DEVOPS, and data analytics. 
Review the provided resume and suggest personalized ways the candidate can improve their skills and profile. 
Focus on relevant certifications, technical tools, programming languages, project experiences, and soft skills they should consider learning or enhancing to boost their employability in their targeted role.
'''


if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file) 
        response=get_gemini_response(input1,pdf_content,input_text)
        st.subheader("The response is,")
        st.write(response)

    else:
        st.write("Please Upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file) 
        response=get_gemini_response(input2,pdf_content,input_text)
        st.subheader("The response is,")
        st.write(response)

    else:
        st.write("Please Upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file) 
        response=get_gemini_response(input3,pdf_content,input_text)
        st.subheader("The response is,")
        st.write(response)

    else:
        st.write("Please Upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file) 
        response=get_gemini_response(input4,pdf_content,input_text)
        st.subheader("The response is,")
        st.write(response)

    else:
        st.write("Please Upload the resume")        









