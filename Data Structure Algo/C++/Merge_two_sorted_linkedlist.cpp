// Merge 2 sorted linked list
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fio                       \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
class node
{
public:
    int data;
    node *next;
    node(int val)
    {
        data = val;
        next = NULL;
    }
};
void insertattail(node *&head, int val)
{

    node *n = new node(val);

    if (head == NULL)
    {
        head = n;
        return;
    }

    node *temp = head;
    while (temp->next != NULL)
    {
        temp = (temp->next);
    }
    temp->next = n;
}
void display(node *head)
{

    while (head != NULL)
    {
        cout << (head->data) << "->";
        head = head->next;
    }
    cout << "NULL\n";
}

int length(node *head)
{
    int c = 0;
    while (head != NULL)
    {
        head = head->next;
        c++;
    }
    return c;
}
node *merge(node *&head1, node *&head2)
{
    node *p1 = head1;
    node *p2 = head2;
    node *dummynode = new node(-1);
    node *p3 = dummynode;
    while (p1 != NULL && p2 != NULL)
    {
        if (p1->data < p2->data)
        {
            p3->next = p1;
            p1 = p1->next;
        }
        else
        {
            p3->next = p2;
            p2 = p2->next;
        }
        p3 = p3->next;
    }
    while (p1 != NULL)
    {
        p3->next = p1;
        p1 = p1->next;
        p3 = p3->next;
    }
    while (p2 != NULL)
    {
        p2->next = p1;
        p1 = p1->next;
        p2 = p2->next;
    }
    return dummynode->next;
}
node *mergerecursive(node *&head1, node *&head2)
{
    if (head1 == NULL)
        return head2;
    if (head2 == NULL)
        return head1;
    node *res;
    if (head1->data < head2->data)
    {
        res = head1;
        res->next = mergerecursive(head1->next, head2);
    }
    else
    {
        res = head2;
        res->next = mergerecursive(head1, head2->next);
    }
    return res;
}
int32_t main()
{
    fio
        node *head1 = NULL;
    node *head2 = NULL;
    for (int i = 1; i <= 7; i += 2)
        insertattail(head1, i);

    for (int i = 0; i <= 7; i += 2)
        insertattail(head2, i);

    display(head1);
    display(head2);
    node *newnode = mergerecursive(head1, head2);
    display(newnode);
    cerr
        << "processor time: " << clock() / (double)CLOCKS_PER_SEC << "s    ";

    return 0;
}
// Time-O(N+M)