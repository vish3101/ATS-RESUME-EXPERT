# ATS Resume Matcher using Gemini 1.5 Flash

This project is an AI-powered Applicant Tracking System (ATS) that uses Google’s Gemini 1.5 Flash model to analyze resumes against job descriptions and provide detailed feedback. The tool helps job seekers understand how well their resume matches a specific role and suggests improvements.

## Features

- **Two Resume Processing Methods**:
  1. **Bytes-based PDF Extraction**: Used in `app.py`, where resume files are read as raw bytes and converted to text for compatibility with scanned or irregular PDFs.
  2. **Direct Text Extraction**: Used in `extended_ats.py`, where `PyPDF2` extracts text directly from standard PDF resumes.

- **Four Functional Options (via Streamlit buttons)**:
  - **Tell Me About the Resume**: Gives an HR-style analysis of strengths and weaknesses.
  - **Percentage Match**: Returns a match score, strong keywords, and missing ones.
  - **What Are the Keywords That Are Missing?**: Lists important keywords in the JD not found in the resume.
  - **How Can I Improvise My Skills?**: Provides improvement suggestions for career growth.

## Technologies & Libraries Used

- `streamlit` – for the web interface
- `python-dotenv` – to manage environment variables securely
- `google-generativeai` – to access the Gemini 1.5 Flash API
- `pdf2image` – for optional PDF page rendering if needed
- `PyPDF2` – for direct text extraction from PDF resumes

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ats-gemini-project
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install streamlit python-dotenv google-generativeai pdf2image PyPDF2
```

### 4. Set up the `.env` file

Create a `.env` file in the project root and add your Gemini API key:

```
GOOGLE_API_KEY=your_google_generativeai_api_key
```

### 5. Run the App

For bytes-based version:

```bash
streamlit run app.py
```

For direct-text version:

```bash
streamlit run extended_ats.py
```

## File Structure

```
ats-gemini-project/
├── app.py                # Resume parsed via raw bytes
├── extended_ats.py       # Resume parsed via direct PyPDF2 text extraction
├── .env                  # API key file (not committed)
└── README.md             # Project overview and setup
```

## Goal

To provide a smart ATS system capable of analyzing resumes and offering match percentages, keyword insights, and professional development suggestions using GenAI.
