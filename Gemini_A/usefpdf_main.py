from fpdf import FPDF

def generate_topic_pdf_fpdf(csv_data, output_filename="topics_with_blanks_fpdf.pdf"):
    """
    Generates a PDF where each topic starts on a new page, followed by blank
    pages corresponding to the 'Pages' value, with the topic printed at the
    top and bottom-left of each page, and lines for notes, using fpdf2.

    Args:
        csv_data (str): A string containing the CSV data.
        output_filename (str): The name of the PDF file to generate.
    """
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    line_height = 5  # Adjust as needed for line spacing

    for line in csv_data.strip().split('\n')[1:]:  # Skip the header row
        order, topic, pages_str = line.split(',')
        try:
            num_pages = int(pages_str)
        except ValueError:
            print(f"Warning: Could not convert '{pages_str}' to an integer for topic '{topic}'. Skipping blank pages.")
            num_pages = 0

        # Add the topic page
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=16)
        pdf.cell(0, 10, topic, 0, 1, 'C') # Topic at the top-center
        pdf.set_font("Arial", size=12)
        pdf.text(10, 290, topic) # Topic at the lower-left

        # Add blank pages with topic and lines
        for _ in range(num_pages):
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.text(10, 290, topic) # Topic at the lower-left
            pdf.set_xy(10, 20) # Start drawing lines from near the top
            for i in range(30): # Add 30 lines (adjust as needed)
                pdf.line(10, pdf.get_y(), 200, pdf.get_y())
                pdf.ln(line_height) # Move to the next line

    pdf.output(output_filename)
    print(f"PDF '{output_filename}' generated successfully using fpdf2.")

# Your CSV data
csv_data = """Order,Topic,Pages
1,Variables,2
2,Lists,3
3,Functions,3
4,While-loop,2
5,Methods,3
"""

generate_topic_pdf_fpdf(csv_data)