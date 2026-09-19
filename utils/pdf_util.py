from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os
from reportlab.platypus import (Paragraph,SimpleDocTemplate,Spacer,Table,TableStyle,)


class PDFUtil:

    @staticmethod
    def generate_order_summary(
        file_path,
        customer_name,
        product_names,
        product_prices,
        item_total,
        tax,
        final_total,
        order_status,
    ):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        document = SimpleDocTemplate(
            file_path,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50,
        )

        styles = getSampleStyleSheet()
        content = []

        content.append(
            Paragraph("SauceDemo Order Summary", styles["Title"])
        )

        content.append(Spacer(1, 20))

        content.append(
            Paragraph(
                f"<b>Customer:</b> {customer_name}",
                styles["Normal"],
            )
        )

        content.append(Spacer(1, 15))

        product_data = [["Product", "Price"]]

        for index in range(len(product_names)):
            product_data.append(
                [
                    product_names[index],
                    product_prices[index],
                ]
            )

        product_table = Table(
            product_data,
            colWidths=[4.5 * inch, 1.5 * inch],
        )

        product_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#E2231A"),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white,
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold",
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.grey,
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),
                ]
            )
        )

        content.append(product_table)
        content.append(Spacer(1, 20))

        content.append(
            Paragraph(item_total, styles["Normal"])
        )

        content.append(
            Paragraph(tax, styles["Normal"])
        )

        content.append(
            Paragraph(
                f"<b>{final_total}</b>",
                styles["Normal"],
            )
        )

        content.append(Spacer(1, 20))

        content.append(
            Paragraph(
                f"<b>Order Status:</b> {order_status}",
                styles["Normal"],
            )
        )

        document.build(content)

        return file_path

    @staticmethod
    def read_pdf(file_path):
        reader = PdfReader(file_path)
        pdf_text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                pdf_text += page_text

        return pdf_text