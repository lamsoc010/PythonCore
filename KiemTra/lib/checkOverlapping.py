def is_overlapping(shape1, shape2):
    """
    Kiểm tra xem hai hình có chồng lên nhau hay không
    """
    # Tính toán tọa độ các cạnh của hai hình
    x1, y1, w1, h1 = shape1.get_bounds()
    x2, y2, w2, h2 = shape2.get_bounds()
    
    # Kiểm tra xem hai hình có trùng nhau hay không
    if shape1 == shape2:
        return True
    
    # Kiểm tra xem hai hình có giao nhau hay không
    if x1 + w1 > x2 and x2 + w2 > x1 and y1 + h1 > y2 and y2 + h2 > y1:
        return True
    
    # Nếu không thì hai hình không chồng lên nhau
    return False

def count_overlapping_shapes(shapes):
    max_count = 0
    max_overlapping_shapes = []

    for i in range(len(shapes)):
        overlapping_shapes = [shapes[i]]
        count = 0

        for j in range(i + 1, len(shapes)):
            if is_overlapping(shapes[i], shapes[j]):
                overlapping_shapes.append(shapes[j])
                count += 1

        if count > max_count:
            max_count = count
            max_overlapping_shapes = overlapping_shapes

    return max_count, max_overlapping_shapes