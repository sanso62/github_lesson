def decimal_to_hex(decimal_value):
    hex_value=""
    hex_num={0:"0", 1:"1", 2:"2", 3:"3", 
             4:"4", 5:"5", 6:"6", 7:"7",
             8:"8", 9:"9", 10:"a", 11:"b",
             12:"c", 13:"d", 14:"e", 15:"f"}
    
    while decimal_value>=16:
        decimal_value, remainer=divmod(decimal_value, 16)
        hex_value = hex_num[remainer] + hex_value
    hex_value="0x"+hex_num[decimal_value]+hex_value

    return hex_value