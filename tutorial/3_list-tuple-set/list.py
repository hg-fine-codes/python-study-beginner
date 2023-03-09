courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses)
# print(len(courses))
# print(type(courses))

# print(courses[0])
# print(courses[-1])

# print(courses[4])

# print(courses[0:3])
# print(courses[:3])
# print(courses[2:])

# courses.append('Art')

# courses.insert(0, 'Art')

# courses_2 = ['Art', 'Education']

# courses.insert(0, courses_2)
# courses.append(courses_2)

# courses.extend(courses_2)

# courses.remove('Math')

# popped = courses.pop()
# print(popped)

# courses.reverse()


nums = [1, 53, 5, 244, 72]

# courses.sort()
# nums.sort()

# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)

# print(sorted_courses)
# print(courses)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index('CompSci'))
# print(courses.index('compSci'))

# print('Art' in courses)
# print('Math' in courses)

# for item in enumerate(courses):
#     print(item)

# for index, course in enumerate(courses):
#     print(index, course)

# for index, course in enumerate(courses, start=1):
#     print(index, course)

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)
