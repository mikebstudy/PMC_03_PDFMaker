from fpdf import FPDF
import csv
from io import StringIO

def generate_topic_pdf_from_csv_string(csv_string, output_filename="topics_from_csv_fpdf.pdf"):
    """
    Generates a PDF from CSV data provided as a string, emulating file reading.

    Args:
        csv_string (str): A string containing the CSV data.
        output_filename (str): The name of the PDF file to generate.
    """
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    line_height = 5

    # Use StringIO to treat the string as a file
    csvfile = StringIO(csv_string)
    reader = csv.reader(csvfile)
    header = next(reader) # Read the header row (optional, but good practice)

    for row in reader:
        if len(row) == 3:
            order, topic, pages_str = row
            try:
                num_pages = int(pages_str)
            except ValueError:
                print(f"Warning: Could not convert '{pages_str}' to an integer for topic '{topic}'. Skipping blank pages.")
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
        else:
            print(f"Warning: Skipping row with incorrect number of columns: {row}")

    pdf.output(output_filename)
    print(f"PDF '{output_filename}' generated successfully by emulating CSV reading with fpdf2.")

# Your CSV data as a string
csv_data = """Order,Topic,Pages
1,Variables,2
2,Lists,3
3,Functions,3
4,While-loop,2
5,Methods,3
"""

generate_topic_pdf_from_csv_string(csv_data)