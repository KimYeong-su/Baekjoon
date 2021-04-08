#include <iostream>
#include <queue>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	queue<int> q;
	for (int i = 1; i < N+1; i++) {
		q.push(i);
	}
	int turn = 0;
	cout << "<";
	while (q.size() > 1) {
		turn += 1;
		if (turn == K) {
			turn = 0;
			cout << q.front() << ", ";
			q.pop();
		}
		else {
			q.push(q.front());
			q.pop();
		}
	}
	cout << q.front() << ">\n";
	return 0;
}