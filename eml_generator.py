import string
import time
import random

# Declaring Global Variables
_msgId = 0
_domains = ["enron.com", "test.comp.com", "behlocal.com"]
_letters = string.ascii_lowercase[:12]
_emailName = ""


def get_domain(domains):
    return random.choice(domains)


def get_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_emails(length):
    return get_name(_letters, length) + '@' + get_domain(_domains)


def get_msg_id():
    return random.randint(10000000, 999999999)


def create_template(_msgId, sender):
    template = {"Message-ID: <": _msgId,
                "From:": sender,
                "Subject:": "Welcome",
                "Date:": "Test",
                "To:": "Test",
                "Mime-Version:": "1.0"
                }

    timestr = time.strftime("%Y%m%d_%H%M")
    file = open(timestr + ".eml", "w")
    for k, v in template.items():
        s = str(k) + " " + str(v)
        file.write(s + "\n")
    file.close()


if __name__ == "__main__":
    sender = generate_random_emails(7)
    create_template(get_msg_id(), sender)