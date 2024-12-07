import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
from sympy.physics.units import temperature

load_dotenv()
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "employees", "portfolio-techstacks.csv")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

urls = ["https://example.com/careers"]

loader = WebBaseLoader(urls)
document = loader.load()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(model_name="llama-3.1-70b-versatile")
        self.email_llm = ChatGroq(model_name = "llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
             ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Roman, the CEO of TechSolutions Inc., a leading IT consulting and software development company. TechSolutions specializes in delivering innovative technology solutions tailored to enhance business operations and drive growth.
            With years of experience, the company has empowered various businesses through scalable, cost-effective solutions that optimize processes and improve efficiency.
            
            Your job is to write a cold email to the client regarding the job mentioned above, emphasizing TechSolutions' capabilities in addressing their needs. 
            Additionally, include the most relevant projects from the following portfolio links to demonstrate TechSolutions' expertise: {link_list}. 
            Remember, you are Roman, the CEO of TechSolutions Inc. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.email_llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


obj = Chain()
print(obj.extract_jobs(document))
