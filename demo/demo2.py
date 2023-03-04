from PIL import Image, ImageDraw, ImageFont
# Tạo ảnh mới với độ phân giải 800x600 pixel và màu trắng
img = Image.new('RGB', (800, 600), color='white')

# Tạo đối tượng vẽ trên ảnh
draw = ImageDraw.Draw(img)

# Đặt font chữ và kích thước
font = ImageFont.truetype('arial.ttf', size=24)

# Vẽ tiêu đề của báo cáo
draw.text((10, 10), 'BÁO CÁO DOANH SỐ', font=font, fill='black')

# Vẽ biểu đồ
# ...

# Lưu ảnh ra file
img.save('bao_cao.png')