def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    senders: dict = {}

    for line in handle:
        if line.startswith('From '):
            line = line.rstrip()
            line = line.split()
            sender: list = line[1]
            senders[sender] = senders.get(sender, 0) + 1
    
    the_sender = None
    largest = -1
    for key, value in senders.items():
        if value > largest:
            largest = value
            the_sender = key
        
    print(the_sender, largest)
    

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
