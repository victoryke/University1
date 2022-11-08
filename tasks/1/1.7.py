timestamp1_hour=int(input())
timestamp1_minute=int(input())
timestamp1_second=int(input())
timestamp2_hour=int(input())
timestamp2_minute=int(input())
timestamp2_second=int(input())
timestamp1 = timestamp1_hour*3600+timestamp1_minute*60+timestamp1_second;
timestamp2 = timestamp2_hour*3600+timestamp2_minute*60+timestamp2_second;
print(f'{timestamp2-timestamp1}')
