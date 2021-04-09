import json

if __name__ == "__main__":
    with open('file/data.json') as f:
        read_json = json.load(f)

    head = '<?xml version="1.0" encoding="UTF-8" ?>'
    root_open = '<root>'
    root_close = '</root>'

    result = ""
    result = head + '\n' + root_open + '\n'

    for key in read_json:
        node = '\t<{key}>' + f'{read_json[key]}' + f'</{key}>'
        result += f'\t{node}\n'

    with open('file/result.xml', 'w') as f:
        result += root_close
        f.write(result)
