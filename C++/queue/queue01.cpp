// Queue in C++
#include <iostream>
#include <queue>

using namespace std;

// Print the queue
void showq(queue<int> gq) {
	queue<int> g = gq;
	while (!g.empty()) {
		cout << ' ' << g.front();
		g.pop();
	}
	cout << '\n';
}

int main() {
	queue<int> q1;
	for(int i=0; i<10;i++){
		q1.push(i);
	}

	cout << "The queue q1 is : ";
	showq(q1);

	cout << "\nq1.size()  : " << q1.size();
	cout << "\nq1.front() :  " << q1.front();
	cout << "\nq1.back()  :  " << q1.back();

	cout << "\nq1.pop()   : ";
	q1.pop();
	showq(q1);

	return 0;
}

/*  g++ -o queue01 -p queue01.cpp  */
