import requests as net
import json
import os

# Konfigurasi file dan URL
cookie_file = "cookie.txt"
ids_file = "ids.txt"
url = "https://www.blackbox.ai/api/check"

def get_cookie():
    """Memeriksa apakah cookie sudah ada di file, jika tidak ada, minta input dari user."""
    if os.path.exists(cookie_file) and os.path.getsize(cookie_file) > 0:
        with open(cookie_file, "r") as f:
            return f.read().strip()
    else:
        cookie = input("Masukkan Cookie: ")
        with open(cookie_file, "w") as f:
            f.write(cookie)
        return cookie

def get_ids():
    """Memeriksa apakah ID sudah ada di file, jika tidak ada, minta input dari user."""
    if os.path.exists(ids_file) and os.path.getsize(ids_file) > 0:
        with open(ids_file, "r") as f:
            return f.read().strip()
    else:
        ids = input("Masukkan ID: ")
        with open(ids_file, "w") as f:
            f.write(ids)
        return ids

def send_query(cookie, query, ids):
    """Mengirimkan query ke server menggunakan cookie dan ID, serta menampilkan hasilnya."""
    headers = {
        "Host": "www.blackbox.ai",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "Origin": "https://www.blackbox.ai",
        "Referer": "https://www.blackbox.ai/?explore=true",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Priority": "u=1, i",
        "Cookie": cookie
    }

    # Payload sesuai dengan format yang diharapkan
    data = {
        "query": query,
        "messages": [
            {"id": ids, "content": query, "role": "user"}
        ],
        "index": None
    }

    # Mengirimkan POST request
    response = net.post(url, headers=headers, json=data)

    # Menampilkan respons mentah
    print("Raw Response Text:", response.text)
    
    # Menampilkan status kode
    print(f"Status Code: {response.status_code}")

def main():
    """Fungsi utama untuk menjalankan program."""
    cookie = get_cookie()
    ids = get_ids()
    query = input("Masukkan Query: ")
    send_query(cookie, query, ids)

if __name__ == "__main__":
    main()
