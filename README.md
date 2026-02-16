Proyek ini berisi dataset performa jaringan seluler dan skrip EDA otomatis untuk mendukung pembuatan dashboard operasional NOC (Network Operation Center) Witel JTT dalam memantau performa dan anomali jaringan.

## 📦 Dataset

Dataset berisi log performa jaringan per call/session dengan beberapa kolom utama, antara lain:

- `Timestamp`: waktu panggilan/traffic.
- `Signal Strength dBm`: kekuatan sinyal (dBm, semakin negatif = semakin lemah).
- `SNR`: Signal-to-Noise Ratio.
- `Call Duration s`: durasi call/traffic (detik).
- `Environment`: kategori lokasi (home, urban, suburban, open).
- `Attenuation`: nilai redaman sinyal.
- `Distance to Tower km`: jarak ke BTS.
- `Tower ID`: ID menara/pemancar.
- `User ID`: ID pengguna.
- `Call Type`: tipe traffic (voice / data).
- `IncomingOutgoing`: arah traffic (incoming / outgoing).

Dataset juga dapat diperluas dengan sheet/kolom turunan untuk kebutuhan feature engineering dan dashboard ringkasan.
