import time
from pathlib import Path

from pypdf import PdfReader


class PDFUtil:

    @staticmethod
    def wait_for_pdf_download(
        download_directory,
        timeout=20
    ):
        download_directory = Path(download_directory)
        end_time = time.time() + timeout

        while time.time() < end_time:
            partial_downloads = list(
                download_directory.glob("*.crdownload")
            )

            pdf_files = list(
                download_directory.glob("*.pdf")
            )

            if (
                pdf_files
                and not partial_downloads
            ):
                downloaded_pdf = max(
                    pdf_files,
                    key=lambda file: file.stat().st_mtime
                )

                if downloaded_pdf.stat().st_size > 0:
                    return downloaded_pdf

            time.sleep(0.5)

        raise TimeoutError(
            "Order-summary PDF was not downloaded "
            f"within {timeout} seconds."
        )

    @staticmethod
    def read_pdf(file_path):
        reader = PdfReader(file_path)
        pdf_text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                pdf_text += page_text + "\n"

        return pdf_text 