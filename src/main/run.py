from myapp import create_app
from waitress import serve
import os

if __name__ == '__main__':
    print("Creating app...")
    app = create_app('production')
    print("Starting server...")
    try:
        serve(app, host='0.0.0.0', port=5000)
        print("Server started on http://0.0.0.0:5000")
    except Exception as e:
        print(f"Error starting server: {e}")
