class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}

        for path in paths:
            components = path.split()
            directory = components[0]
            for i in range(1, len(components)):
                file_name, content = components[i].split('(')
                content = content[:-1]
                file_path = directory + '/' + file_name
                if content in content_dict:
                    content_dict[content].append(file_path)
                else:
                    content_dict[content] = [file_path]
        
        duplicates = [files for files in content_dict.values() if len(files) > 1]
        return duplicates