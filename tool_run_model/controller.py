from data_access import *
from variable import *
import shutil, os

def excute_code(file_path, language, code_test_name_file, code_train_name_file, input_file, output_file):
    os.chdir(file_path)
    if language == "python2":
        # active_venv
        output_test = os.popen(f"python {code_test_name_file}").read()
        print(output_test)
        output_train = os.popen(f"python {code_train_name_file}").read()
        print(output_train)
    elif language == "python3":
        # load result_file
        data_output = open(os.path.join(file_path, output_file), 'r').readlines()
        data_output = [x.replace("\n","").strip() for x in data_output if x != "" or x != None]
        # run code_train
        output_train = os.popen(f"{PYTHON3_VENV} {code_train_name_file}").read()
        print("Training...")
        print(output_train)
        # run code_test
        output_test = os.popen(f"{PYTHON3_VENV} {code_test_name_file} {input_file}").read()
        output_test = [x.replace("\n", "").strip() for x in output_test.split("\n")]
        output_test.remove("")
        count = 0
        for res, excute in tuple(zip(data_output, output_test)):
            if str(res) == str(excute):
                count += 1
        accuracy = round(float(count/len(data_output)), 5)
        print(accuracy)
        return accuracy
    elif language == "javascript":
        output_test = os.popen(f"node {code_test_name_file}").read()
        print(output_test)
        output_train = os.popen(f"node {code_train_name_file}").read()
        print(output_train)
    return None
        
def process_result():
    db = DataBase()
    result = db.get_result()
    result["status"] = "I"
    db.update_result(result)
    language = db.get_language(str(result["language_id"]))
    result["accuracy"] = excute_code(result["path_code"], language, result["code_test"], result["code_train"], "input.csv", "output.csv")
    result["status"] = "S"
    db.update_result(result)

process_result()