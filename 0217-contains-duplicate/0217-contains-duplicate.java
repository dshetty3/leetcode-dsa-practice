class Solution {
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> sett = new HashSet<>();

        for(int n : nums){
            if(sett.contains(n)){
                return true;
            }
            sett.add(n);
        }

        return false;
        
    }
}