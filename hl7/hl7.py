import subprocess
import sys
import os
from generator.generator import generated_person, write_seed


def get_module_path() -> str:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)


def gen_birthday(date) -> str:
    date = date.split('-')
    date = date[2] + date[1] + date[0]
    return date


def send_hl7_message(order):
    path_to_hl7 = os.path.join(get_module_path(), 'bin\\')
    path_to_bin = f'{path_to_hl7}HL7_cmd.exe'
    path_to_hl7 = f'{path_to_hl7}test_{order}.hl7'
    with open(path_to_hl7, 'r', encoding='utf-8') as file:
        file_data = file.read()
    if order == 'sc':
        write_seed()
    patient_info = next(generated_person())
    file_data = file_data.replace('PATIENT_NAME',
                                  f'{patient_info.last_name}^{patient_info.first_name}^{patient_info.middle_name}')
    file_data = file_data.replace('BIRTH_DAY', f'{gen_birthday(patient_info.birthday)}')
    with open(f'{path_to_hl7}.tmp', 'w', encoding='utf-8') as file:
        file.write(file_data)
    cmd = f'{path_to_bin} -i nt.ris-x.com -fp {path_to_hl7}.tmp -r 1 -ct 1'
    returned_output = subprocess.check_output(cmd)
    print(returned_output.decode('cp1251'))
    os.remove(f'{path_to_hl7}.tmp')
