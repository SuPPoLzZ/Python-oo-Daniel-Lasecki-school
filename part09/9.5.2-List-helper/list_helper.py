class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None

        
        count_dict = {}
        for item in my_list:
            count_dict[item] = count_dict.get(item, 0) + 1

        
        most_common_item = max(count_dict, key=count_dict.get)
        return most_common_item

    @classmethod
    def doubles(cls, my_list: list):
        if not my_list:
            return 0

        
        count_dict = {}
        for item in my_list:
            count_dict[item] = count_dict.get(item, 0) + 1

        
        count_doubles = sum(1 for count in count_dict.values() if count >= 2)
        return count_doubles


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
