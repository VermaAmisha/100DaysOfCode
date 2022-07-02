import smtplib

my_email = "amishaverma.2612@gmail.com"
password = "Amisha@123"

connection = smtplib.SMTP("smtp.gmail.com")

# "starttls" makes the connection secure tls is 'transport layer security'
connection.starttls()

connection.login(user=my_email , password=password)

connection.sendmail(from_addr=my_email , to_addrs="ankitaverma1501@gmail.com" ,msg="Hello")
connection.close()
