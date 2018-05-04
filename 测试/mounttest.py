#!/usr/bin/env python3
import unittest
from mounttab import parse_mounts


class TestMount(unittest.TestCase):
    def test_parsemount(self):
        result = parse_mounts()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

    def test_rootext4(self):
        """
        测试找出根文件系统
        """
        result = parse_mounts()
        for line in result:
            if line[1] == '/' and line[2] != 'rootfs':
                self.assertEqual(line[2], 'ext4')

if __name__ == '__main__':
    unittest.main()
