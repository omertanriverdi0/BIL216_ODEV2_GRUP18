import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sounddevice as sd

# --- 1. AYARLAR ---
fs = 44100
harf_suresi = 0.2
bosluk_suresi = 0.05
chars = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ "

low_freqs = [600, 700, 800, 900, 1000]
high_freqs = [1200, 1300, 1400, 1500, 1600, 1700]

dtmf_table = {}
counter = 0
for l in low_freqs:
    for h in high_freqs:
        if counter < len(chars):
            dtmf_table[chars[counter]] = (l, h)
            counter += 1

# --- 2. FONKSİYONLAR ---
def metni_sese_cevir_ve_cal(metin):
    t = np.linspace(0, harf_suresi, int(fs * harf_suresi))
    tum_sinyal = []
    for harf in metin.upper():
        if harf in dtmf_table:
            f1, f2 = dtmf_table[harf]
            sinyal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
            tum_sinyal.append(sinyal)
            tum_sinyal.append(np.zeros(int(fs * bosluk_suresi)))
    final_sinyal = np.concatenate(tum_sinyal)
    sd.play(final_sinyal, fs)
    sd.wait()
    final_sinyal_int = (final_sinyal / np.max(np.abs(final_sinyal)) * 32767).astype(np.int16)
    wav.write('mesaj.wav', fs, final_sinyal_int)

def sesi_metne_cevir(dosya_adi='mesaj.wav'):
    rate, data = wav.read(dosya_adi)
    if len(data.shape) > 1: data = data[:, 0]
    adim = int(fs * (harf_suresi + bosluk_suresi))
    parca_boyutu = int(fs * harf_suresi)
    cozulen_mesaj = ""
    for i in range(0, len(data) - parca_boyutu + 1, adim):
        parca = data[i : i + parca_boyutu]
        parca = parca * np.hamming(len(parca))
        yf = np.fft.fft(parca)
        xf = np.fft.fftfreq(len(parca), 1/fs)
        idx = xf > 0
        xf_p, yf_p = xf[idx], np.abs(yf[idx])
        peaks = xf_p[np.argsort(yf_p)[-2:]]
        f_bulunan = sorted(peaks)
        bulunan_harf = "?"
        for harf, (tf1, tf2) in dtmf_table.items():
            if abs(f_bulunan[0] - tf1) < 20 and abs(f_bulunan[1] - tf2) < 20:
                bulunan_harf = harf
                break
        cozulen_mesaj += bulunan_harf
    return cozulen_mesaj

# --- 3. ANA ÇALIŞTIRMA VE GRAFİK ---
if __name__ == "__main__":
    mesaj = "İSTANBUL"
    metni_sese_cevir_ve_cal(mesaj)
    sonuc = sesi_metne_cevir('mesaj.wav')
    
    print("\n" + "="*30)
    print(f"GİRİLEN: {mesaj} -> ÇÖZÜLEN: {sonuc}")
    print("="*30)

    # Grafik için tek bir harfi tekrar analiz et
    rate, data = wav.read('mesaj.wav')
    if len(data.shape) > 1: data = data[:, 0]
    parca = data[0 : int(fs * harf_suresi)]
    parca = parca * np.hamming(len(parca))
    yf = np.fft.fft(parca)
    xf = np.fft.fftfreq(len(parca), 1/fs)
    idx = xf > 0
    
 
    plt.style.use('dark_background') # Koyu tema 
    plt.figure(figsize=(12, 6))
    
    # Ana sinyali çiz (Parlak turkuaz/cyan rengi)
    plt.plot(xf[idx], np.abs(yf[idx]), color='#00ffcc', linewidth=1.2, label='Frekans Bileşenleri')
    
    # Altını hafif saydam bir renkle doldur
    plt.fill_between(xf[idx], np.abs(yf[idx]), color='#00ffcc', alpha=0.1)
    
    # En yüksek iki tepeyi (peak) işaretle (Kırmızı noktalarla)
    top2_idx = np.argsort(np.abs(yf[idx]))[-2:]
    plt.scatter(xf[idx][top2_idx], np.abs(yf[idx])[top2_idx], color='red', s=50, zorder=5, label='Tespit Edilen Tepeler')

    # Grafik Detayları
    plt.xlim(400, 2000) # Sadece bizim frekans aralığı
    plt.title(f"DTMF SPEKTRUM ANALİZİ: '{mesaj[0]}' HARFİ", fontsize=14, fontweight='bold', color='#00ffcc', pad=20)
    plt.xlabel("Frekans (Hz)", fontsize=11, color='white')
    plt.ylabel("Enerji / Genlik", fontsize=11, color='white')
    
    # Izgara çizgilerini daha soft yap
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(loc='upper right')
    
    # Kenarlık renklerini ayarla
    ax = plt.gca()
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    
    plt.tight_layout()
    plt.show()