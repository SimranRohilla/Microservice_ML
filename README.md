Steps to Run the Project without Docker

1.Create a Virtual Environment

python -m venv (your_virtual_env_name)

2.Activate the Environment

.\(your_virtual_env_name)\Scripts\Activate

3.Installing all the necessasy Dependencies

pip install -r requirements.txt



Steps to Run the Project with Docker

Ensure you have Docker contain in the System

1.docker build -t my-python-app .

2. docker run -d -p 5000:5000 --name python-container my-python-app


