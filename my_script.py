def read_data():
    # ده كود هيطلع إيرور لأن الملف ده مش موجود
    with open("non_existent_file.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    read_data()
