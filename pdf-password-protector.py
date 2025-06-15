#!/usr/bin/env python3
"""
PDF Password Protection Script

This script adds password encryption to a PDF file using the pypdf library.
It accepts the input PDF path, output PDF path, and encryption password via command-line arguments.

Author: Muru
Date: 2025-06-15
"""

import argparse
from pypdf import PdfReader, PdfWriter
import os
import sys

def protect_pdf(input_file: str, output_file: str, password: str) -> None:
    """
    Encrypts a PDF file with the given password and writes the result to a new file.

    :param input_file: Path to the input (original) PDF file.
    :param output_file: Path to save the encrypted output PDF.
    :param password: Password to encrypt the PDF with.
    """
    try:
        # Load the existing PDF
        reader = PdfReader(input_file)
        writer = PdfWriter()

        # Add each page from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Set the encryption password
        writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_file, "wb") as out_file:
            writer.write(out_file)

        print(f"✅ PDF successfully encrypted and saved to: {output_file}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main entry point for the script. Parses arguments and runs the protection function.
    """
    parser = argparse.ArgumentParser(
        description="Encrypt a PDF file with a password using pypdf."
    )
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("output", help="Path to save the encrypted PDF")
    parser.add_argument("password", help="Password to secure the PDF")

    args = parser.parse_args()

    # Validate input file
    if not os.path.isfile(args.input):
        print(f"❌ Error: '{args.input}' is not a valid file.")
        sys.exit(1)

    # Run the encryption
    protect_pdf(args.input, args.output, args.password)

if __name__ == "__main__":
    main()
