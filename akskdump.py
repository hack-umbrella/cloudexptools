import os
import threading

def check_property_files(property_file, result_file, lock):
    """
    Check if the xxx.properties file contains sensitive information such as password, accesskeyid, accesskey, 
    secret, accesskeysecret, accessesecret, accessid, secretkey.
    """
    if property_file.endswith(".properties") and os.path.isfile(property_file):
        with open(property_file, "r") as f:
            content = f.read()
            if ("password" in content.lower() or
                    "accesskeyid" in content.lower() or
                    "accesskey" in content.lower() or
                    "secret" in content.lower() or
                    "accesskeysecret" in content.lower() or
                    "accessesecret" in content.lower() or
                    "accessid" in content.lower() or
                    "secretkey" in content.lower()):
                lock.acquire()
                result_file.write(property_file + "\n")
                lock.release()

def read_property_files_in_1_txt():
    """
    Batch read the content of xxx.properties files in 1.txt file, 
    and print the file name if it contains sensitive information such as password, accesskeyid, accesskey, 
    secret, accesskeysecret, accessesecret, accessid, secretkey.
    """
    threads = []
    lock = threading.Lock()
    with open("1.txt", "r") as file, open("2222.txt", "w") as result_file:
        lines = file.readlines()
        for line in lines:
            property_file = line.strip()
            t = threading.Thread(target=check_property_files, args=(property_file,result_file,lock))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

read_property_files_in_1_txt()
