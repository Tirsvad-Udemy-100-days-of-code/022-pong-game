[English](Home) · [Dansk](Home-da) · **Bahasa Melayu**

# Pong Game

Permainan arked Pong klasik untuk dua pemain dengan grafik turtle Python: pastikan bola kekal dalam permainan dan jaring mata apabila pemain lain terlepas.

![Tetingkap permainan Pong semasa permainan, skor 3 lawan 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/raw/branch/main/docs/images/pong.png)

## Apakah ini?

Hari ke-22 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Tetingkap hitam 800 kali 600 bertajuk "Pong" dibuka dengan sebuah pemukul putih di setiap sisi dan sebiji bola putih di tengah. Pemain kanan menggerakkan pemukul kanan dengan kekunci anak panah <kbd>Up</kbd> dan <kbd>Down</kbd>, pemain kiri menggerakkan pemukul kiri dengan <kbd>W</kbd> dan <kbd>S</kbd>. Bola melantun pada dinding atas dan bawah serta pada pemukul, dan setiap pukulan pemukul menjadikannya lebih laju. Apabila pemukul terlepas, pemain lain mendapat satu mata, bola kembali ke tengah, bertukar arah dan kelajuannya ditetapkan semula. Mata dipaparkan di bahagian atas: pemain kiri di sebelah kiri, pemain kanan di sebelah kanan. Satu klik pada tetingkap menutupnya. Peraturan permainan yang tidak memerlukan paparan berada dalam `rules.py`, jadi ia diuji tanpa tetingkap.

## Apa yang diajar oleh latihan ini

- Menyediakan skrin turtle dan melukis dua pemukul serta sebiji bola sebagai objek `Turtle`
- Menggerakkan bola bingkai demi bingkai dengan `tracer`, `update` dan `sleep`, dan melantunkannya pada dinding serta pemukul
- Menulis kelas `Paddle`, `Ball` dan `Scoreboard` sebagai subkelas `Turtle`
- Mengikat kekunci dua pemain kepada dua pemukul
- Mengesan pukulan melalui jarak dan kedudukan, melajukan bola dan menetapkannya semula apabila pemukul terlepas
- Memisahkan peraturan daripada paparan dalam `rules.py`, supaya ia boleh diuji tanpa tetingkap

## Apa yang dilakukannya

- Dua pemukul, satu untuk setiap pemain: Up dan Down untuk pemukul kanan, W dan S untuk pemukul kiri
- Bola yang melantun pada dinding dan pemukul serta bertambah laju pada setiap pukulan pemukul
- Satu mata untuk pemain lain apabila pemukul terlepas; bola kembali ke tengah dan kelajuannya ditetapkan semula
- Papan skor dengan kedua-dua mata di bahagian atas tetingkap
- Tiada kebergantungan semasa larian selain pustaka standard Python

## Seterusnya

- [Bermula](Getting-Started-ms)
- [Dokumen Projek](Project-Documents-ms)
