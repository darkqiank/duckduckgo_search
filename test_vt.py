from engines import VT
import json
import time

for i in range(1):
    print(i)
    start_time = time.time()
    with VT(proxies="socks5://100.77.221.27:7890", timeout=20) as vt:
        res = vt.api(input_str='00000944c9e053f1c545ef1b4b21bfbf6f07265b6449bffdeb4b761c78416e6e')
        # res = vt.api(input_str='baidu.com')
        with open('vt.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
    end_time = time.time()
    print(f"Total time taken: {end_time-start_time} seconds")
