import ctypes
from time import sleep
library = ctypes.CDLL('./stackoverflow.so')
get_data = library.GetData
free_me = library.FreeMe
free_me.argtypes = [ctypes.POINTER(ctypes.c_char)]
get_data.restype = ctypes.POINTER(ctypes.c_char)

for i in range(1,100):
    j = get_data("", "", "")
    print(ctypes.c_char_p.from_buffer(j).value.decode('UTF-8'))
    free_me(j)
    # print(j)
    sleep(1)
