func possibleStringCount(word string) int {
    n, ans := len(word), 1

        for i:= 1; i < n; i++ {
            if word[i - 1] == word[i]{
                ans++
            }
        }
        return ans
    
}