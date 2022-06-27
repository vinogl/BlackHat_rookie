import subprocess


def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = b'Fail to execute command. \n'
    finally:
        return output


if __name__ == '__main__':
    while True:
        command = input('<GL:#> ')
        response = run_command(command=command)

        print(response.decode('utf-8'))
