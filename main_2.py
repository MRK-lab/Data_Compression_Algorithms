import time
import lzma

with open("file.txt", "rb") as f_in, lzma.open("file.xz", "wb") as f_out:
    f_out.write(f_in.read())

with lzma.open("file.xz", "rb") as f_in, open("uncompressed.txt", "wb") as f_out:
    f_out.write(f_in.read())

