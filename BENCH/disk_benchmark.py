import os;
import time;

def disk_performance():
    file_size_mb = 100
    file_name = "test_file_bin"

    #escritura
    start_time = time.time()
    with open(file_name, "wb") as file:
        file.write(os.urandom(file_size_mb * 1024 * 1024))
    write_duration = time.time() - start_time

    #lectura
    start_time = time.time()
    with open(file_name, "rb") as file:
        content = file.read()
    read_duration = time.time() - start_time

    os.remove(file_name)
    print(f"escritura del disco: {write_duration} Seconds")
    print(f"lectura del disco: {read_duration} Seconds")

if __name__ == "__main__":
    disk_performance()