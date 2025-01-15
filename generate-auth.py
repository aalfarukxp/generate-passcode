from flask import Flask, request, jsonify
import pyotp

app = Flask(__name__)

@app.route("/generate-passcode", methods=["GET"])
def generate_google_authenticator_passcode():
    """
    API endpoint to generate a Google Authenticator passcode.
    """
    # Get the secret_key from the request arguments
    secret_key = request.args.get("secret_key")
    
    if not secret_key:
        return jsonify({"error": "Secret key is required"}), 400
    
    try:
        # Generate the TOTP passcode
        totp = pyotp.TOTP(secret_key)
        passcode = totp.now()
        return jsonify({"passcode": passcode})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
