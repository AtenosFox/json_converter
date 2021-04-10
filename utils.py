def json_to_xml(json_data):
    result: str = ''

    for key in json_data:
        if isinstance(json_data[key], dict):
            list_data = [json_data[key]]
            json_data[key] = list_data
            if isinstance(json_data[key], list):
                for x in json_data[key]:
                    result += f'<{key}>\n'
                    result += json_to_xml(x)
                    result += f'</{key}>\n'
            else:
                node = f'<{key}> {json_data[key]} </{key}>'
                result += f'{node}\n'

        else:
            if isinstance(json_data[key], list):
                for x in json_data[key]:
                    result += f'<{key}>\n'
                    result += json_to_xml(x)
                    result += f'</{key}>\n'
            else:
                node = f'<{key}> {json_data[key]} </{key}>'
                result += f'{node}\n'
    return result

def pretify_xml(xml_data):
    data = xml_data.split('\n')
    tab_count = -1
    result_xml = []
    for line in data:
        if line:
            if line[0] == '<' and line[:2] != '</' and '</' in line:
                result_xml.append(('\t' * tab_count) + line)
            elif line[0] == '<' and line[:2] != '</':
                result_xml.append(('\t' * tab_count) + line)
                tab_count += 1
            elif line[:2] == '</':
                tab_count -= 1
                result_xml.append(('\t' * tab_count) + line)
        else:
            result_xml.append(line)
    return '\n'.join(result_xml)
