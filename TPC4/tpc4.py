import re
import json

def csv_to_json(csv_file):
    
    with open(csv_file, 'r') as f:
        csv_content = f.read()

   
    lines = csv_content.split('\n')

    
    header_pattern = re.compile(r'(?P<field>[^,{}]+)(?P<list>{\d+(,\d+)?})?(?P<func>::\w+)?(?:,|$)')

    
    header = []
    for field in header_pattern.finditer(lines[0]):
        field_name = field.group('field')
        list_size = field.group('list')
        func_name = field.group('func')
        header.append((field_name, list_size, func_name))

    
    records = []
    for line in lines[1:]:
        
        if not line:
            continue

        
        fields = line.split(',')

        
        record = {}
        for i, (field_name, list_size, func_name) in enumerate(header):
            if list_size:
                
                list_size = list(map(int, list_size[1:-1].split(',')))
                field_values = [fields[i+j] for j in range(list_size[0])]
                record[field_name] = field_values
            elif func_name:
                
                field_values = [float(x) for x in fields[i].split(',') if x]
                if func_name == 'sum':
                    record[field_name] = sum(field_values)
                elif func_name == 'media':
                    record[field_name] = sum(field_values) / len(field_values)
            else:
                
                record[field_name] = fields[i]

        records.append(record)

    
    return json.dumps(records,ensure_ascii=False,indent=1)


csv_file = 'alunos5.csv'
json_data = csv_to_json(csv_file)
print(json_data)
