# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 22:29:59 2026

@author: i5
"""

#from trie import Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for put: key = {key} must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def get(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for get: key = {key} must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def delete(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for delete: key = {key} must be a non-empty string")

        def _delete(node, key, depth):
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def is_empty(self):
        return self.size == 0

    def longest_prefix_of(self, s):
        if not isinstance(s, str) or not s:
            raise TypeError(f"Illegal argument for longestPrefixOf: s = {s} must be a non-empty string")

        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    def keys_with_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for keysWithPrefix: prefix = {prefix} must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._collect(current, list(prefix), result)
        return result

    def _collect(self, node, path, result):
        if node.value is not None:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self):
        result = []
        self._collect(self.root, [], result)
        return result


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        # validation
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a string"
            )

        if pattern == "":
            # пустий суфікс — формально підходять усі слова
            return self.size

        count = 0

        def dfs(node, path):
            nonlocal count

            # якщо це кінець слова — перевіряємо суфікс
            if node.value is not None:
                word = "".join(path)
                if word.endswith(pattern):
                    count += 1

            for ch, nxt in node.children.items():
                path.append(ch)
                dfs(nxt, path)
                path.pop()

        dfs(self.root, [])
        return count

    def has_prefix(self, prefix) -> bool:
        # validation
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for has_prefix: prefix = {prefix} must be a string"
            )

        if prefix == "":
            # пустий префікс — якщо trie не порожній
            return not self.is_empty()

        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        # якщо ми дійшли сюди — такий шлях існує,
        # отже є хоча б одне слово з цим префіксом
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True
