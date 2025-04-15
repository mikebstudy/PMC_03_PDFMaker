from fpdf import FPDF
import pandas as pd
from io import StringIO

def generate_topic_pdf_exactly_right(csv_string, output_filename="topics_exactly_right_fpdf.pdf"):
    """
    Generates a PDF with the exact number of pages (1 initial + 'Pages' additional),
    topic header only on the first page, footer on the right of all pages,
    and lines filling all pages.

    Args:
        csv_string (str): A string containing the CSV data.
        output_filename (str): The name of the PDF file to generate.
    """
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    line_height = 5
    margin = 10  # Standard margin

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

        # Add the first topic page WITH header and lines
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=16)
        pdf.text(margin, 15, topic)  # Header on the left
        pdf.set_font("Arial", size=12)
        pdf.text(pdf.get_x() + 170, 290, topic) # Footer on the right

        # Calculate the number of lines to fill the page
        available_height = 297 - 2 * margin - 20 # A4 height - top/bottom margins - header/footer space
        num_lines = int(available_height / line_height)

        pdf.set_xy(margin, 25) # Start drawing lines a bit below the header
        for i in range(num_lines):
            pdf.line(margin, pdf.get_y(), 210 - margin, pdf.get_y()) # Assuming A4 width (210 mm)
            pdf.ln(line_height)

        # Add the *additional* blank pages with ONLY footer and lines
        for _ in range(num_pages):
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.text(pdf.get_x() + 170, 290, topic) # Footer on the right

            # Calculate the number of lines to fill the page
            available_height = 297 - 2 * margin - 10 # A4 height - top/bottom margins - footer space
            num_lines = int(available_height / line_height)

            pdf.set_xy(margin, margin) # Start drawing lines from the top margin
            for i in range(num_lines):
                pdf.line(margin, pdf.get_y(), 210 - margin, pdf.get_y()) # Assuming A4 width (210 mm)
                pdf.ln(line_height)

    pdf.output(output_filename)
    print(f"PDF '{output_filename}' generated successfully with the exact number of pages using pandas and fpdf2.")

# Your CSV data as a string
csv_data = """Order,Topic,Pages
1,Variables,2
2,Lists,3
3,Functions,3
4,While-loop,2
5,Methods,3
"""

generate_topic_pdf_exactly_right(csv_data)