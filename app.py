from flask import Flask, jsonify, request,render_template
from model import compute_performance_metrics
from metrics import save_metrics, get_metrics
from database import init_db

app = Flask(__name__)

# Health Check Api
@app.route('/')
def home():
    return "Welcome to the ML Model Performance API!"

# Endpoint for trained model performance
@app.route('/train_model_result', methods=['GET'])
def train_model():
    # Loading the dataset and computing  metrics
    accuracy, f1 = compute_performance_metrics()
    
    # Save the metrics to the database
    save_metrics(accuracy, f1)
    
    return jsonify({"accuracy": accuracy, "f1_score": f1})

# Endpoint to retrieve metrics history
@app.route('/metrics-history', methods=['GET'])
def metrics_history():
    metrics = get_metrics()
    return render_template('metrics.html', metrics=metrics)
    # return jsonify(metrics)


@app.route('/metrics-json-history', methods=['GET'])
def metrics_json_history():
    metrics = get_metrics()
    return jsonify(metrics)

if __name__ == '__main__':
    init_db()#initializing the Database
    app.run(debug=True)
