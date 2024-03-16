#include <stdio.h>
#define SIZE 100

int queue[SIZE];
int front = -1;
int rear = -1;

void enqueue(int item) {
    if (rear == SIZE - 1) {
        printf("Queue is Full\n");
    } 
    else {
        if (front == -1){
            front = 0;
        }
        rear++;
        queue[rear] = item;
        printf("Inserted -> %d\n", item);
    }
}

void dequeue() {
    if (front == -1) {
        printf("Queue is Empty\n");
    } 
    else {
        printf("Removed -> %d\n", queue[front]);
        front++;
        if (front > rear)
            front = rear = -1;
    }
}

void display() {
    if (rear == -1) {
        printf("Queue is Empty\n");
    } else {
        int i;
        printf("Queue: ");
        for (i = front; i <= rear; i++)
            printf("%d ", queue[i]);
        printf("\n");
    }
}

int main() {
    int choice, value;
    printf("Queue Implementation using Array ::\n");
    for(int i=0; i<10; i++){
    	enqueue(i);
    }
    display();
    while(rear > -1){
    	dequeue();
    	display();
    }
    return 0;
}

/* gcc queue02.c -o q2 */
