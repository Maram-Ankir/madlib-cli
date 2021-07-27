import re 

print("""
    Welcome to Madlib Game 

    MadLibs game is key words replaced with blanks. ... One player asks the other players, in turn, to contribute a   word of the specified type for each blank, but without revealing the context for that word.
    """)


input_list=['Adjective','Adjective','A First Name','Past Tense Verb','A First Name','Adjective','Adjective',
'Plural Noun','Large Animal','Small Animal',"A Girl's Nam",'Adjective','Plural Noun','Adjective','Plural Noun',
'Number 1-50',"First Name's",'Number','Plural Noun','Number','Plural Noun']

output_list=[]

def input_user():
    for i in range (len(input_list)):
        input_val=input(f'>> Enter {input_list[i]}')
        output_list.append(input_val)


if __name__== '__main__':
    input_user() 


def read_template(filepath: str) -> str:
    with open('text/text2.txt', 'r') as file:

        file_content = file.read()
    return file_content.strip()


def parse_template(content_file):
    modified_text=re.sub('{[^}]+}','{}',content_file)
    removed_str_parts=tuple(re.findall("{(.*?)}",content_file))
    return  modified_text, removed_str_parts

def merge(parse_text,userInp):
    return parse_text.format(*userInp)



def script_copy(merged_text):
    with open('text/text1.txt','wb') as write_file:
         return write_file.write(bytes(merged_text,'utf-8'))







