from fpdf import FPDF
import pandas as pd
from io import StringIO

def generate_topic_pdf_from_pandas(csv_string, output_filename="topics_from_pandas_fpdf.pdf"):
    """
    Generates a PDF from CSV data using pandas for processing.

    Args:
        csv_string (str): A string containing the CSV data.
        output_filename (str): The name of the PDF file to generate.
    """
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    line_height = 5

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_string))

    # Iterate through each row of the DataFrame
    for index, row in df.iterrows():
        topic = row['Topic']
        try:
            num_pages = int(row['Pages'])
        except ValueError:
            print(f"Warning: Could not convert '{row['Pages']}' to an integer for topic '{topic}'. Skipping blank pages.")
            num_pages = 0

        # Add the topic page
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=16)
        pdf.cell(0, 10, topic, 0, 1, 'C')
        pdf.set_font("Arial", size=12)
        pdf.text(10, 290, topic)

        # Add blank pages with topic and lines
        for _ in range(num_pages):
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.text(10, 290, topic)
            pdf.set_xy(10, 20)
            for i in range(30):
                pdf.line(10, pdf.get_y(), 200, pdf.get_y())
                pdf.ln(line_height)

    pdf.output(output_filename)
    print(f"PDF '{output_filename}' generated successfully using pandas and fpdf2.")

# Your CSV data as a string
csv_data = """Order,Topic,Pages
1,Variables,2
2,Lists,3
3,Functions,3
4,While-loop,2
5,Methods,3
"""

generate_topic_pdf_from_pandas(csv_data)