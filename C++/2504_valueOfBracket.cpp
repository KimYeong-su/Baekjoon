#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;

	stack<int> b;
	int answer = 0;
	int tmp = 1;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '(') {
			b.push(i);
			tmp *= 2;
		}
		else if (s[i] == '[') {
			b.push(i);
			tmp *= 3;
		}
		else if (s[i] == ')') {
			if (b.empty()) {
				answer = 0;
				break;
			}
			if (s[b.top()] == '(') {
				if (b.top() + 1 == i) answer += tmp;
				b.pop();
				tmp /= 2;
			}
			else {
				answer = 0;
				break;
			}
		}
		else if (s[i] == ']') {
			if (b.empty()) {
				answer = 0;
				break;
			}
			if (s[b.top()] == '[') {
				if (b.top() + 1 == i) answer += tmp;
				b.pop();
				tmp /= 3;
			}
			else {
				answer = 0;
				break;
			}
		}
	}
	if (!b.empty()) {
		answer = 0;
	}
	cout << answer << endl;
	return 0;
}