from difflib import SequenceMatcher
with open('Solution1.java') as file_1,open('Solution2.java') as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print (similarity_ratio*100)  #plagiarism detected