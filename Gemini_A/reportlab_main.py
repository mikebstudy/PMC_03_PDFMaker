from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def generate_topic_pdf(csv_data, output_filename="topics_with_blanks.pdf"):
    """
    Generates a PDF where each topic starts on a new page, followed by blank
    pages corresponding to the 'Pages' value, with the topic printed at the
    top and bottom-left of each page, and lines for notes.

    Args:
        csv_data (str): A string containing the CSV data.
        output_filename (str): The name of the PDF file to generate.
    """
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    lines_per_page = 30  # Adjust as needed for line spacing

    for line in csv_data.strip().split('\n')[1:]:  # Skip the header row
        order, topic, pages_str = line.split(',')
        try:
            num_pages = int(pages_str)
        except ValueError:
            print(f"Warning: Could not convert '{pages_str}' to an integer for topic '{topic}'. Skipping blank pages.")
            num_pages = 0

        # Add the topic page
        story.append(Paragraph(topic, styles['h1']))
        story.append(Spacer(1, 0.2 * inch)) # Add some space

        c = canvas.Canvas(output_filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(inch, 0.75 * inch, topic) # Lower left corner
        c.saveState()
        c.restoreState()
        c.showPage() # Start a new page

        # Add blank pages with topic and lines
        for _ in range(num_pages):
            c = canvas.Canvas(output_filename, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(inch, 0.75 * inch, topic) # Lower left corner
            c.drawCentredString(letter[0] / 2.0, letter[1] - inch, topic) # Top center
            y_position = 2 * inch
            for _ in range(lines_per_page):
                c.line(inch, y_position, letter[0] - inch, y_position)
                y_position += (letter[1] - 4 * inch) / (lines_per_page - 1) if lines_per_page > 1 else 1 * inch
            c.showPage()

    doc.build(story)
    print(f"PDF '{output_filename}' generated successfully.")

# Your CSV data
csv_data = """Order,Topic,Pages
1,Variables,2
2,Lists,3
3,Functions,3
4,While-loop,2
5,Methods,3
"""

generate_topic_pdf(csv_data)