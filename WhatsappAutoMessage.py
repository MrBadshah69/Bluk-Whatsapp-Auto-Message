import pywhatkit as kit
import time
import csv

# Path to your CSV file
csv_file = "contacts.csv"

# Message template
message_template = """Dear {company_name},

My name is Muhammad Arsalan, and I am a professional WordPress developer specializing in remote website development. I am available to assist your company with any website development or IT-related projects. Additionally, I offer custom website services tailored to your specific needs. All work can be conducted online, ensuring convenience and flexibility.  

For your review, I have attached my resume and portfolio:
- Resume: https://mrbadshah69.github.io/Muhammad-Arsalan.github.io/
- GitHub: https://github.com/MrBadshah69
- LinkedIn: https://www.linkedin.com/in/muhammadarsalanmalik/

Should you have any projects or need assistance with remote work, please do not hesitate to reach out. Thank you for considering my application.

Best regards,  
Muhammad Arsalan"""

# Function to send WhatsApp messages
def send_whatsapp_messages(csv_file):
    # Open the CSV file and read the contacts
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        
        # Skip the header row if it exists
        next(csvreader)
        
        # Loop through the CSV file and send messages
        for row in csvreader:
            company = row[0]
            number = row[1]
            
            # Personalize the message for each company
            message = message_template.format(company_name=company)
            
            # Send message (1 minute after the script starts to avoid issues)
            kit.sendwhatmsg(number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
            
            # Wait for 30 seconds before sending the next message
            time.sleep(60)
            
    print("All messages have been sent!")

# Call the function to send WhatsApp messages
send_whatsapp_messages(csv_file)
