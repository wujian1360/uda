# 数据类型和运算符

- 数据类型：整型、浮点型、布尔型、字符串、列表、元组、集合、字典
- 运算符：算术、赋值、比较、逻辑、成员、恒等运算符
- 内置函数、复合数据结构、类型转换
- 空格和样式指南



### 算术运算符
- 算术运算：+ - * / (加减乘除) %(取模) **(取幂) //(地板除)
- 赋值运算符：= += -+ *= 
- 代码规范：空格等
- 整形、浮点型，除零错误
- 布尔、比较、逻辑运算符: 
  - 比较：<  >  ==  != 
  - 逻辑：and or not

### 字符串
- 转义字符：'Simon\'s skateboard is in the garage.'
- 索引：first_word[0]

### 类型转换
- type() 检查类型函数
- int()、str()、float()、...
- len('this')、print('h')
- 方法：string方法、list方法 可以查询文档。
- string.find('ah')、string.count('a')
、string.islower()、string.isalpha()、string.isspace()

### 列表和成员运算符
- 可变性：主要指对象是否可以更改。
    - 列表是可变对象，可以通过索引更改
    - 字符串是不可变对象，一旦改变就是重新赋值
    - 字典是可变的
    - 集合是不可变的
    - 元组是不可变的
- 有序性：对象是否有顺序
    - 字符串是有序的
    - 列表也是有序的
    - 集合是无序的
    - 字典是无序的
    - 元组是有序的
### 列表
  - 可变有序元素数据类型
  - 列表切片：eclipse_dates[-3 : ]//取末尾三个元素
  - 拼接函数：将字符串列表作为参数，用一个连接符连接
    new_str = "\n".join(["fore", "aft", "starboard", "port"])
  - 排序函数：sorted(["Carol", "Albert", "Ben", "Donna"]),排序一个字符串列表
  - 列表append 方法: letters.append('z')
### 元组
  - 不可变有序元素数据类型
  - 在定义元组时，小括号是可选的
  - 元组不可变，你无法向元组中添加项目或从中删除项目，或者直接对元组排序。通常表示坐标点、经纬度
  - location = (13.4125, 103.866667)
  - 元组解包:dimensions = 52, 40, 100
  - 元组赋值:length, width, height = dimensions
### 集合
  - 包含唯一元素的可变无序集合数据类型
  - 集合的一个用途是快速删除列表中的重复项。
  - 集合轻松地执行 union、intersection 和 difference 等方法，并且与其他容器相比，速度快了很多

    ```python
        numbers = [1, 2, 6, 3, 1, 1, 6]
        unique_nums = set(numbers)
        {1, 2, 3, 6}
        ```
  - 元组是无序的，他和列表一样支持in、add()、pop()
    - 删除元素就是随机删除一个
    - 没有最后一个元素
### 字典
  - 可变、无序数据类型，其中存储的是唯一键到值的映射
    
    ```python
        elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
        print("carbon" in elements)
        print(elements.get("dilithium"))
        ```
### 恒等运算符：is 和 is not
  - == 是两边元素的值完全相等
  - is 是恒等，也是就指向同一个对象

### 复合数据结构：
  - 我们可以在其他容器中包含容器，以创建复合数据结构。
   ```python
    # 向嵌套字典中添加值
    elements["hydrogen"]["is_noble_gas"] = False
    elements["helium"]["is_noble_gas"] = True
   ```

