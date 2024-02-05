# IP INFO by HARDIK

This Python script provides information about an IP address using the ipinfo.io API. It displays details such as IP address, country, location, ISP, postal code, and coordinates.

## Dependencies

- **requests**: A library for making HTTP requests
  - Install using: `pip install requests`

- **pyfiglet**: A library for creating custom text banners using ASCII art
  - Install using: `pip install pyfiglet`

## Important Parts

- **Formatted String**: The `api_url` variable is a formatted string used to construct the API URL with the target IP address.
  - Example: `api_url = f"https://ipinfo.io/{ip_address}/json"`

- **JSON Format**: The script specifies that the information needed is in JSON (JavaScript Object Notation) format.
  - `response = requests.get(api_url)`: The request is made to the API, and the response is stored in the `response` variable.

- **Data Storage**: The information from the response is stored in the `data` dictionary for easier accessibility.
  - `data = response.json()`

- **Main Script Check**: The block `if __name__ == "__main__":` is used to determine whether the Python script is being run as the main script.
  - `banner()`: Invokes the `banner` function to display a custom text banner.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/hardikkum444/IPINFO---Hardik-Kumawat.git
    cd IPINFO---Hardik-Kumawat
    ```

2. Install the required dependencies:

    ```bash
    pip install requests
    pip install pyfiglet
    ```

3. Run the script:

    ```bash
    python3 ipinfo.py
    ```

4. Follow the prompts to enter the target IP address.

## Author

- **HARDIK** - [GitHub](https://github.com/hardik)

Feel free to contribute, open issues, or provide feedback.




[MIT License](LICENSE).
