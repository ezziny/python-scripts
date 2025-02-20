import os
from PyPDF2 import PdfReader, PdfWriter

#edit dimensions as you please. dimensions should be in mm (for example here the new dimensions are 90mm x 50 mm)
def process_pdf(input_path, output_path, new_width=90, new_height=50):
    pdfFile = PdfReader(open(input_path, 'rb'))
    writer = PdfWriter()

    new_height_pts = new_height * 2.83464567
    new_width_pts = new_width * 2.83464567

    for page in pdfFile.pages:
        page.scale_to(new_width_pts, new_height_pts)
        writer.add_page(page)

    with open(output_path, "wb") as outfp:
        writer.write(outfp)

def main():
    input_dir = "your/directory/goes/here"
    output_dir = input_dir + "_resized"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"resized_{filename}")
            try:
                process_pdf(input_path, output_path)
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    main()