from tests import validate_schemas

def main():
    version = "2.0.0"  # Change this to "2.1.0" for testing the next version
    if validate_schemas(version):
        print(f"{version} JSON Schema pass! 🎉")
        # Optionally, update README or perform additional actions here
    else:
        print("JSON Schema validation failed.")

if __name__ == "__main__":
    main()