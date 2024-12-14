import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True)

        print("", result.stdout)

        if result.stderr:
            print("error:\n", result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"error: {e}")


if __name__ == "__main__":
    python = "python3.12"
    encoder_qr = "QREncoder.py"
    encoder_color = "colorEncoder.py"
    encoder_text = "textEncoder.py"

    command = ""
    command += python + " " + encoder_qr + " & "
    command += python + " " + encoder_color + " & "
    command += python + " " + encoder_text

    run_command(command)
