from collections import Counter


filename = "./input/12.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [[i for i in line.rstrip().split("-")] for line in lines]

conns = {}

for conn in lines:
    if conn[0] not in conns and conn[0] != "end":
        conns[conn[0]] = []
    if conn[1] not in conns and conn[1] != "end":
        conns[conn[1]] = []
    if conn[0] != "end" and conn[1] != "start":
        conns[conn[0]].append(conn[1])
    if conn[1] != "end" and conn[0] != "start":
        conns[conn[1]].append(conn[0])


def find_paths(part=1):
    paths = []
    allowed_lower = []
    complete_paths = []
    new_path = ["start"]
    paths.append(new_path.copy())
    allowed_lower.append(True)
    while True:
        new_paths = 0
        for i, path in enumerate(paths):
            if path[-1] != "end":
                for conn in conns[path[-1]]:
                    if part == 1:
                        if conn == conn.lower() and conn in path:
                            continue
                    if part == 2:
                        if (
                            conn == conn.lower()
                            and conn not in ["start", "end"]
                            and conn in path
                            and not allowed_lower[i]
                        ):
                            continue
                    new_path = path.copy()
                    new_path.append(conn)
                    if new_path not in paths and conn != "end":
                        lower_count = Counter(
                            [
                                c
                                for c in new_path
                                if c == c.lower() and c not in ["start", "end"]
                            ]
                        )
                        allowed = (
                            len(lower_count) == 0 or max(lower_count.values()) == 1
                        )
                        paths.append(new_path)
                        allowed_lower.append(allowed)
                        new_paths += 1
                    if conn == "end" and new_path not in complete_paths:
                        complete_paths.append(new_path)
        if new_paths == 0:
            return complete_paths


paths = find_paths(1)
print("Part 1:", len(paths))

paths = find_paths(2)
print("Part 2:", len(paths))
paths.sort()
