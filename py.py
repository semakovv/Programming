from datetime import datetime
iso_string = "2023-11-15T14:30:00"
dt = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S")
dt = datetime.strftime(dt, "%m-%m-%dT%H:%M:%S")
print(dt)