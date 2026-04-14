📰 News Headlines Web Scraper
=============================

A Python-based **web scraping project** that extracts top news headlines from the BBC News website and saves them in structured formats like .txt or .csv.

📌 Project Overview
-------------------

This project demonstrates how to:

*   Fetch real-time data from a website
    
*   Parse HTML content
    
*   Extract useful information (headlines)
    
*   Store data in files for further use
    

The scraper collects **top headlines from BBC News**, cleans them, and allows users to save them in a preferred format.

🚀 Features
-----------

*   🌐 **Live Data Fetching**
    
    *   Extracts real-time headlines from BBC News
        
*   🧠 **Data Cleaning**
    
    *   Removes empty and irrelevant text
        
    *   Filters meaningful headlines
        
*   🔁 **Duplicate Removal**
    
    *   Ensures unique headlines only
        
*   🎯 **User Input Control**
    
    *   Choose how many headlines to display
        
*   🕒 **Timestamp Support**
    
    *   Saves date & time with each headline
        
*   💾 **Multiple Save Formats**
    
    *   Save as .txt file
        
    *   Save as .csv file
        
*   ⚠️ **Error Handling**
    
    *   Handles invalid user input gracefully
        

🛠️ Technologies Used
---------------------

*   Python
    
*   requests (for HTTP requests)
    
*   BeautifulSoup (for HTML parsing)
    
*   csv (for structured data storage)
    
*   datetime (for timestamps)
    

🖥️ How to Run
--------------

### 1\. Install required libraries

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install requests beautifulsoup4   `

### 2\. Navigate to project folder

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd news-scraper   `

### 3\. Run the script

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python scraper.py   `

🎮 How to Use
-------------

1.  How many headlines you want? 5
    
2.  Save as (1 = txt, 2 = csv)
    
3.  Output will be:
    
    *   Displayed in terminal
        
    *   Saved in file
        

📂 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   news-scraper/  │── scraper.py          # Main script  │── headlines.txt       # Output file (optional)  │── headlines.csv       # Output file (optional)  │── README.md           # Project documentation   `

💡 Example Output
-----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Top Headlines:  1. Global markets react to...  2. AI trends continue to grow...  3. New policies announced...   `

🎯 Learning Outcomes
--------------------

*   Understanding HTTP requests
    
*   HTML parsing using BeautifulSoup
    
*   Data extraction techniques
    
*   File handling in Python
    
*   Building real-world CLI tools
    

🔧 Future Improvements
----------------------

*   Multi-website scraping (BBC + TOI)
    
*   Category-based filtering
    
*   Automated daily scraping (scheduler)
    
*   Data visualization using pandas
    

👨‍💻 Author
------------

**Chinmay**CSE Student | Python Learner | Aspiring Data Analyst

⭐ Support
---------

If you like this project:

*   ⭐ Star the repository
    
*   🍴 Fork it
    
*   📢 Share with others
    

📌 Note
-------

This project is built for learning purposes and demonstrates real-world web scraping concepts.