import sys
import re



def replace_dollar(text):
    pattern = re.compile(r'\$(.+?)\$', re.DOTALL)
    replaced_text = pattern.sub(lambda m: f'$`{m.group(1)}`$', text)
    return replaced_text


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = replace_dollar(content)

    output_filename = filename.replace('.md', '_re.md')
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_content)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python replace_dollar.py filename')
    else:
        main(sys.argv[1])
