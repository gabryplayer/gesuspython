import time

x = """  http://185.145.86.131:82
 http://185.145.86.131:81
 http://188.9.108.125:80
 http://151.84.63.58:80
 http://91.214.60.215:80
 http://83.211.180.206:80
 http://37.77.101.48:80
 http://79.62.233.205:89
 http://151.97.133.170:80
 http://194.116.11.176:80
 http://46.234.229.169:80
 http://77.32.81.120:80
 http://89.150.39.221:86
 http://194.116.8.10:83
 http://194.116.8.10:84
 http://194.116.8.10:86
 http://194.116.8.10:85
 http://194.116.8.10:89
 http://93.49.2.196:8081
 http://93.49.2.196:8083
 http://93.49.2.196:8082
 http://93.49.2.196:8080
 http://93.49.2.196:8084
 http://159.255.152.116:60001
 http://188.12.182.58:81
 http://46.21.183.56:80
 http://82.62.98.148:90
 http://82.62.98.148:91
 http://188.14.157.66:80
 http://87.26.188.210:3000
 http://87.26.188.210:2000
 http://185.37.205.130:80
 http://31.196.1.214:84
 http://83.211.37.161:81
 http://188.11.27.179:80
 http://93.70.236.56:85
 http://87.27.218.8:80
 http://95.255.183.164:8080
 http://2.40.36.158:8084
 http://195.103.108.145:82
 http://195.103.108.145:81
 http://195.103.108.145:85
 http://195.103.108.145:84
 http://94.81.229.117:81
 http://94.81.229.117:82
 http://94.81.229.117:85
 http://109.115.124.92:81
 http://185.128.149.65:8082
 http://188.14.157.65:80
 http://79.8.52.211:88
 http://79.8.52.211:89
 http://213.182.95.96:9015
 http://193.138.5.192:80
 http://185.158.239.53:81
 http://217.133.31.26:80
 http://46.141.92.2:81
 http://217.133.33.211:80
 http://46.141.57.188:80
 http://82.113.203.98:82
 http://80.88.166.43:90
 http://188.10.134.166:88
 http://213.187.17.124:8081
 http://82.180.38.145:8080
 http://185.85.25.87:80
 http://37.77.163.122:80
 http://193.178.137.50:80
 http://62.110.217.34:8080
 http://93.39.64.30:81
 http://2.224.241.14:84
 http://2.35.32.6:81
 http://2.40.45.90:80
 http://2.42.203.84:80
 http://185.56.157.187:81
 http://185.158.239.53:83
 http://93.48.237.53:80
 http://5.94.175.56:80
 http://128.116.236.55:3000
 http://37.99.254.198:83
 http://93.46.116.184:8000
 http://92.245.172.177:8083
 http://79.8.16.194:80
 http://82.62.154.117:81
 http://94.101.60.53:80
 http://92.245.172.177:8082
 http://88.34.237.193:81
 http://2.115.69.178:8081
 http://2.115.69.178:8080
 http://185.139.50.106:8080
 http://78.134.96.136:80
 http://213.182.82.116:8001
 http://82.62.154.117:83
 http://62.170.136.109:8001
 http://185.128.149.87:8081
 http://79.0.95.68:83
 http://79.0.95.68:85
 http://217.59.61.46:80
 http://91.214.60.211:80
 http://185.20.64.215:83
 http://93.38.112.181:8081
 http://2.47.141.164:8084
 http://185.56.157.187:83
 http://217.61.172.168:82
 http://185.56.157.187:80
 http://79.10.24.158:80
 http://195.32.37.157:9000
 http://88.147.108.145:80
 http://185.229.174.139:91
 http://185.37.205.121:80
 http://194.32.175.101:80
 http://83.139.244.70:81
 http://83.139.244.70:84
 http://83.139.244.70:82
 http://83.139.244.70:83
 http://89.97.231.70:8083
 http://89.97.231.70:8082
 http://89.97.231.70:8084
 http://89.97.231.70:8090
 http://151.8.241.70:8080
 http://185.51.139.42:8080
 http://93.38.57.20:8080
 http://91.214.60.213:80
 http://185.85.22.208:8080  """
b = "_______________________"


print(" _______________________________________________________________________________")     
print("¦ ---------------------------------OPIVERET3------------------------------------¦")
print("¦...............................................................................¦")
print("---------------------------------------------------------------------------------")
p = input("how much link do you want to gen /max 1 million/: ")

if  p.isdigit() and 1 <= int(p) <= 1000000:
 time.sleep(5)
 for _ in range(1000000):
    print(x)
 else:
   print("Invalid Number")