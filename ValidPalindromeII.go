/*
LeetCode 680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
*/

func validPalindrome(s string) bool {
	left, right := 0, len(s)-1
	for left < right{
			if s[left] == s[right]{
					left++
					right--
			} else {
					return isPal(s,left+1, right) || isPal(s,left, right-1)
			}
	}
	return true
}

func isPal(s string, left, right int) bool{
	for left < right{
			if s[left] == s[right]{
					left++
					right--
			} else{
					return false
			}
	}
	return true
}
