from data_access import *
from variable import *
import shutil, os, subprocess
from datetime import datetime
import regex

def excute_code(result_path, code_test, code_train, train_data_path, test_data_path):
    try:
        full_file_path = os.path.join(MEDIA_PATH, result_path)
        # cd into full_file_path
        os.chdir(full_file_path)

        # Load result
        test_data = open(os.path.join(full_file_path, test_data_path), 'r').readlines()
        test_data = [x.replace("\n","").strip() for x in test_data if x != "" or x != None]
        
        # Load input
        train_data = open(os.path.join(full_file_path, train_data_path), 'r').readlines()
        train_data = [x.replace("\n","").strip() for x in train_data if x != "" or x != None]
        
        # excute test code and caculater accuracy
        count = 0
        list_test = []
        for inp, out in tuple(zip(train_data, test_data)):
            test_info = {}
            ttime = datetime.now().timestamp()
            output_test = subprocess.run(["python3", code_test], capture_output=True, text=True, input=inp)
            ttime = datetime.now().timestamp() - ttime
            test_info["time_excute"] = str(ttime)
            print(str(output_test.stdout).replace("\n","").strip())
            if str(out) == str(output_test.stdout).replace("\n","").strip():
                test_info["status"] = True
                count += 1
            else:
                test_info["status"] = False
                test_info["error"] = str(output_test.stderr)
            list_test.append(test_info)
        print(list_test)
        accuracy = round(float(count/len(test_data)), 5)
        return (accuracy, list_test)
    except Exception as exc:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error in excute_code in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))
    return (None, None)
    
def process_result():
    db = DataBase()
    language_id = db.get_language()
    result = db.get_result(language_id)
    try:
        if result != None:
            # update status result -> Inprocess
            result["status"] = "I"
            db.update_result(result)
            # get problem to get train data, test_data
            problem = db.get_problem(result["problem_id"])
            train_data_path = problem["train_data"]         # input.csv
            test_data_path = problem["test_data"]           # output.csv

            start_time = datetime.now().timestamp()
            match = regex.search(r"^(?P<result_path>[a-zA-Z0-9\/]+)\/", result["code_test"])
            result_path = match.group("result_path")
            result["accuracy"], result["result_info"] = excute_code(result_path, result["code_test"], result["code_train"], train_data_path, test_data_path)
            result["time_excute"] = round(datetime.now().timestamp() - start_time, 5)
            result["status"] = "S"
            db.update_result(result)
    except Exception as exc:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error in process_result in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))
        result["status"] = "F"
        result["accuracy"] = 0
        db.update_result(result)