with open('1.txt', 'r', encoding='utf-8') as f1, open('2.txt', 'r', encoding='utf-8') as f2, \
        open('3.txt', 'r', encoding='utf-8') as f3, open('res.txt', 'w', encoding='utf-8') as f_res:
    f1_content = f1.readlines()
    f2_content = f2.readlines()
    f3_content = f3.readlines()
    files_list = [('1.txt', len(f1_content)), ('2.txt', len(f2_content)), ('3.txt', len(f3_content))]
    files_in_order = sorted(files_list, key=lambda x: x[1])
    for file in files_in_order:
        f_res.write(file[0])
        f_res.write('\n')
        f_res.write(str(file[1]))
        f_res.write('\n')
        if file[0] == '1.txt':
            f_res.writelines(f1_content)
            f_res.write('\n')
        elif file[0] == '2.txt':
            f_res.writelines(f2_content)
            f_res.write('\n')
        else:
            f_res.writelines(f3_content)
            f_res.write('\n')