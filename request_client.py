import requests



url ='http://localhost:8000/api/notes/notes/'
headers = {"X-Auntification":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTY1OTA3NzksImlhdCI6MTYxNjE1ODc3OSwic3ViIjoiQSJ9.poFvVirVJRY2Ym-qO80zhwH1zxCRCPAj1lFGHBOveycUxqVFvL3Q2IMyQwTY4sJV_lzOoW9QofgH6hwjcS1hVCEmdOQV_S4B1KZHM4DMWgyfL1MVbtlKME-38gJ9BHVPwK7sLDVt4zQ269y9gebt9e6jvcp5qqARf-c-p88iHwS6tEejc8iLVh_XCBTMnP2cEl8BrI5yVoMWCpZBNgJA0LK7IRCkcQbPD4Om7XHeMUxsL4OjIwRz8ZKyF3TT8LNlMFozE39-JA3Fso4tM9N7uafyPDi04FiPuvEXN-lzC6raP7uRD1QMlWUR_npzyjdCSajseic-FoHNyRiia-Qz1JqDLblwKcLPvsYUXUm0Kbbx6BAB3SzmKXtRaKeGoEK_ioHII2f83LyiwDeWn5ao1Fj5MV11ka2PXyGY76vd6Wh0ToFglroz1MFFEVFNW6iD2Yb3z_BGFL42vypkEgbdYSpyHLon8LKbjO2vyzCSZc7uE-not9YdRHpxIVtNvRThszNmp-jDwAJ06ICZ-9rSRCoN3S0SmKogEj5lPsxeD1zF1xAGfpO5tJHQL5DzgnTPTqpkMZpQNOHmglkWiU2PU-7JL4o87Ub03m_b7aS2XoZdOMEoNQijV0OzSo2uS-ilaiDDajaPdRyyq0RQnj7G7EZGN5ZTPHMRCZeQZp_UQ-o"}
r = requests.get(url,headers=headers)
print(r)
data = {"text":"Boba","author":1,"type_of_text":1}
r = requests.post(url,headers = headers,data = data)
print(r)