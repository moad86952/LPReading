def get_index_positions(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list


L28 = [[0, 0, 0, 0, 5.0, 5.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 5.0, 5.1, 5.2, 5.3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 5.1, 5.2, 5.2, 5.3, 5.4, 5.5, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 0, 0, 0, 0, 0, 0, 0],
       [5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 0, 0, 0, 0, 0, 0],
       [5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 0, 0, 0, 0, 0],
       [5.4, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 0, 0, 0, 0],
       [5.5, 5.6, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 0, 0, 0],
       [5.6, 5.7, 5.8, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 0, 0],
       [5.7, 5.8, 5.9, 6, 6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 0],
       [5.9, 5.9, 6.0, 6.1, 6.2, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2]]
L30 = [[0, 0, 0, 0, 0, 0, 5, 5.1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 5, 5.1, 5.2, 5.3, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 5, 5.1, 5.2, 5.3, 5.4, 5.5],
       [0, 0, 0, 5.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7],
       [0, 5.0, 5.1, 5.2, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
       [5, 5.1, 5.2, 5.3, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6],
       [5.2, 5.2, 5.3, 5.4, 5.5, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.1, 6.2],
       [5.3, 5.3, 5.4, 5.5, 5.6, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.1, 6.2, 6.3, 6.4],
       [5.4, 5.5, 5.5, 5.6, 5.7, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.2, 6.3, 6.4, 6.5, 6.6],
       [5.5, 5.6, 5.6, 5.7, 5.8, 5.9, 5.9, 6.0, 6.1, 6.2, 6.3, 6.3, 6.4, 6.5, 6.6, 6.7],
       [5.6, 5.7, 5.8, 5.8, 5.9, 6, 6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.5, 6.6, 6.7, 6.8],
       [5.7, 5.8, 5.9, 5.9, 6.0, 6.1, 6.2, 6.2, 6.3, 6.4, 6.5, 6.6, 6.6, 6.7, 6.8, 6.9],
       [5.9, 5.9, 6.0, 6.1, 6.1, 6.2, 6.3, 6.3, 6.4, 6.5, 6.6, 6.7, 6.7, 6.8, 6.9, 7.0],
       [6, 6, 6.1, 6.2, 6.2, 6.3, 6.4, 6.4, 6.5, 6.6, 6.7, 6.8, 6.8, 6.9, 7, 7.1], ]

while True:
    lens_type = input("enter the lens type ? ")
    if lens_type == "L28" or lens_type == "l28":
        row_l28 = [5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7]
        height_l28 = [2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5]
        width_l28 = input(f'Enter the max width of the lanes ? {row_l28}')
        index = row_l28.index(float(width_l28))
        selected_row = L28[index]
        # print(selected_row)
        max_width_l28 = [i for i in selected_row if i > 0]
        max_width_l28 = round(float(input(f'Enter The Isle width from this list {max_width_l28} ? ')), 1)
        selected_column_index = get_index_positions(selected_row, float(max_width_l28))
        hight_list = []
        for i in selected_column_index:
            hight_list.append(height_l28[i])
        print(hight_list)
    elif lens_type == "L30" or lens_type == "l30":
        row_l30 = [5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0]
        width_l30 = input(f'Enter the max width of the lanes ? {row_l30}')
        height_l30 = [2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5]
        index = row_l30.index(float(width_l30))
        selected_row = L30[index]
        # print(selected_row)
        max_width_l30 = [i for i in selected_row if i > 0]
        max_width_l30 = round(float(input(f'Enter The Isle width from this list {max_width_l30} ? ')), 1)
        selected_column_index = get_index_positions(selected_row, float(max_width_l30))
        hight_list = []
        for i in selected_column_index:
            hight_list.append(height_l30[i])
        print(f" You can install at heights : {hight_list} Mtr")
    else:
        print("this not a valid lens.")
        pass
