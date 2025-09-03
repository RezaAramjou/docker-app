from flask import Flask, jsonify, request, make_response
import bleach # Import the bleach library for sanitizing

app = Flask(__name__)

# --- Dummy Database User ---
# In a real app, this would be a database lookup.
admin_user = {"email": "admin@juice-sh.op", "password": "admin_password"}

@app.route('/')
def home():
    # Use bleach.clean() to sanitize any input before displaying it.
    # Here, we'll sanitize a fictional 'name' parameter for demonstration.
    user_name = request.args.get('name', 'Guest')
    safe_name = bleach.clean(user_name)
    return f"Hello from demo app, {safe_name}"

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/login', methods=['POST'])
def login():
    # This is a mock login function to demonstrate remediation.
    # It checks for a specific user, preventing the SQLi 'OR 1=1' logic.
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # FIX for SQLi: Compare input against known values instead of building a query.
    # A real fix would use parameterized queries with a real database.
    if email == admin_user["email"] and password == admin_user["password"]:
        return jsonify({"status": "login successful"}), 200
    else:
        # Generic error message prevents user enumeration.
        return jsonify({"status": "invalid credentials"}), 401

@app.after_request
def add_security_headers(response):
    # FIX for XSS: Add security headers to every response.
    # This tells browsers to enable extra protections.
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
