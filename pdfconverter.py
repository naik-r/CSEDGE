import PyPDF2
import os

def convert_pdf(input_file, output_file_base, format):

  if not os.path.exists(input_file):  
    print(f"Error: Input file not found: {input_file}")
    return

  with open(input_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    if format == 'text':
      with open(f"{output_file_base}.txt", 'w', encoding='utf-8') as out_file: 
        for page_num in range(len(pdf_reader.pages)):
          page = pdf_reader.pages[page_num]
          text = page.extract_text()
          out_file.write(text)
    elif format == 'images':
      for page_num in range(1):
        page = pdf_reader.pages[page_num]
        images = page.extract_images()
        if images:
          for i, image in enumerate(images):
            output_filename = f"{output_file_base}_page_{page_num+1}_image_{i+1}.jpg"
            with open(output_filename, 'wb') as img_file:
              img_file.write(image['data'])
        else:
          print(f"No images found on page {page_num+1}.")
    else:
      print(f"Unsupported format: {format}")

if __name__ == "__main__":
  input_file = "Learner License.pdf"
  output_file_base = "converted_file"  
  format = input("Enter desired format (text, images): ")

  convert_pdf(input_file, output_file_base, format.lower())

  print(f"PDF conversion complete! Output: {output_file_base}.{format}")
