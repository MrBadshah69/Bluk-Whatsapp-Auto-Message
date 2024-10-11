
# WhatsApp Bulk Message Sender

A Python script to send personalized bulk WhatsApp messages using company names and WhatsApp numbers from a CSV file. This script leverages the `pywhatkit` library to automate message sending with a specified delay between each message.

## Features

- Send personalized WhatsApp messages to multiple contacts.
- Reads company names and WhatsApp numbers from a CSV file.
- Custom message template that includes company name dynamically.
- Sends messages with a 30-second delay between each contact.
- Automatically handles blank rows or incomplete data.

## Prerequisites

To run this script, you need:

- **Python 3.x** installed on your machine.
- The `pywhatkit` library for sending WhatsApp messages.
- A valid CSV file containing company names and WhatsApp numbers.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/WhatsApp-Bulk-Message-Sender.git
   cd WhatsApp-Bulk-Message-Sender
   ```

2. **Install the required dependencies:**

   Install the required libraries using `pip`:

   ```bash
   pip install pywhatkit
   ```

## Usage

1. **Prepare the CSV file:**

   The CSV file should contain two columns: `Company Name` and `WhatsApp Number`. The structure should look like this:

   ```csv
   Company Name,WhatsApp Number
   Company A,+1234567890
   Company B,+1987654321
   ```

2. **Customize the message template:**

   The default message template includes placeholders for the company name. You can modify the message in the script if needed:

   ```python
   message_template = f"Dear {{company_name}} Marketing Agency,\n\nMy name is Muhammad Arsalan, and I am a professional WordPress developer specializing in remote website development. I am available to assist your company with any website development or IT-related projects. Additionally, I offer custom website services tailored to your specific needs. All work can be conducted online, ensuring convenience and flexibility.\n\nFor your review, I have attached my resume and portfolio:\n- GitHub: https://github.com/MrBadshah69\n- LinkedIn: https://www.linkedin.com/in/muhammadarsalanmalik/\n- Resume: https://mrbadshah69.github.io/Muhammad-Arsalan.github.io/\n\nShould you have any projects or need assistance with remote work, please do not hesitate to reach out. Thank you for considering my application.\n\nBest regards,\nMuhammad Arsalan"
   ```

3. **Run the script:**

   After setting up the CSV and message template, run the script:

   ```bash
   python bulk_whatsapp_sender.py
   ```

   The script will automatically send WhatsApp messages to all contacts listed in the CSV file with a 30-second delay between each message.

## Example

An example CSV file (`contacts.csv`):

```csv
Company Name,WhatsApp Number
Brand's M*** (P++) L**,+1234****
ABC Marketing Ag**,+1987*****
XYZ Solutions,+1122334455
```

For each entry, the script will generate a message like this:

```
Dear {Company Name} Marketing Agency,

My name is Muhammad Arsalan, and I am a professional WordPress developer specializing in remote website development. I am available to assist your company with any website development or IT-related projects. Additionally, I offer custom website services tailored to your specific needs. All work can be conducted online, ensuring convenience and flexibility.  

For your review, I have attached my resume and portfolio:
- GitHub: https://github.com/MrBadshah69
- LinkedIn: https://www.linkedin.com/in/muhammadarsalanmalik/
- Resume: https://mrbadshah69.github.io/Muhammad-Arsalan.github.io/

Should you have any projects or need assistance with remote work, please do not hesitate to reach out. Thank you for considering my application.

Best regards,  
Muhammad Arsalan
```

## Handling Errors

### UnicodeDecodeError

If you encounter encoding errors while reading the CSV file, ensure that it is saved with `UTF-8` encoding. Alternatively, the script reads the file using `ISO-8859-1` encoding to handle non-UTF-8 characters.

### IndexError

If you encounter an index error, ensure that your CSV file has no blank rows and contains at least two columns (`Company Name` and `WhatsApp Number`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute by submitting issues or pull requests if you have suggestions for improvements.

## Author

- **Muhammad Arsalan**  
  - GitHub: [MrBadshah69](https://github.com/MrBadshah69)  
  - LinkedIn: [Muhammad Arsalan](https://www.linkedin.com/in/muhammadarsalanmalik/)  
