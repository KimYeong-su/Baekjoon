#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int a[50][50];
int b[50][50];
int dx[] = { 1,-1,0,0,-1,-1,1,1 };
int dy[] = { 0,0,1,-1,-1,1,1,-1 };
int w, h;

void bfs(int x, int y, int cnt) {
	queue<pair<int, int>> q;
	b[x][y] = cnt;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int k = 0; k < 8; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (0 <= nx && nx < h && 0 <= ny && ny < w) {
				if (a[nx][ny] == 1 && b[nx][ny] == 0) {
					b[nx][ny] = cnt;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

int main() {
	while (true) {
		cin >> w >> h;
		if (w == 0 && h == 0) break;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> a[i][j];
				if (a[i][j] == 1) {
					b[i][j] = 0;
				}
				else {
					b[i][j] = 1;
				}
			}
		}
		int cnt = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (a[i][j] == 1 && b[i][j] == 0) {
					bfs(i, j, ++cnt);
				}
			}
		}
		cout << cnt << "\n";
	}
	return 0;
}