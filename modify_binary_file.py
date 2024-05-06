def modify_binary_file(filename, offset, new_data):
    """
    :param filename:
    :param offset:
    :param new_data: 
    """
    with open(filename, 'r+b') as file: 
        file.seek(offset)  
        file.write(new_data)  

filename = '32kb.data'  
offset = 4096  
new_data = b'\x00\x01\x02\x03'  
modify_binary_file(filename, offset, new_data)
