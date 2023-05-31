# analysis-of-False-Positive-case-of-CRC
CRC校验只能保证丢掉的数据段一定出现了比特差错，不能保证未丢掉的数据段一定没有比特差错，即CRC校验没有错检但存在漏检。本项目将首先在原理上理论分析何时会发生漏检并给出充要条件，然后通过SageMath语言编程验证结果。
1. 编程语言：SageMath。
2. .py和.ipynb的内容一致。
3. 具体代码逻辑与实现原理请详见pdf文档！
