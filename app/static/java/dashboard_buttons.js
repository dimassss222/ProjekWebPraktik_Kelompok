var tombol_keluar = document.getElementById('tombol_keluar');
var peringatan_keluar = document.getElementById('peringatan_keluar');
var button_tidak = document.getElementById('button-tidak');
var button_iya = document.getElementById('button-iya');

button_iya.style.cursor = 'pointer';
button_tidak.style.cursor = 'pointer';
peringatan_keluar.style.display = 'none';

tombol_keluar.onclick = function () {
    peringatan_keluar.style.display = 'block'
}
button_iya.onclick = function () {
    window.location.assign('/logout')
}
button_tidak.onclick = function () {
    peringatan_keluar.style.display = 'none'
}