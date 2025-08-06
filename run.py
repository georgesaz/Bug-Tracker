import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))  # Default to 80 if PORT not set
    app.run(host='0.0.0.0', port=port)
