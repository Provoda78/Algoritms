#include <iostream>

struct Node
{
    int key;
    int height;
    Node *left;
    Node *right;

    Node(int key, int height) : key(key), height(height), left(nullptr), right(nullptr) {}
};

class AVL
{
    int getHeight(Node *root)
    {
        return (root == nullptr) ? 0 : root->height;
    }

    int getBalanceFactor(Node *root)
    {
        if (root == nullptr)
            return 0;
        return getHeight(root->left) - getHeight(root->right);
    }

    void updateHeight(Node *root)
    {
        if (root != nullptr)
        {
            root->height = 1 + std::max(getHeight(root->left), getHeight(root->right));
        }
    }

    Node *turn_left(Node *x)
    {
        Node *y = x->right;
        Node *T = y->left;

        y->left = x;
        x->right = T;

        updateHeight(x);
        updateHeight(y);

        return y;
    }

    Node *turn_right(Node *x)
    {
        Node *y = x->left;
        Node *T = y->right;

        y->right = x;
        x->left = T;

        updateHeight(x);
        updateHeight(y);

        return y;
    }

    Node *Big_turn_right(Node *x)
    {
        x->left = turn_left(x->left);
        return turn_right(x);
    }

    Node *Big_turn_left(Node *x)
    {
        x->right = turn_right(x->right);
        return turn_left(x);
    }
};
