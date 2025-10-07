from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def main():
    print("Question: Generate 8-10 sentences English text about Linus Torvalds's contributions to software development and technology innovation")

    from dotenv import load_dotenv
    load_dotenv()

    from langchain_openai import ChatOpenAI

    import os

    GEP_API_KEY = os.environ["GEP_API_KEY"]
    GEP_API_URL = os.environ["GEP_API_URL"]

    generate_prompt_template = ChatPromptTemplate.from_template(
        """
        You are a professional and experienced tech blog text writer. Write a 8-10 sentences text on specified topic:
        -------
        {topic}
        -------
        Answer:
        """
    )

    shakespeare_prompt = ChatPromptTemplate.from_template(
        """
        You are a professional and experienced text rewriter, specialized in rewriting given text in William Shakespeare style. 
        Lines should be short, resembling old school Shakespeare poetry formatting, like in example below.
        
        Example:
        Torvalds's labors have likewise wielded great 
        Influence upon the practices of software licensing, 
        advocating for the GNU General Public License (GPL). 
        ...
        
        Rewrite given passage accordingly:
        -------
        {text}
        -------
        Answer:
        """
    )

    md_format_prompt = ChatPromptTemplate.from_template(
        """
        You are a professional text formatting assistant. Format given text in Markdown. 
        Add title as 3rd leve heading.
        Highlight names in bold (like **John Doe**, **Sarah**, etc).
        Highlight tech product or brand names in italic (like *Microsoft*, *Git* etc).
        DO NOT include "```markdown" and "```" marks in the final answer!
        -------
        {text}
        -------
        Answer:
        """
    )

    llm = ChatOpenAI(
        model="amazon.nova-lite-v1:0",
        base_url=GEP_API_URL,
        api_key=GEP_API_KEY
    )

    generate_chain = generate_prompt_template | llm | StrOutputParser()
    shakespeare_chain = shakespeare_prompt | llm | StrOutputParser()
    md_format_chain = md_format_prompt | llm | StrOutputParser()

    print("\n----- Generated Text -----")
    # generate text about Linus Torvalds
    result = generate_chain.invoke(
        {"topic": "Generate 8-10 sentences English text about Linus Torvalds's contributions to software development and technology innovation"}
    )
    print(f"\n{result}")

    print("\n----- Rewritten in Shakespeare style -----")
    # rewrite text in Shakespeare style
    result = shakespeare_chain.invoke(
        {
            "text": result
        }
    )
    print(f"\n{result}")

    print("\n----- MD Formatted -----")
    # MD format
    result = md_format_chain.invoke(
        {
            "text": result
        }
    )
    print(f"\n{result}")

    fname="linus.md"
    with open(fname, "w") as f:
        f.write(result)
        print(f"\nResult was written in file: {fname}")


if __name__ == "__main__":
    main()
