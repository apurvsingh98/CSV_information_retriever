from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile


#streamlit run main.py

def main():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = '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'
    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENApipI_API_KEY is set")

    st.set_page_config(page_title="CSV assistant prototype for LivaNova 📈")
    st.header("Intelligent database assistant prototype for LivaNova 📈")


    file = st.file_uploader("upload file", type="csv")
    
    

    if file:
        name = file.name
        file_name = '/Users/apurvsingh/Desktop/LivaNova/' + name
        print(name)
        with tempfile.TemporaryFile() as f: # Create temporary file
            f.write(file.getvalue()) # Save uploaded contents to file
            llm = OpenAI(temperature=0)
            user_input = st.text_input("Question here:")

            agent = create_csv_agent(llm, file_name , verbose=True) # Pass temporary filename to create_csv_agent
            if user_input:
                response = agent.run(user_input)
                st.write(response)

if __name__ == "__main__":
    main()


# Questions: 
# What is this datset about?
# Which was the worst year for Bangladesh with Men mortality rate. Give the worst 2 years
# Which were the top worst years for Bangladesh with Men mortality rate?
# How does the rate of HIV/AIDS infections correlate with health expenditure, life expectancy, and adult mortality rates? Can we observe any patterns?
# What is the correlation value between immunization coverage for diseases like Polio and life expectancy and adult mortality in Afghanistan?
# How does the income composition of resources impact various health indicators over time? Can we observe a trend where higher income composition correlates with better health outcomes?
