/*python code is failing with TLE
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while(b):
            temp=(a&b)<<1
            a=a^b
            b=temp
        return a
*/
class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int temp=(a&b)<<1;
            a=a^b;
            b=temp;
        }
        return a;
    }
}
