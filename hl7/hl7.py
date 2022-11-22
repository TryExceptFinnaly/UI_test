import subprocess
import sys
import os
from generator.generator import generated_person, write_seed

ID_MO = '777'
ID_ROOM = '333'


def get_module_path() -> str:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)


def send_hl7_message(order):
    path_to_hl7 = os.path.join(get_module_path(), 'bin\\')
    path_to_bin = f'{path_to_hl7}HL7_cmd.exe'
    path_to_hl7 = f'{path_to_hl7}test_{order}.hl7'
    with open(path_to_hl7, 'r', encoding='utf-8') as file:
        file_data = file.read()
    if order == 'sc':
        write_seed()
    patient_info = next(generated_person())
    # Identificator's
    file_data = file_data.replace('_ID_MO', ID_MO)
    file_data = file_data.replace('_ID_ROOM', ID_ROOM)
    # Patient info
    file_data = file_data.replace('PATIENT_NAME',
                                  f'{patient_info.last_name}^{patient_info.first_name}^{patient_info.middle_name}')
    file_data = file_data.replace('BIRTH_DAY',
                                  f'{patient_info.birth_year}{patient_info.birth_month}{patient_info.birth_day}')
    file_data = file_data.replace('PHONE_NUMBER', f'{patient_info.phone_number}')
    file_data = file_data.replace('PATIENT_SEX', f'{patient_info.sex}')
    file_data = file_data.replace('PATIENT_EMAIL', f'{patient_info.email}')
    file_data = file_data.replace('_ALLERGY_TYPE', f'{patient_info.allergy_type}')
    file_data = file_data.replace('_IDENTIFIER_TYPE', f'{patient_info.identifier_type}')
    # Study info
    file_data = file_data.replace('_TREATMENT_CASE', f'{patient_info.treatment_case}')
    file_data = file_data.replace('_PATIENT_CLASS', f'{patient_info.patient_class}')
    file_data = file_data.replace('_STATUS_CITO', f'{patient_info.is_cito}')
    with open(f'{path_to_hl7}.tmp', 'w', encoding='utf-8') as file:
        file.write(file_data)
    cmd = f'{path_to_bin} -i nt.ris-x.com -fp {path_to_hl7}.tmp -r 1 -ct 1'
    returned_output = subprocess.check_output(cmd)
    print(returned_output.decode('cp1251'))
    os.remove(f'{path_to_hl7}.tmp')
