import struct

# ## Format string essentials
# Format = [byte-order char][count+format_chars...]. Common type codes:

# | Code | C type / Python | Size (standard) |
# |---|---:|---:|
# | x | pad byte | 1 |
# | c | char (bytes length 1) | 1 |
# | b | signed char | 1 |
# | B | unsigned char | 1 |
# | ? | _Bool / bool | 1 |
# | h | short (signed) | 2 |
# | H | unsigned short | 2 |
# | i | int (signed) | 4 |
# | I | unsigned int | 4 |
# | l | long | 4 (standard) |
# | L | unsigned long | 4 |
# | q | long long (signed) | 8 |
# | Q | unsigned long long | 8 |
# | f | float | 4 |
# | d | double | 8 |
# | s | char[] (string) | count bytes |
# | p | pascal string (length-prefixed) | count bytes |
# | P | void * (pointer) | native pointer size |

# Counts can prefix codes, e.g. 4B = four unsigned bytes, 2s = two-byte string.

# ## Byte order, size & alignment (prefixes)
# - @ — native alignment, native byte order (default)
# - = — native byte order, standard sizes (no padding)
# - < — little-endian, standard sizes
# - > — big-endian, standard sizes
# - ! — network (= big-endian)

# Always explicitly specify endianness (< or >) for portable protocols.

# ## Alignment behavior
# - Native (@) inserts padding so packed bytes match C struct layout on that platform.
# - Standard (=, <, >, !) omit automatic C padding (portable). Use these for file/network formats.


fmt = "<I H B"
data = struct.pack(fmt, 0xCAFEBABE, 512, 3) # bytes
assert struct.calcsize(fmt) == 4+2+1
vals = struct.unpack(fmt, data) # (3405691582, 512, 3)

print(vals)

fmt = '<I2sH' # id: uint32, tag: 2-bytes, value:uint16
buf = b''.join(struct.pack(fmt, i, b'tg', i*10) for i in range(1, 4))
for rec in struct.iter_unpack(fmt, buf):
    print(rec)


buf = bytearray(16)
struct.pack_into('<I', buf, 0, 0x12345678)
x, = struct.unpack_from('<I', buf, 0)
print(x)

fmt = '>8sI' # 8-byte string, uint32 (big-endian)
b = struct.pack(fmt, b'hi', 5) # string is padded with NULs
s, n = struct.unpack(fmt, b)
s = s.strip(b'\x00') # trim padding
print(s, n)

# Pascal string (p) behavior

fmt = '10p' # 10-byte field: first byte is length
b = struct.pack(fmt, b'hello') # stores length + data + padding
s, = struct.unpack(fmt, b)
print(s)


s = struct.Struct('<I H')
packed = s.pack(1, 2)
vals = s.unpack(packed)
print(vals)