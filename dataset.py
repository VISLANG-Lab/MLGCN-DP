from __future__ import print_function
import numpy as np

"""
Basic operations on dependency trees.
"""


class Tree(object):
    """
    Reused tree object from stanfordnlp/treelstm.
    """
    def __init__(self):
        self.parent = None
        self.num_children = 0
        self.children = list()

    def add_child(self,child):
        child.parent = self
        self.num_children += 1
        self.children.append(child)

    def size(self):
        if getattr(self, '_size'):
            return self._size
        count = 1
        for i in range(self.num_children):
            count += self.children[i].size()
        self._size = count
        return self._size

    def depth(self):
        if getattr(self, '_depth'):
            return self._depth
        count = 0
        if self.num_children>0:
            for i in range(self.num_children):
                child_depth = self.children[i].depth()
                if child_depth>count:
                    count = child_depth
            count += 1
        self._depth = count
        return self._depth

    def __iter__(self):
        yield self
        for c in self.children:
            for x in c:
                yield x

def head_to_tree(head):
    """
    Convert a sequence of head indexes into a tree object.
    """
    head = sorted(head, key=lambda x: x[2])
    head = [w[1] for w in head]
    # print(head, len(head))
    # tokens = tokens[:len(head)]
    # head = head
    root = None
    # print('head:'. head.size())
    # print('tokens:', )

    nodes = [Tree() for _ in head]

    for i in range(len(nodes)):

        h = head[i]
        # print('1111', h)
        nodes[i].idx = i
        nodes[i].dist = -1  # just a filler
        if h == 0:
            root = nodes[i]
        else:
            nodes[h-1].add_child(nodes[i])


    assert root is not None
    return root


def tree_to_adj(sent_len, tree, sent, not_directed=True):
    """
    Convert a tree object to an (numpy) adjacency matrix.
    """
    # ret = np.ones((sent_len, sent_len), dtype=np.float32)
    ret = np.zeros((sent_len, sent_len), dtype=np.float32)
    length = ret.shape[0]

    queue = [tree]
    idx = []
    while len(queue) > 0:
        t, queue = queue[0], queue[1:]

        idx += [t.idx]

        for c in t.children:
            ret[t.idx, c.idx] = 1
        queue += t.children

    # if sent == 'sent2':
    #     for i in range(length):
    #         ret[length-1, i] = 1
    # elif sent == 'sent3':
    #     for i in range(length):
    #         ret[length-2, i] = 1
    #         ret[length-1, i] = 1
    # elif sent == 'sent4':
    #     for i in range(length):
    #         ret[length-3, i] = 1
    #         ret[length-2, i] = 1
    #         ret[length-1, i] = 1
    #
    if not_directed:
        ret = ret + ret.T

    ret = ret + np.eye(sent_len)

    return ret                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         �;�<);й�9;���+Z��2(�s-�1t89��6]5�4ϱ0�J��80;��&4��0��9�6��-]6�3�1&1�/���;�"��5��@�	�S�j�G6�4(�9�ϸ�0M9k0����9(8#8�6�6e�+�/v��3!7�-�1[�Y��1�4�}8|7+�)�!5'�0K8
��3ۨ�����~3�2h65�ػ{:�2M�54F����a�22�/۶\:���}��_���\1(��,�"<�7�3۶��ض'=^��1۸9Y��%B6�5���,�(�<�015a=87K�����2����8u7�+�5��%����0036�7
�!�$��-�c/дi9ܬH����/z�"�!;$<'9(2�s��=��4��8;<��;�,��/1��F-;�1s��,�8�3�6"K�K��3s:��E��:�4P0�9��%��8���Y5\ͷøB�ު�/�/�2B8I��6�87��7�:�ʷL6�,�2,U���ʴ)A�7?4,-6��9k*w��-,\8�7�:<8z5�=o)���o7�������3ꮖ�]�r1g72?3��&�4�*��T��4�))�A�z�L��4�v��,,�+�6b�]�Y�(�y9k��³W���A����;�4�4��!%��4�<�07.4�7��c8`7�2s+����Űh�����+�޺M%�5702j2���0}7�)#��6�2��*��Q6G�7n5T6��+=h5�ڸ﷿����4.��/n+���-s6�_�=�U3����9V5�%36ɸ+����
����#��q�:?8F4η5<�;ӵp�s�M5^+�6S4�.'�´E52��0�����7U�Q��626�-.�0)<��O7���%<�G���04�ḁ���4p1E�ҵ"��9a8�c��(򲀴b=O�q�9	��/��+0>�9;:30�2-��E9�8C�̯/4�5?,�#�,�
�E8A����1�440�E�t�x9��}�E�\����w�Ű�9�2�~��	�H���R��v�;9��<�ɸ+�-����Z�r"?��-]�}��7A2:�3J�5/�.�����|��7g��4[�E�����o4�2�7ӱ<0ĵ>-ï,,­`����9שU��V�%�\���Ϲ@�����^�e�e��9K27*�`�~5��`2q0�����9F�i$��:ʸq5�4���-�.`4Ǩ�Q�4�U��78�����2�5b����#��'�2f�:��;#<\5�8�2c��r8T7A���S