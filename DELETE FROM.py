import sqlite3


conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()


jenis = 'Mamalia'  
cursor.execute(f"DELETE FROM hewan WHERE jenis = '{jenis}'")
conn.commit()


if cursor.rowcount > 0:
    print(f"Data HEWAN dengan Jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data HEWAN dengan Jenis {jenis}.")


conn.close()
