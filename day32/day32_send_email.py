import smtplib

my_email = "qwerty@gmail.com"
password = "123456"

# connection = smtplib.SMTP("smtp.gmail.com")

# # "starttls" makes the connection secure tls is 'transport layer security'
# connection.starttls()

# connection.login(user=my_email , password=password)

# connection.sendmail(from_addr=my_email , 
# to_addrs="tyuiop@gmail.com" ,
# msg="Subject:Hello\n\nThis the mail I am sending you via Python code!!!")
# connection.close()

# # # # # To avoid closing the connection separately # # # # #

with smtplib.SMTP("smtp.gmail.com") as connection:

    # "starttls" makes the connection secure tls is 'transport layer security'
    connection.starttls()

    connection.login(user=my_email , password=password)

    connection.sendmail(from_addr=my_email , 
    to_addrs="tyuiop@gmail.com" ,
    msg="Subject:Hello\n\nThis the mail I am sending you via Python code!!!")
    
