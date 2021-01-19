my_dict = {'Peter': 21, 'George': 18, 'John': 45}

sorted_dict = dict(sorted(my_dict.items(), key= lambda x: x[0], reverse = True))

print(sorted_dict)