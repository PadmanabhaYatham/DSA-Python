from typing import List, Any


def get_longest_palindrome(string: str) -> str:
    """
    gets the longest palindrome from given string
    Args:
        string(str): input string

    Returns:
        Str: longest palindrome string
    """
    if len(string) <= 1:
        return string

    max_len = 1
    max_str = string[0]
    dp = [[False for _ in range(len(string))] for _ in range(len(string))]
    for i in range(len(string)):
        dp[i][i] = True
        for j in range(i):
            if string[j] == string[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                if i - j + 1 > max_len:
                    max_len = i - j + 1
                    max_str = string[j:i + 1]
    return max_str


def get_all_subsequences(indx: int, curr_pair: List[Any], result: List[Any], arr=None) -> List | None:
    """
    Gets the subsequences of given array
    Args:
        indx(int): Index of array where to start subarray
        curr_pair(List[Any]): current pair
        result(List[Any]): result array where we need to add su arrays
        arr(list, optional): array to get the subsequences, Defaults to [5,4,2,7,8].

    Returns:
        result(List[Any]): list of sub sequences
    """
    if arr is None:
        arr = [5, 4, 2, 7, 8]

    if indx == len(arr):
        result.append(curr_pair[:])
        # print(result)
        return

    curr_pair.append(arr[indx])
    get_all_subsequences(indx+1, curr_pair, result, arr)
    curr_pair.pop()
    get_all_subsequences(indx+1, curr_pair, result, arr)
    
    return result
    

if __name__ == '__main__':
    print(get_longest_palindrome("adgdhahaahahjsjhjh"))
    # print(get_all_subsequences(0, [], [], arr=[5, 4, 2, 1, 3]))
    
