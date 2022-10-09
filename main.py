import requests
from multiprocessing.dummy import Pool

class Exploit:
    def __init__(self, domain):
        self.domain = domain
    
    def install(self):
        try:
            for a in path:
                r = requests.get(self.domain+a)
                if "?step=1" in r.text:
                    print("        [{}{}] > Vuln!".format(self.domain, a))
                    open('result.txt', 'a').write(self.domain+a+"\n")
                else:
                    print("        [{}{}] > Not Vuln!".format(self.domain, a))
        except:
            pass

def asuna(list):
    global website
    website = Exploit(list)
    website.install()

def main():
    print("""
        Wp-Install
        Author : angga1337
    """)
    global path
    path = [
        '/wp-admin/install.php',
        '/wp/wp-admin/install.php',
        '/wordpress/wp-admin/install.php'
    ]
    urList = open(input("        root@weblist~# "), "r").read().split("\n")
    thread = int(input("        root@threads~# "))
    print("\n")
    pool = Pool(thread)
    pool.map(asuna, urList)
    pool.close()
    pool.join

if __name__ == '__main__':
    main()
