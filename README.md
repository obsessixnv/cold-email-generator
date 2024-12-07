
# Cold Email Generator

## Overview

The **Cold Email Generator** is an AI-driven tool that automates the creation of personalized cold emails, especially for job applications. By leveraging advanced language models like **Llama 3.1** and frameworks such as **LangChain** and **Streamlit**, this application allows users to generate effective and tailored cold emails based on job listings extracted from a company’s career page.

## Features

- **Job Listing Extraction**: Input a company's career page URL to automatically scrape job listings.
- **Personalized Cold Emails**: Generate professional and personalized cold emails based on job descriptions.
- **Tech Stack Integration**: Query relevant portfolio or project links from a vector database to enhance the email content.
- **Generative AI**: Utilizes Llama 3.1 for high-quality, engaging email generation.
- **Interactive UI**: Built with Streamlit for a seamless user experience.

## Tech Stack

- **Python**: Core language for development.
- **Streamlit**: Framework for creating the web interface.
- **ChromaDB**: Stores and queries tech stack links based on relevance.
- **Groq API**: Provides AI model interactions.
- **Llama 3.1**: A powerful generative AI model for text generation.
- **LangChain**: Integrates various models and tools for enhanced performance.

## Installation & Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/obsessixnv/cold-email-generator.git
    cd cold-email-generator
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name cold-email-env python=3.8
    conda activate cold-email-env
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file in the project root and add your API key:
      ```bash
      GROQ_API_KEY=your_groq_api_key_here
      ```

5. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

- After running the application, you can input the URL of a company's careers page.
- The tool will extract available job listings, and based on the description, it will generate personalized cold emails.
- You can further customize the email content with relevant portfolio or project links from the database.

## Contributing

Feel free to open issues or submit pull requests if you wish to contribute. Make sure to follow the established code style for smooth collaboration.
