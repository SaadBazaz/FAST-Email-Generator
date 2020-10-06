
prepend = "i"
batches = [17, 18, 19, 20]
domain = "@nu.edu.pk"
emails = []

for batch in batches:
    for i in range (0, 2000):
        email = prepend + str(batch) + "{0:0=4d}".format(i) + domain
        print(email)
        emails.append(email)

print (emails)

emailers = ["Shuja", "Saad", "Laiba", "Areesha", "Iftikhar", "FPS FAST"]

import csv

with open('email-list.csv', mode='w') as mailing_list:
    mailing_writer = csv.writer(mailing_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    mailing_writer.writerow(emailers)
    j = 0
    for i in range (1, len(emails)):
        if i % len(emailers) == 0:
            mailing_writer.writerow(emails[j:i])
            j = i
