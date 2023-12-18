class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content_map = {}
        duplicates = []

        for path in paths:
            path_parts = path.split()
            directory = path_parts[0]

            for i in range(1, len(path_parts)):
                file_info = path_parts[i].split('(')
                file_name = file_info[0]
                content = file_info[1][:-1]
                file_path = directory + '/' + file_name

                if content in file_content_map:
                    file_content_map[content].append(file_path)
                else:
                    file_content_map[content] = [file_path]

        for content, file_paths in file_content_map.items():
            if len(file_paths) > 1:
                duplicates.append(file_paths)

        return duplicates