from data_access import *
from variable import *
import shutil, os, subprocess
from datetime import datetime

def excute_code(file_path, language, code_test_name_file, code_train_name_file, input_file, output_file):
    try:
        os.chdir(file_path)
        # Load result
        data_output = open(os.path.join(file_path, output_file), 'r').readlines()
        data_output = [x.replace("\n","").strip() for x in data_output if x != "" or x != None]
        # Load input
        data_input = open(os.path.join(file_path, input_file), 'r').readlines()
        data_input = [x.replace("\n","").strip() for x in data_input if x != "" or x != None]
        # excute
        if language == "python2":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run(["python", code_test_name_file], capture_output=True, text=True, input=inp)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "python3":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run([PYTHON3_VENV, code_test_name_file], capture_output=True, text=True, input=inp)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "c++":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                compile_test = subprocess.run(["g++", "-o", "output", code_test_name_file], capture_output=True, text=True)
                print("compile out %s " % str(compile_test.stdout))
                print("compile err %s " % str(compile_test.stderr))
                output_test = subprocess.run(["./output"], capture_output=True, text=True, input=inp)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "c":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                compile_test = subprocess.run(["gcc", "-o", "output", code_test_name_file], capture_output=True, text=True)
                print("compile out %s " % str(compile_test.stdout))
                print("compile err %s " % str(compile_test.stderr))
                output_test = subprocess.run(["./output"], capture_output=True, text=True, input=inp)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "java":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                compile_test = subprocess.run(["javac", code_test_name_file], capture_output=True, text=True)
                print("compile out %s " % str(compile_test.stdout))
                print("compile err %s " % str(compile_test.stderr))
                output_test = subprocess.run(["java", code_test_name_file.replace(".java", "")], capture_output=True, text=True, input=inp)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "javascript":
            os.system("cp -f '%s' '%s'" % (code_train_name_file , JAVASCRIPT_VENV))
            os.system("cp -f '%s' '%s'" % (code_test_name_file , JAVASCRIPT_VENV))
            os.chdir(JAVASCRIPT_VENV)
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run(["node", code_test_name_file], capture_output=True, text=True, input=inp)
                print(output_test)
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
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
    except Exception as exc:
        print("Error in excute code: %s" % str(exc))
    return (None, None)
    
def process_result():
    try:
        db = DataBase()
        result = db.get_result()
        if result != None:
            result["status"] = "I"
            db.update_result(result)
            language = db.get_language(str(result["language_id"]))
            problem = db.get_problem(result["problem_id"])
            input_test_file = problem["train_data"]     # input.csv
            result_file = problem["test_data"]          # output.csv
            start_time = datetime.now().timestamp()
            result["accuracy"], result["result_info"] = excute_code(result["path_code"], language, result["code_test"], result["code_train"], input_test_file, result_file)
            result["time_excute"] = round(datetime.now().timestamp() - start_time, 5)
            result["status"] = "S"
            db.update_result(result)
    except Exception as exc:
        print("Error in process_result: %s" % str(exc))
        result["status"] = "F"
