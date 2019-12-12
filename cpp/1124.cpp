#include <iostream>
using namespace std;
main()
{
	// int che[100001]={0};
	// for (int i=2; i<=100000; i++)
	// {
	// 	if (che[i]==0)
	// 	{
	// 		int tmp=i;
	// 		for (int k=1; k<=18; k++)
	// 		{
	// 			for (int j=1; tmp*j<=100000; j++)
	// 			{
	// 				che[tmp*j]++;
	// 			}
	// 			if ((long long)tmp*i>100000) break;
	// 			tmp*=i;
	// 		}
	// 	}
	// }
	// int ans=0, a,b;
	// cin >>a >>b;
	// for (int i=a; i<=b; i++)
	// 	if (che[che[i]]==1) ans++;
	// cout <<ans;
    int era[100001];
	for (int i=0; i<100001; i++) era[i] = 1;
    era[0] = 0;
    era[1] = 0;
    int sosu[100001];
    static long cnt = 0;
	// 에라토스테네스의 체 만들기 (소수 찾기)
    for (long i=2; i<100001; i++){
		cout << i << "케이스 입니다";
        if (era[i] == 1){
			cout << i << "는 소수입니다.";
            sosu[cnt] = i;
			cnt ++;
			cout << cnt;
            for (long j=2; j<100001; j++){
                if (i*j > 100000) break;
				else {
					era[i*j] = 0;
				}
        	}
    	}
	}
	long tocnt = 0, a, b;
	cin >> a >> b; 
	for (long i=a; i<=b; i++){
		long temp = i;
		long kcnt = 0;
		while (temp > 1){
			for(long j=0; j<cnt; j++){
				if (temp % sosu[j] == 0){
					temp /= sosu[j];
					kcnt += 1;
					break;
				}
			}
		} 
		for (int j=0; j<kcnt; j++){
			if (kcnt == sosu[j]){
				tocnt++;
			}
		}
	}
	cout << tocnt;
}
