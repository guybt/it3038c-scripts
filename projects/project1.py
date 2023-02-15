import psutil

#finds the disk usage statistics (total, used, free) of the root directory (/) in bytes and assigns it to a variable
diskUsage =psutil.disk_usage ('/')

#converts free space attribute from bytes to gigabytes and assigns it to a variable
freeSpace = round(diskUsage.free / (1024 * 1024 * 1024), 2)

print("You have ", freeSpace, " GB of free space on your hard drive.")