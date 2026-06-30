class MedianFinder {
    private PriorityQueue<Integer> low; //max Heap
    private PriorityQueue<Integer> high; //min Heap

    public MedianFinder() {
        low = new PriorityQueue<>(Collections.reverseOrder());
        high = new PriorityQueue<>();
    }
    
    public void addNum(int num) {

        low.offer(num);

        high.offer(low.poll());

        if(low.size() < high.size()){
            low.offer(high.poll());
        }
        
    }
    
    public double findMedian() {

        if(low.size() > high.size())
            return low.peek();
        else
            return (low.peek() + high.peek()) / 2.0 ;    
    }
}

/*
Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

For the first follow-up:

Since all values are in a small fixed range, I would replace the two heaps with a frequency array of size 101 and compute the median by scanning counts.

For the second:

I would use a hybrid solution: a counting array for the common [0,100] values and heaps or another ordered structure for the rare outliers.


*/

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
