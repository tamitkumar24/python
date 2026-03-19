class SecretConnection:
    def __enter__(self):
        print("Opening secure connection...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing secure connection securely.")

with SecretConnection() as conn:
    print("Transmitting data...")
    
# Output:
# Opening secure connection...
# Transmitting data...
# Closing secure connection securely.