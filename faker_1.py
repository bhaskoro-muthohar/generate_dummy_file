from faker import Faker
import random, string, datetime
import csv

def datagenerate(csv_name, records, headers):
    fake = Faker('en_US')
    random.seed(69)
    with open(csv_name, "wt") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()

        for row in range(records):
            writer.writerow({
                "id_penyelenggara" : (random.randint(0, 148)),
                "id_borrower" : (random.randint(0, records)),
                "jenis_pengguna" : 1,
                "nama_borrower" : fake.name(),
                "no_identitas" : fake.ssn(),
                "no_npwp" : fake.itin(),
                "id_pinjaman" : (random.randint(0, records)),
                "tgl_perjanjian_borrower" : fake.date_between(start_date='-2y', end_date='today'),
                "tgl_penyaluran_dana" : fake.date_between(start_date='-2y', end_date='today'),
                "nilai_pendanaan" : (random.randint(200000, 15000000)),
                "tgl_pelaporan_data" : fake.date_between(start_date='today', end_date='today'),
                "kualitas_pinjaman" : (random.randint(1, 3)),
                "dpd_terakhir" : (random.randint(0, 30)),
                "dpd_max" : (random.randint(0, 30)),
                "status_pinjaman" : random.choice(["W", "L", "O"])
            })

if __name__ == '__main__':
    records = 1000
    name = "1000.csv"
    headers = ["id_penyelenggara", "id_borrower", "jenis_pengguna", "nama_borrower", "no_identitas", "no_npwp",
                "id_pinjaman", "tgl_perjanjian_borrower", "tgl_penyaluran_dana", "nilai_pendanaan",
                "tgl_pelaporan_data", "kualitas_pinjaman", "dpd_terakhir", "dpd_max",
                "status_pinjaman"]
    datagenerate(name, records, headers)
    print("selesai")
