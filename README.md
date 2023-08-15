# Data_Compression_Algorithms
Comparison of three data compression algorithms

####### Tukish
Bu programda 3 farklı dosya sıkıştırma yöntemini test ettik.
Birinci dosyada 3 tanesini hız olarak test ettik
ikinci dosyada ise oluşturduğumuz bir dosya Metin belgesindeki veriyi sıkıştırdık daha sonra o veriyi tekrar eski haline dönüştürdük
#######


In this program, we tested 3 different file compression methods.
In the first file, we tested three of them for speed.
In the second file, we compressed the data from a text document that we created, and later restored that data back to its original state.

This code includes a Python program that tests and evaluates the performance of three different file compression methods (lzma, gzip, and bz2) by compressing a sample dataset. The steps are explained below:

Firstly, the required libraries (time, lzma, gzip, bz2) are imported.

A sample data is created: The variable data is assigned a byte sequence obtained by repeating the string 'This is some sample data' 990000 times.

The size of the original data is printed to the screen.

Testing the LZMA Compression Method:

The start time is recorded using time.time().
The data is compressed using lzma.compress(data).
The end time is recorded using time.time().
The compression time and the size of the compressed data are printed to the screen.
Testing the Gzip Compression Method:

The start time is recorded using time.time().
The data is compressed using gzip.compress(data, compresslevel=1). Here, the compresslevel=1 determines the compression level.
The end time is recorded using time.time().
The compression time and the size of the compressed data are printed to the screen.
Testing the Bz2 Compression Method:

The start time is recorded using time.time().
The data is compressed using bz2.compress(data).
The end time is recorded using time.time().
The compression time and the size of the compressed data are printed to the screen.
The purpose of this code is to assess how much the different compression methods can reduce the data size and to evaluate the time taken for these operations. Additionally, the compresslevel parameter is used to define the Gzip compression level. Lower levels provide faster compression with less reduction in size, while higher levels provide more compression at the cost of longer processing times.
