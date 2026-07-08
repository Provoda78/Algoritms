#include <iostream>
#include <stack>

struct Node
{
    int key;
    Node *left;
    Node *right;

    Node(int value) : key(value), left(nullptr), right(nullptr) {}

    static Node *search(Node *root, int target)
    {
        if (root == nullptr || root->key == target)
        {
            return root;
        }

        if (root->key > target)
        {
            return search(root->left, target);
        }

        if (root->key < target)
        {
            return search(root->right, target);
        }
    }

    static Node *insert(Node *root, int value)
    {
        if (root == nullptr)
        {
            return new Node(value);
        }

        if (value > root->key)
        {
            root->right = insert(root->right, value);
        }

        else if (value < root->key)
        {
            root->left = insert(root->left, value);
        }

        return root;
    }

    static void inorder(Node *root)
    {
        if (root != nullptr)
        {
            inorder(root->left);
            std::cout << root->key << " ";
            inorder(root->right);
        }
    }

    static void order_w(Node *root)
    {
        std::stack<Node *> s;
        Node *current = root;

        while (current != nullptr || !(s.empty()))
        {
            while (current != nullptr)
            {
                s.push(current);
                current = current->left;
            }

            current = s.top();
            s.pop();
            std::cout << root->key << " ";
            current = current->right;
        }
    }

    static Node *findmin(Node *root)
    {
        if (root->left == nullptr)
        {
            return root;
        }

        return findmin(root->left);
    }

    static Node *deletNode(Node *root, int key)
    {
        if (root == nullptr)
        {
            return nullptr;
        }

        if (key < root->key)
        {
            root->left = deletNode(root->left, key);
        }

        else if (key > root->key)
        {
            root->right = deletNode(root->right, key);
        }

        else
        {

            if (root->left == nullptr)
            {
                Node *temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr)
            {
                Node *temp = root->left;
                delete root;
                return temp;
            }

            Node *temp = findmin(root->right);
            root->key = temp->key;
            root->right = deletNode(root->right, temp->key);
        }
        return root;
    }
};

int main()
{
    Node *root = nullptr;

    root = Node::insert(root, 50);
    root = Node::insert(root, 30);
    root = Node::insert(root, 20);
    root = Node::insert(root, 40);
    root = Node::insert(root, 70);
    root = Node::insert(root, 60);
    root = Node::insert(root, 80);

    std::cout << "Дерево (inorder): ";
    Node::order_w(root); // Выведет: 20 30 40 50 60 70 80
    std::cout << "\n";

    std::cout << "Удаляем узел 20 (листовой)\n";
    root = Node::deletNode(root, 20);
    Node::inorder(root); // Выведет: 30 40 50 60 70 80
    std::cout << "\n";

    std::cout << "Удаляем узел 30 (с одним потомком)\n";
    root = Node::deletNode(root, 30);
    Node::inorder(root); // Выведет: 40 50 60 70 80
    std::cout << "\n";

    std::cout << "Удаляем узел 50 (корень с двумя потомками)\n";
    root = Node::deletNode(root, 50);
    Node::inorder(root); // Выведет: 40 60 70 80
    std::cout << "\n";

    return 0;
}
