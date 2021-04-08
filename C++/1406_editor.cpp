#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	string s;
	stack<char> left, right;

	cin >> s;
	for (int a = 0; a < s.size(); a++) {
		left.push(s[a]);
	}

	int n;
	cin >> n;
	while (n--) {
		char order;
		cin >> order;
		if (order == 'L') {
			if (!left.empty()) {
				right.push(left.top());
				left.pop();
			}
		}
		else if(order == 'D') {
			if (!right.empty()) {
				left.push(right.top());
				right.pop();
			}
		}
		else if(order == 'B') {
			if (!left.empty()) {
				left.pop();
			}
		}
		else if (order == 'P') {
			char alpa;
			cin >> alpa;
			left.push(alpa);
		}
	}
	while (!left.empty()) {
		right.push(left.top());
		left.pop();
	}
	while (!right.empty()) {
		cout << right.top();
		right.pop();
	}
	cout << endl;
	return 0;
}