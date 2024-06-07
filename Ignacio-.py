from flask import Flask, request

app = Flask(__name__)

@app.route('/run_chuck', methods=['POST'])
def run_chuck():
    chuck_file = request.files['chuck_file']
    # Save chuck_file and trigger ChucK process
    return 'ChucK process started'

@app.route('/run_python_exe', methods=['POST'])
def run_python_exe():
    python_exe_file = request.files['python_exe_file']
    # Save python_exe_file and trigger Python process
    return 'Python process started'

if __name__ == '__main__':
    app.run(debug=True)
