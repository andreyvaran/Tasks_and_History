try:
    memory = {}
    prefix = 0
    while True:
        temp = input()
        temp = temp.strip()
        if temp == '{':
            prefix += 1
            continue
        elif temp == '}':
            prefix -= 1
            for i in memory:
                if len(i) > prefix + 1 and i[prefix] != '_' and i[prefix - 1] == '_':
                    del memory[i]
            continue
        else:
            a, b = temp.split('=')
            if b.isdigit() or b[0] == '-':
                memory[f'{prefix if prefix != 0 else ""}{a}'] = b
                continue
            b_with_prefix = f'{prefix if prefix != 0 else ""}{b}'
            if b_with_prefix in memory:
                print(memory[b_with_prefix])
                memory[f'{prefix if prefix != 0 else ""}{a}'] = memory[b_with_prefix]
            elif prefix > 0:
                temp_prefix = prefix
                while temp_prefix > 0:
                    temp_prefix -= 1
                    b_with_prefix_ = f'{temp_prefix if temp_prefix != 0 else ""}{b}'
                    if b_with_prefix_ in memory:
                        print(memory[b_with_prefix_])
                        memory[f'{prefix if prefix != 0 else ""}{a}'] = memory[b_with_prefix_]
                        break
            else:
                print(0)
                k = f'{prefix if prefix != 0 else ""}{a}'
                if k in memory and memory[k] != 0:
                    del memory[k]
except (ValueError,EOFError):
    pass





""""




"""