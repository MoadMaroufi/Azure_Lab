from flask import Flask
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/numericalintegralservice/<lower>/<upper>')
def integrate(lower, upper):
    def numerical_integration(lower, upper, N):
        upper,lower=float(upper),float(lower)
        x = np.linspace(lower, upper, N + 1)
        dx = (upper - lower) / N
        y = np.abs(np.sin(x))
        area = np.sum(y[:-1] * dx) 
        return area

    Ns = [10, 100, 1000, 10000, 100000, 1000000]
    results = [numerical_integration(lower, upper, N) for N in Ns]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)