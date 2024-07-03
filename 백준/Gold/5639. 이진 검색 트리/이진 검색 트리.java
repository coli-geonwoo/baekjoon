

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static int root;
    private static List<Node> nodes = new LinkedList<>();
    private static Node rootNode;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int index = 0;
        while (true) {
            String inputs = br.readLine();
            if (inputs == null) {
                break;
            }
            if (index == 0) {
                root = Integer.parseInt(inputs);
                rootNode = new Node(index, root);
                index++;
                continue;
            }
            rootNode.insert(new Node(index, Integer.parseInt(inputs)));
            index++;
        }
        post_order(rootNode);
    }

    private static void post_order(Node node) {
        if (node == null) {
            return;
        }
        post_order(node.left);
        post_order(node.right);
        System.out.println(node.value);
    }

    static class Node {
        int sequence;
        int value;
        Node left;
        Node right;

        Node(int sequence, int value) {
            this.sequence = sequence;
            this.value = value;
        }

        void insert(Node other) {
            if (other.value > value) {
                if (right == null) {
                    right = other;
                    return;
                } else {
                    right.insert(other);
                }
            } else {
                if (left == null) {
                    left = other;
                    return;
                } else {
                    left.insert(other);
                }
            }
        }
    }


}
