def read_data(file_path):
    store_data = []

    with open(file_path, "r") as f:
        records = f.readlines()
    for record in records:
        cleaned_record = record.strip()
        name, age = cleaned_record.split(",")
        data = (name, int(age))
        store_data.append(data)
    return store_data

    

