from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from PyPDF2 import PdfFileReader, PdfFileWriter

# Đường dẫn tới file ảnh
image_path = "myplot.png"

# Các trường dữ liệu của thẻ sinh viên
student_id = "123456"
student_name = "Nguyen Van A"
course = "Python Programming"
academic_year = "2023-2024"

# Tạo ảnh nền cho thẻ sinh viên
background = Image.new('RGB', (600, 400), (255, 255, 255))

# Tải ảnh hồ sơ sinh viên và chèn vào thẻ
student_image = Image.open(image_path)
student_image = student_image.resize((150, 150))
background.paste(student_image, (50, 50))

# Tạo các đối tượng văn bản cho các trường dữ liệu
font = ImageFont.truetype('arial.ttf', 20)
text_color = (0, 0, 0)
text_draw = ImageDraw.Draw(background)

# Chèn các trường dữ liệu vào thẻ
text_draw.text((200, 10), "Student ID: {}".format(student_id), fill=text_color, font=font)
text_draw.text((200, 50), "Student Name: {}".format(student_name), fill=text_color, font=font)
text_draw.text((200, 90), "Course: {}".format(course), fill=text_color, font=font)
text_draw.text((200, 130), "Academic Year: {}".format(academic_year), fill=text_color, font=font)

background.save('student_card.png')

# Tạo một file PDF mới và chèn thẻ sinh viên vào đó
# output_pdf = PdfFileWriter()
# input_pdf = PdfFileReader(open("path/to/input_pdf_file.pdf", "rb"))
# page = input_pdf.getPage(0)
# page_pdf = BytesIO()
# background.save(page_pdf, "PDF", quality=100)
# page_pdf.seek(0)
# background_pdf = PdfFileReader(page_pdf)
# page.mergePage(background_pdf.getPage(0))
# output_pdf.addPage(page)

# # Lưu file PDF mới
# with open("path/to/output_pdf_file.pdf", "wb") as outputStream:
#     output_pdf.write(outputStream)