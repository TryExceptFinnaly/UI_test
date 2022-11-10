import subprocess
import sys
import os


def get_module_path() -> str:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)


def send_hl7_message():
    path_to_hl7 = os.path.join(get_module_path(), 'bin\\')
    cmd = f'{path_to_hl7}HL7_cmd.exe -i nt.ris-x.com -fp {path_to_hl7}test_sc.hl7 -r 1'
    returned_output = subprocess.check_output(cmd)
    print(returned_output.decode('cp1251'))
