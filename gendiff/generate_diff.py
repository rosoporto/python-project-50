import json


def to_str(value):
    if type(value) is bool:
        return str(value).lower()
    return value


def get_data_files(json_file1, json_file2):
    with open(json_file1, 'r') as f1, open(json_file2, 'r') as f2:
        data_f1 = json.load(f1)
        data_f2 = json.load(f2)
    return data_f1, data_f2


def output_data(list_results):
    output = '{\n'
    for result in list_results:
        output += result + '\n'
    output += '}'
    return output


def generate_diff(json_file1, json_file2, to_output=True):
    dict_1, dict_2 = get_data_files(json_file1, json_file2)
    shared_keys = set(dict_1.keys() | dict_2.keys())
    results_list = []
    for key in sorted(shared_keys):
        if key in dict_1 and key not in dict_2:
            results_list.append(f'  - {key}: {to_str(dict_1[key])}')
        elif key in dict_2 and key not in dict_1:
            results_list.append(f'  + {key}: {to_str(dict_2[key])}')
        elif dict_1[key] != dict_2[key]:
            results_list.append(f'  - {key}: {to_str(dict_1[key])}')
            results_list.append(f'  + {key}: {to_str(dict_2[key])}')
        else:
            results_list.append(f'    {key}: {to_str(dict_1[key])}')
    result = output_data(results_list)
    if to_output:
        print(result)
    else:
        return result


def main():
    json_file1 = 'tests/fixtures/file1.json'
    json_file2 = 'tests/fixtures/file2.json'
    generate_diff(json_file1, json_file2)


if __name__ == '__main__':
    main()
