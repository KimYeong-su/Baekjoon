#include <iostream>
#include <algorithm>
using namespace std;
int dest[1001];
int n, T;
bool visit[1001];


void cycle(int s) {
	if (visit[s]) return;
	visit[s] = true;
	cycle(dest[s]);
}

int main() {
	cin >> T;
	for (int tc = 0; tc < T ; tc++) {
		cin >> n;
		int cnt = 0;
		for (int i = 1; i < n+1; i++) {
			cin >> dest[i];
			visit[i] = false;
		}
		for (int s = 1; s < n+1; s++) {
			if (visit[s] == false) {
				cycle(s);
				cnt += 1;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}