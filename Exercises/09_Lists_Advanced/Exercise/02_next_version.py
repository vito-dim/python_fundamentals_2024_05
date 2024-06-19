def next_version_fun(start_version: list) -> str:
    current_version_as_str = ''.join(start_version)
    current_version_as_int = int(current_version_as_str)
    next_version_as_int = current_version_as_int + 1
    next_version_as_str = str(next_version_as_int)
    next_version_result = '.'.join(next_version_as_str)
    return next_version_result


version = input()
version_as_str_list = version.split('.')
next_version = next_version_fun(version_as_str_list)
print(next_version)

# Short solution
# version = input().split('.')
# version_as_int = int(''.join(version))
# next_version = '.'.join(str(version_as_int + 1))
# print(next_version)
