from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App
st.set_page_config(page_title="SQL Query Retrieval", page_icon="📊")
st.title("Gemini App to Retrieve SQL Data")
st.write("This application converts your English questions into SQL queries and retrieves data from the database.")

# Input for the question
question = st.text_input("Enter your question about the STUDENT database:", key="input")

# Submit button
submit = st.button("Submit")

# If submit is clicked
if submit:
    if question:
        # Get SQL query from Gemini model
        response = get_gemini_response(question, prompt)

        # Retrieve results from the database
        results = read_sql_query(response, "student.db")

        # Display results
        if results:
            st.subheader("Query Result:")
            for row in results:
                st.write(row)
        else:
            st.warning("No results found for the given query.")
    else:
        st.error("Please enter a question.")

# Footer section
st.markdown("---")
