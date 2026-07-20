class Solution {
    private List<String> res = new ArrayList<>();
    private StringBuilder subset = new StringBuilder();

    private final String[] letters = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) return res;
        backtrack(0, digits);
        return res;
    }
     private void backtrack(int index, String digits) {
        if (index == digits.length()) {
            res.add(subset.toString());
            return;
        }

        String currentLetters = letters[digits.charAt(index) - '0'];

        for (int i = 0; i < currentLetters.length(); i++) {
            subset.append(currentLetters.charAt(i));
            backtrack(index + 1, digits);
            subset.deleteCharAt(subset.length() - 1);
        }
    }
}
