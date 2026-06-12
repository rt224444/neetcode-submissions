from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the full word at terminal nodes

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]

            # Found a word
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            # Restore
            board[r][c] = ch

            # Optional trie pruning
            if not nxt.children:
                node.children.pop(ch)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return result