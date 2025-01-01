from typing import List, Any


def get_all_subsequences(indx: int, curr_pair: List[Any], result: List[Any], arr: List[Any]=[5,4,2,7,8]) -> List | None:
    """
    Gets the subsequences of given array
    Args:
        arr (list, optional): array to get the subsequences, Defaults to [5,4,2,7,8].

    Returns:
        List: list of sub sequences
    """
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
    print(get_all_subsequences(0,[],[], arr=[5,4,2,1,3]))
    
