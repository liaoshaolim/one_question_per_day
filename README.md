# one_question_per_day
# 每日一算法
## time line：
* 2020年09月09日 

   * 最长公共前缀
* 2020年09月11日

    * 基础: 快排 
    * 给定两个数组，编写一个函数来计算它们的交集 
    * 有序数组交集
* 2020年09月16日

    * 二分查找 
    * 二分查找升级版之左右侧边界
* 2020年09月21日

    * 第一个只出现一次的字符 
    * 合并两个有序数组 
    * 有效的括号 
    * 整数反转 
    * 字符串反转 
    * 只出现一次的数字
* 2020年09月22日

    * 斐波那契数列三种解法 
    * 青蛙跳台阶问题
* 2020年09月23日

    * 零钱兑换TODO
    * 有效的字母异位词
* 2020年09月24日

    * 节点、链表基础知识回顾 
    * 单向链表翻转 + 单向链表中是否有环
* 2020年09月29日

    * 是否是回文数
    * 两数之和
* 2020年10月10日

    * 45 度遍历二维数组    

* 2020年10月19日

    * 滑动窗口最大值 
    * 罗马数字转整数 

* 2020年11月05日

    * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

* 2020年11月09日

    * 相同的二叉树

*** 

## 知识点记录：

### 双指针
* 快慢指针
* 左右指针
* 滑动窗口


### 位运算符概念及使用场景
* & ：按位与 (都为 1 则为 1，否则为 0)

    * 迅速清零（eg:a & 0)
    * 判断奇偶（eg：a & 1 == 1 为奇数，== 0 为偶数)
    * 检查状态

* ｜ ：按位或（有一个为 1 就为 1，否则为 0）
   *  a | 0XFF，值为 255，因为 0XFF 值为 11111111

* ^ : 按位异或（不同为 1，相同为 0）
    * 任何数和 0 异或，结果仍为这个数
    * 相同的两个数异或为 0
    * 和同一个数连续异或两次，结果仍为这个数
  
    ```
    // eg:
    // 交换两个整数的位置
    int a = 10;
    int b = 20;
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    ```
* ~: 按位取反（位运算符中唯一一个单目运算符）每个位置都取反
* << :左移运算 (将 2 进制值向左移动若干位)
    * eg:当数字要与 2 或 2 的倍数相乘时用，可提高效率
* \>>:右移运算（将 2 进制值向右移动若干位）
