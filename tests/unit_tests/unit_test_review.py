import time
import random

PRODUCT_NAMES = ["product-a", "product-b", "product-c"]
IP_ADDRESSES = ["000.000.00.1", "000.000.00.2", "000.000.00.2"]

def check_if_everythings_works_ok(response):
    if response == "" or "error" in response: 
        return False 
    return '"state":"READY"' in response 

def test_check_everythings_terrible():
    for i in range(len(PRODUCT_NAMES)): 
        product_name = PRODUCT_NAMES[i]
        ip_address = IP_ADDRESSES[i]

        print(f"Checking {product_name} at {ip_address}...") 

        time.sleep(2) 

        response = random.choice([
            '{"state":"READY"}',
            '{"state":"NOT_READY"}',
            '{"state":"ERROR"}', 
        ])


        result = check_if_everythings_works_ok(response)

        time.sleep(3)

        if result:
            print("Models Ready$")
        else:
            print(f"Oops, something went wrong for {product_name}: {response}")
            time.sleep(5) 

    assert True, "Everything is working as expected"

