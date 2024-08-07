#Sistem Pemantauan Jaringan
1. Deskripsi Umum
Aplikasi Sistem Pemantauan Jaringan adalah alat yang dirancang untuk memantau dan menganalisis perangkat-perangkat dalam jaringan komputer. Aplikasi ini mengumpulkan data dari berbagai perangkat seperti router, switch, dan server untuk memantau kinerja, penggunaan sumber daya, dan status kesehatan perangkat tersebut. Dengan informasi yang diperoleh, pengguna dapat memantau dan mengelola jaringan secara efisien, serta mendeteksi dan mengatasi masalah yang mungkin terjadi.

2. Fitur Utama
Pemantauan Perangkat: Aplikasi memantau perangkat-perangkat dalam jaringan, termasuk penggunaan CPU, memori, bandwidth, dan port terbuka.
Analisis Data: Mengumpulkan data dari perangkat untuk analisis lebih lanjut, membantu dalam identifikasi tren dan potensi masalah.
Peringatan dan Notifikasi: Memberikan notifikasi dan peringatan ketika perangkat mencapai ambang batas tertentu atau mengalami masalah.
Antarmuka Pengguna: Menyediakan antarmuka berbasis web untuk memudahkan pengguna dalam melihat data dan status perangkat secara real-time.
3. Cara Kerja
Inisialisasi Database:
Aplikasi menggunakan SQLite sebagai database untuk menyimpan informasi tentang perangkat yang dipantau. Tabel-tabel di database mencakup data seperti ID perangkat, alamat IP, nama, penggunaan CPU, memori, bandwidth, dan port terbuka. Inisialisasi database dilakukan dengan skrip yang membuat tabel-tabel yang diperlukan.

Pemantauan Jaringan:
Aplikasi melakukan pemantauan jaringan dengan menggunakan SNMP (Simple Network Management Protocol) atau metode lain untuk mengumpulkan data dari perangkat. Proses ini dilakukan secara berkala untuk mendapatkan data terkini.

Pengolahan Data:
Data yang dikumpulkan dari perangkat disimpan dalam database dan diproses untuk analisis lebih lanjut. Penggunaan CPU, memori, bandwidth, dan status port dianalisis untuk memastikan perangkat berfungsi dengan baik dan tidak mengalami masalah.

Penyimpanan dan Akses Data:
Data yang telah diproses disimpan dalam database SQLite. Aplikasi menggunakan SQLAlchemy untuk berinteraksi dengan database dan melakukan query untuk mendapatkan data yang dibutuhkan.

Antarmuka Pengguna:
Aplikasi menyediakan antarmuka web yang memungkinkan pengguna untuk melihat data secara real-time. Halaman utama menampilkan informasi terkini tentang perangkat yang dipantau, termasuk grafik dan tabel yang menunjukkan penggunaan sumber daya dan status perangkat.

Peringatan dan Notifikasi:
Aplikasi mengonfigurasi peringatan untuk memberikan notifikasi jika terjadi masalah atau jika perangkat mencapai ambang batas tertentu. Notifikasi ini dapat dikirimkan melalui email atau ditampilkan di antarmuka pengguna.
