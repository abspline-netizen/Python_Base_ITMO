def load_test_data():
    data = []
    with open("test_Drowning_2_2_data.txt") as f:
        for line in f:
            if line.strip():
                data.append(list(map(float, line.split())))
    
    return data
    

