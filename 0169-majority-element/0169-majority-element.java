class Solution {
    public int majorityElement(int[] nums) {

        Map<Integer, Integer> mapp = new HashMap<>();
        int n = nums.length;

        for(int num : nums){
            if(mapp.containsKey(num)){
                mapp.put(num, mapp.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        for(Map.Entry<Integer, Integer> count : mapp.entrySet()){
            Integer key = count.getKey();
            Integer val = count.getValue();

            if(val > n / 2){
                return key;
            }
        }
        
    }
}