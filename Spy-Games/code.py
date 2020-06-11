# --------------
#Code starts here
path=file_path
#Function to read file
def read_file(path):
    file=open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence
sample_message=read_file(path) 
print(sample_message) 
 
#Function to fuse message

def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)

#Function to substitute the message
def substitute_msg(message_c):
    sub=''
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Marine Biologist'
    else:
        pass
    return sub

#Calling the function to read file
message_3=read_file(file_path_3)
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)

#Function to compare message
def compare_msg(message_d,message_e):
    a_list=message_d.split(' ')
    b_list=message_e.split(' ')
    c_list=[i for i in a_list if i not in b_list]
    final_msg= ' '.join(word for word in c_list)
    return final_msg
    
#Calling the function to read file
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
secret_msg_3= compare_msg(message_4,message_5)
print(secret_msg_3)

#Function to filter message
def extract_msg(message_f):
    a_list= message_f.split(' ')
    even_word= lambda x: True if len(x) % 2 == 0 else False
    b_list= list(filter(even_word, a_list))
    final_msg= ' '.join(word for word in b_list)
    return final_msg
    
    
#Calling the function to read file
message_6=read_file(file_path_6)
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg= ' '.join(word for word in message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()


#Calling the function to write inside the file    
write_file('secret_msg',final_path)
print(secret_msg)
#Printing the entire secret message


#Code ends here




