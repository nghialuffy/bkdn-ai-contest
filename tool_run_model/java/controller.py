from data_access import *
from variable import *
import shutil, os, subprocess
from datetime import datetime
import ntpath

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
        
        # copy data from problem to result
        os.system("cp -f '%s' '%s'" % (train_data_path , full_file_path))
        os.system("cp -f '%s' '%s'" % (test_data_path , full_file_path))

        # prepare to run
        code_test_file = ntpath.split(code_test)[1]
        compile_test = subprocess.run(["javac", code_test_file], capture_output=True, text=True)
        print("compile out %s " % str(compile_test.stdout))
        print("compile err %s " % str(compile_test.stderr))

        # excute test code and caculater accuracy
        count = 0
        list_test = []
        for inp, out in tuple(zip(train_data, test_data)):
            test_info = {}
            ttime = datetime.now().timestamp()
            output_test = subprocess.run(["java", code_test_file.replace(".java", "")], capture_output=True, text=True, input=inp)
            ttime = datetime.now().timestamp() - ttime
            test_info["time_execute"] = str(ttime)
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
    db.connect()
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
            result_path = ntpath.split(result["code_test"])[0]
            result["accuracy"], result["result_info"] = excute_code(result_path, result["code_test"], result["code_train"], train_data_path, test_data_path)
            result["time_execute"] = round(datetime.now().timestamp() - start_time, 5)
            result["status"] = "S"
            db.update_result(result)
    except Exception as exc:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error in process_result in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))
        result["status"] = "F"
        result["accuracy"] = 0
        db.update_result(result)