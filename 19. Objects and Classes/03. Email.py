class Email:
    def __init__(self, sender, receiver, contend):
        self.sender = sender
        self.receiver = receiver
        self.contend = contend
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self, ):
        return f"{self.sender} says to {self.receiver}: {self.contend}. Sent: {self.is_sent}"


emails = []

data = input()
while data != 'Stop':
    tokens = data.split()
    sender = tokens[0]
    receiver = tokens[1]
    contend = tokens[2]
    email = Email(sender, receiver, contend)
    emails.append(email)
    data = input()

send_emails = list(map(int, input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
