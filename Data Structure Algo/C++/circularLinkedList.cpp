#include<iostream>
using namespace std;

class Node{
    public:
        int data;
        Node *next;
        Node *prev;
        Node(){
            data=0;
            next=NULL;
            prev=NULL;
        }
        Node(int val){
            data=val;
            next=NULL;
            prev=NULL;
        }
};

class CircularLL{
    private:
        Node *head;
    public:
        CircularLL(){
            head=NULL;
        }
        
        bool isEmpty(){
            if(head==NULL){
                return true;
            }
            return false;
        }
        
        bool isFull(){
            Node *ptr=new Node;
            if(!ptr){
                return true;
            }
            delete ptr;
            return false;
        }

        void prependNode(int val){
            if(isFull()){
                cout<<"\nNo space left for new Nodes to be added." <<endl;
            }
            else{
                if(isEmpty()){
                    head=new Node(val);
                    head->next=head;
                    head->prev=head;
                }
                else{
                    Node *ptr=new Node(val), *last=head->prev;
                    last->next=ptr;
                    ptr->prev=last;
                    ptr->next=head;
                    head->prev=ptr;
                    head=ptr;
                }
                cout<<"\nNode with value " <<val <<" is Prepended at First." <<endl;
            }
        }

        void appendNode(int val){
            if(isFull()){
                cout<<"\nNo space left for new Nodes to be added." <<endl;
            }
            else{
                if(isEmpty()){
                    head=new Node(val);
                    head->next=head;
                    head->prev=head;
                }
                else{
                    Node *ptr=new Node(val), *last=head->prev;
                    ptr->prev=last;
                    ptr->next=head;
                    last->next=ptr;
                    head->prev=ptr;
                    last=ptr;
                }
                cout<<"\nNode with value " <<val <<" is Appended at Last." <<endl;
            }
        }

        void display(){
            if(isEmpty()){
                cout<<"\nNo elements present to display." <<endl;
            }
            else{
                Node *ptr=head;
                cout<<"\nPrinting all the values of Nodes: " <<endl;
                do{
                    cout<<"\t >> " <<ptr->data <<endl;
                    ptr=ptr->next;
                }while(ptr!=head);
            }
        }

        int deleteFirst(){
            if(isEmpty()){
                cout<<"\nNo elements present to display." <<endl;
                return -1;
            }
            Node *ptr=head->next;
            int val=ptr->data;
            ptr->prev=NULL;
            delete head;
            head=ptr;
            cout<<"\nNode with value " <<val <<" is Deleted from first." <<endl;
            return val;
        }

        int deleteLast(){
            if(isEmpty()){
                cout<<"\nNo elements present to display." <<endl;
                return -1;
            }
            Node *ptr=head->prev;
            int val=ptr->data;
            delete ptr;
            cout<<"\nNode with value " <<val <<" is Deleted from Last." <<endl;
            return val;
        }

        int count(){
            if(isEmpty()){
                cout<<"\nNo elements present." <<endl;
                return 0;
            }
            else{
                Node *ptr=head->next;
                int counter=1;
                while(ptr!=head){
                    counter++;
                    ptr=ptr->next;
                }
                cout<<"\n" <<counter <<" no. of Nodes are present in Circular LL." <<endl;
                return counter;
            }
        }

        int stackTop(){
            if(isEmpty()){
                cout<<"\nNo elements present to Return." <<endl;
                return -1;
            }
            else{
                cout<<"\nValue of Node at Stack-Top is: " <<head->data <<endl;
                return head->data;
            }
        }

        int stackBottom(){
            if(isEmpty()){
                cout<<"\nNo elements present to Return." <<endl;
                return -1;
            }
            else{
                int val=head->prev->data;
                cout<<"\nValue of Node at Stack-Bottom is: " <<val <<endl;
                return val;
            }
        }
};


int main(){
    
    int val, op;
    CircularLL cll;

    while(1){
        cout<<"Press 0. to Exit" <<endl;
        cout<<"Press 1. to Prepend Node" <<endl;
        cout<<"Press 2. to Append Node" <<endl;
        cout<<"Press 3. to Delete first element" <<endl;
        cout<<"Press 4. to Delete last element" <<endl;
        cout<<"Press 5. to check if Doubly LL is Full" <<endl;
        cout<<"Press 6. to check if Doubly LL is Empty" <<endl;
        cout<<"Press 7. to Display all elements" <<endl;
        cout<<"Press 8. to get StackTop" <<endl;
        cout<<"Press 9. to get StackBottom" <<endl ;
        cout<<"Press 10. to get count" <<endl <<endl <<"\t>> ";

        cin>>op;

        switch (op)
        {
        case 0:
            cout<<"\nSystem Exits..." <<endl;
            exit(0);
        
        case 1:
            cout<<"\nEnter the value to be Prepended: ";
            cin>>val;
            cll.prependNode(val);
            break;
        
        case 2:
            cout<<"\nEnter the value to be Appended: ";
            cin>>val;
            cll.appendNode(val);
            break;

        case 3:
            cout<<"\nDeleting First Node..." <<endl;
            cll.deleteFirst();
            break;

        case 4:
            cout<<"\nDeleting Last Node..." <<endl;
            cll.deleteLast();
            break;

        case 5:
            if(cll.isFull()){
                cout<<"\nMemory Overflow." <<endl;
            }
            else{
                cout<<"\nMore elements can be added to Linked List." <<endl;
            }
            break;

        case 6:
            if(cll.isEmpty()){
                cout<<"\nLinked List is Empty\nNo nodes present at the moment." <<endl;
            }
            else{
                cout<<"\nSome Nodes are already present in the Doubly LL." <<endl;
            }
            break;

        case 7:
            cll.display();
            break;
                
        case 8:
            cll.stackTop();
            break;

        case 9:
            cll.stackBottom();
            break;
                
        case 10:
            cll.count();
            break;
                
        default:
            cout<<"\nEnter a valid option b/w 0-9." <<endl;
            break;
        }
    }


    return 0;
}
