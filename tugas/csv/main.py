import csv
import json
print("-------csv-------")
file_json_path = r"C:\Users\Dzaky Ammar Banu\OneDrive\Documents\belajar python\materi-10-file\rukun_islam.json"
with open(file_json_path, "r") as file_rukun_islam:
# guanakan fungsi reader() dari module csv
    data_rukun_islam = json.load(file_rukun_islam)
    print(f"Judul:{data_rukun_islam['Judul']}")
    print(f"Jumlah rukun:{data_rukun_islam}")
    # keluarkan seluruh data dengan forloop
    for rukun in data_rukun_islam:
        print(rukun)