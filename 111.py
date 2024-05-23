def find_element_index(matrix, target):
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == target:
                return row_index, col_index
    return None

# 示例用法
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target_element = 5
print(find_element_index(matrix, target_element))  # 输出 (1, 1)，表示元素 5 在第 1 行第 1 列
