import time
import lzma
import gzip
import bz2

data=b'This is some sapmle data' * 990000

print("Original data size: ", len(data))

start=time.time()
compressed_data_lzma=lzma.compress(data)
end=time.time()

print(end-start)
print("lzma data size: ",len(compressed_data_lzma))

#########

start=time.time()
#compressed_data_gzip=gzip.compress(data)
compressed_data_gzip=gzip.compress(data,compresslevel=1) # determination of compression level 1-9
end=time.time()

print(end-start)
print("gzip data size: ",len(compressed_data_gzip))


#########

start=time.time()
compressed_data_bz2=bz2.compress(data)
end=time.time()

print(end-start)
print("bz2 data size: ",len(compressed_data_bz2))
