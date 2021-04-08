#include <iostream>
#include <algorithm>
using namespace std;
int N;
int a[25][25];
int visit[25][25];
int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,-1,1 };
int answer[25 * 25];

void dfs(int x, int y, int cnt) {
	visit[x][y] = cnt;
	for (int k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (0 <= nx && nx < N && 0 <= ny && ny < N) {
			if (a[nx][ny] == 1 && visit[nx][ny] == 0) {
				dfs(nx, ny, cnt);
			}
		}
	}
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		char str[25];
		cin >> str;
		for (int j = 0; j < N; j++) {
			a[i][j] = str[j] - '0';
			visit[i][j] = 0;
		}
	}
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (a[i][j] == 1 && visit[i][j] == 0) {
				dfs(i, j, ++cnt);
			}
		}
	}
	cout << cnt << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			answer[visit[i][j]] += 1;
		}
	}
	sort(answer + 1, answer + cnt + 1);
	for (int i = 1; i <= cnt; i++) {
		cout << answer[i] << endl;
	}
	return 0;
}