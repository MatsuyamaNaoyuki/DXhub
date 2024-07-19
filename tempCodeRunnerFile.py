import struct

# バイナリデータ
binary_data = b'Q\xf9\x00\x00z\x00\x00\x00g\x00z\x00\x00\x00\x00\x002\x1d\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\xe8\x06\xacB\x97\xd9\x0e\xc1\x1dz\xe2A\xa8u\xa8B7\x831A\xdd\xf4LA\x83R\x00CP\x94\x08B\x02\xf8\x11A\x9a\xa4$C\x06`RBW\xff\xf2@\x91\xc4{CS\xe8\xb8B\x91?\xc4A\xb5\x98LC\xc2\xb1\x8fB\xc2/&A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Gj\x9fN\x11\x04\x02\x00\x01\x00\x00\x00+\x12P\xc8\x90\x01\x00\x00\x00\x00'

# バイナリデータを適切な形式でデコードするためのフォーマット
formats = [
    ('f', 4),  # 32ビット浮動小数点数
    ('d', 8),  # 64ビット浮動小数点数
    ('I', 4),  # 32ビット符号なし整数
    ('Q', 8)   # 64ビット符号なし整数
]

# デコード結果を表示するための関数
def decode_binary_data(binary_data, data_format, size):
    decoded_values = []
    offset = 0
    while offset + size <= len(binary_data):
        value, = struct.unpack_from(data_format, binary_data, offset)
        decoded_values.append(value)
        offset += struct.calcsize(data_format)
    return decoded_values

# 各フォーマットでデコードして結果を表示
for fmt, size in formats:
    decoded_values = decode_binary_data(binary_data, fmt, size)
    print(f"Format {fmt}: {decoded_values}\n")
