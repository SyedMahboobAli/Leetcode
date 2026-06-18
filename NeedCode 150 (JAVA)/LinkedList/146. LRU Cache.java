class LRUCache {

    private class Node{
        int key, value;
        Node next, prev;

        Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final Map<Integer,Node> map;
    private final Node head, tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.head = new Node(0,0); //Dummy node
        this.tail = new Node(0,0); // Dummy node
        head.next = tail;
        tail.prev = head;        
    }
    
    public int get(int key) {
        if(!map.containsKey(key)) return -1;

        Node node = map.get(key);
        moveToFront(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node node = map.get(key);
            node.value = value;
            moveToFront(node);
            return;
        }

        if(map.size() == capacity){
            Node lru = tail.prev;
            removeNode(lru);
            map.remove(lru.key);
        }
        
        Node newNode = new Node(key,value);
        addToFront(newNode);
        map.put(key,newNode);
    }

    private void moveToFront(Node node){
        removeNode(node);
        addToFront(node);
    }

    private void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addToFront(Node node){
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
