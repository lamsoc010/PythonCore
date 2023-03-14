import random

def generate_input_file(file_name, num_shapes):
    shapes = ['Rect', 'Circle', 'Triangle']
    with open(file_name, 'w') as f:
        for i in range(num_shapes):
            shape_type = random.choice(shapes)
            f.write(f"#{shape_type}\n")
            if shape_type == 'Rect':
                chieu_dai = random.randint(1, 10)
                chieu_rong = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f"{chieu_dai} {chieu_rong}\n")
                f.write(f"{x} {y}\n")
            elif shape_type == 'Circle':
                ban_kinh = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f"{ban_kinh}\n")
                f.write(f"{x} {y}\n")
            else:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                while (a + b <= c) or (a + c <= b) or (b + c <= a):
                    # Nếu ba cạnh không thỏa mãn điều kiện tam giác thì tạo lại đến khi thỏa mãn
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f"{a} {b} {c}\n")
                f.write(f"{x} {y}\n")

# generate_input_file("input.txt", 10)