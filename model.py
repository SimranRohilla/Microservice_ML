from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

def compute_performance_metrics():
    # Loading  dataset mentioned in the folder i.e IRIS.csv
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    
    # Initialize model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Making predictions
    y_pred = model.predict(X_test)
    
    # Calculating metrics

    #Accuracy measures the proportion of correctly classified instances out of the total number of instances.
    #General Formula (Number of Correct Predictions)/(Number of Correct Predictions)
    accuracy = accuracy_score(y_test, y_pred)

    #The F1 Score is the harmonic mean of precision and recall.
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    return accuracy, f1