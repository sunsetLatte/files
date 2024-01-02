import os


def sort_files():
    files = os.listdir('sorted')
    result = []
    for file_ in files:
        with open(f'sorted/{file_}', 'r', encoding='utf8') as f:
            text = f.read()
            f.seek(0)
            result.append({'name': file_, 'count_lines': len(f.readlines()), 'text': text})

    sorted_files = sorted(result, key=lambda f: f['count_lines'])
    with open('result.txt', 'w', encoding='utf8') as f:
        for file_ in sorted_files:
            f.write(file_['name']+'\n')
            f.write(str(file_['count_lines'])+'\n')
            f.write(file_['text']+'\n')


sort_files()