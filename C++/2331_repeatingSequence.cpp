#include <iostream>
using namespace std;
int check[1000000];

int pow(int a, int p) {
	int ans = 1;
	while (p--) {
		ans *= a;
	}
	return ans;
}

int next(int a, int p) {
	int ans = 0;
	while (a > 0) {
		ans += pow(a%10, p);
		a /= 10;
	}
	return ans;
}

int sequence(int a, int p, int cnt) {
	if (check[a] != 0) {
		return check[a] - 1;
	}
	check[a] = cnt;
	int b = next(a, p);
	return sequence(b, p, cnt+1);
}

int main() {
	int A, P;
	cin >> A >> P;
	cout << sequence(A, P, 1) << endl;
	return 0;
}