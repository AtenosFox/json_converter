import json
import utils

if __name__ == "__main__":
    with open('file/data.json') as f:
        json_data = json.load(f)
    print(json_data)
    head = '<?xml version="1.0" encoding="UTF-8" ?>'
    root_open = '<root>'
    root_close = '</root>'
    result = head + '\n' + root_open + '\n'
    result += utils.json_to_xml(json_data)
    result = utils.pretify_xml(result)

    with open('file/result.xml', 'w') as f:
        result += root_close
        f.write(result)