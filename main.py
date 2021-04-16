import pytest, os

from multiprocessing import Pool

device_infos = [{"platform_version": "5.1.1", "server_port": 4723, "device_port": 62001, "system_port": 8200},
                {"platform_version": "7.1.2", "server_port": 4725, "device_port": 62002, "system_port": 8201}]

def run_parallel(device_infos):
    pytest.main([f"--cmdopt={device_infos}",
                "--alluredir", "Reports"])
    os.system("allure generate Reports -o Reports/html --clean")
if __name__ == '__main__':
    with Pool(2) as pool:
        pool.map(run_parallel, device_infos)
        pool.close()
        pool.join()