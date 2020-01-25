import java.util.HashSet;

class Solution {
    public int solution(int[] A) {
        int num = 1;
        HashSet<Integer> hset = new HashSet<Integer>();

        for (int i = 0 ; i < A.length; i++) {
            hset.add(A[i]);                     
        }

         while (hset.contains(num)) {
                num++;
            }

        return num;
    }
}