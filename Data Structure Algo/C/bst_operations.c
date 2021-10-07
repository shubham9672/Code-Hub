#include <stdio.h>
#include <stdlib.h>

struct bst
{
    int data;
    struct bst *lchild;
    struct bst *rchild;
};

struct bst *newnode(int val)
{
    struct bst *ptr = malloc(sizeof(struct bst));
    ptr->data = val;
    ptr->lchild = NULL;
    ptr->rchild = NULL;

    return ptr;
}

struct bst *insert(struct bst *root, int val)
{
    if (root == NULL)
    {
        return newnode(val);
    }
    else if (root->data < val)
    {
        root->rchild = insert(root->rchild, val);
    }
    else if (root->data > val)
    {
        root->lchild = insert(root->lchild, val);
    }

    return root;
}

struct bst *search(struct bst *root, int key)
{
    if (root == NULL)
    {
        return NULL;
    }
    if (root->data == key)
    {
        return root;
    }
    else if (key < root->data)
    {
        return search(root->lchild, key);
    }
    else
    {
        return search(root->rchild, key);
    }
}

struct bst *iterative_search(struct bst *root, int key)
{
    while (root != NULL)
    {
        if (root->data == key)
        {
            return root;
        }
        else if (root->data > key)
        {
            root = root->lchild;
        }
        else
        {
            root = root->rchild;
        }
    }
    return NULL;
}

struct bst *predecessor(struct bst *root)
{
    root = root->lchild;
    while (root->rchild != NULL)
    {
        root = root->rchild;
    }
    return root;
}

struct bst *delete (struct bst *root, int val)
{
    struct bst *ipre;
    if (root == NULL)
    {
        return NULL;
    }

    if (root->lchild == NULL && root->rchild == NULL)
    {
        free(root);
        return NULL;
    }

    if (root->data > val)
    {
        root->lchild = delete (root->lchild, val);
    }
    else if (root->data < val)
    {
        root->rchild = delete (root->rchild, val);
    }

    else
    {
        ipre = predecessor(root);
        root->data = ipre->data;
        root->lchild = delete (root->lchild, ipre->data);
    }
    return root;
}

void inorder(struct bst *root)
{
    if (root == NULL)
        return;

    inorder(root->lchild);
    printf("%d\t", root->data);
    inorder(root->rchild);
}

int main()
{
    struct bst *root = NULL;
    int choice, num;

    while (1)
    {
        printf(">>>>>Available choices<<<<<\n\n");
        printf("1.Insert the elements into bst\n");
        printf("2.Delete the element from bst\n");
        printf("3.Search for a number from the bst(recursive search)\n");
        printf("4.Search for a number from the bst(iterative search)\n");
        printf("5.Print inorder sequence for the bst\n");
        printf("6.Quit \n");

        printf("Enter your choice : ");
        scanf("%d", &choice);

        switch (choice)
        {

        case 1:
            printf("Enter the element to be inserted to the tree : ");
            scanf("%d", &num);
            root = insert(root, num);
            printf("%d inserted to the tree\n\n",num);

            // insert(A, num, n);
            // n = n + 1;
            break;
        case 2:
            printf("Enter the elements to be deleted from the tree: ");
            scanf("%d", &num);
            delete (root, num);
            printf("\n");
            // delete (A, num, n);
            break;
        case 3:
            printf("Enter the elements to be searched from the tree: ");
            scanf("%d", &num);
            struct bst *ptr = search(root, num);
            if (ptr != NULL)
            {
                printf("%d found in bst\n\n", ptr->data);
            }
            else
            {
                printf("element not found in bst\n\n");
            }
            // display(A);
            break;
        case 4:
            printf("Enter the elements to be searched from the tree: ");
            scanf("%d", &num);
            struct bst *ptr2 = iterative_search(root, num);
            if (ptr2 != NULL)
            {
                printf("%d found in bst\n\n", ptr2->data);
            }
            else
            {
                printf("element not found in bst\n\n");
            }
        case 5:
            printf("Inorder sequence for the above bst is:  ");
            inorder(root);
            printf("\n\n");
            break;
        case 6:
        printf("EXITTING...\n");
            exit(0);
        default:
            printf("Invalid choice \n");
            printf("Enter from the available choices only\n\n");
        }
    }

    return 0;
}