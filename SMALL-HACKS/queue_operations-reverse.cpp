//Write a code to perform push from the back, pop from the front, get the size, get back and get front operations.
void push(queue<int> &q,int x)
{
    q.push_back(x);
}

int pop(queue<int> &q)
{
    int x=getFront(q);
    q.pop_front();
    
    return x;
}


int getSize(queue<int> &q)
{
    return q.size();
}

int getBack(queue<int> &q)
{
    return q.back();
}

int getFront(queue<int> &q)
{
    return q.front();
}
