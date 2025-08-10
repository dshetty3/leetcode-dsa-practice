class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> res = new ArrayList<>();
        List<Integer> sol = new ArrayList<>();
        backtrack(nums, 0, res, sol);

        return res;
        
    }

    private void backtrack(int[] nums, int i, List<List<Integer>> res, List<Integer> sol){

        if(i == nums.length){
            res.add(new ArrayList<>(sol));
            return;
        }

        sol.add(nums[i]);
        backtrack(nums, i + 1, res, sol);
        sol.remove(sol.size() - 1);
        backtrack(nums, i + 1, res, sol);
        
    }
}