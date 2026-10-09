---
title: Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention
  Residuals
title_zh: 基于循环原生注意力残差的万级测试时迭代扩展方法
authors:
- Pengxiang Li
- Dilxat Muhtar
- Di He
- Guinan Su
- Lu Yin
- Shiwei Liu
affiliations:
- The Hong Kong Polytechnic University
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Peng Cheng Laboratory
- Max Planck Institute for Intelligent Systems
- Shenzhen University of Advanced Technology
arxiv_id: '2610.11570'
url: https://arxiv.org/abs/2610.11570
pdf_url: https://arxiv.org/pdf/2610.11570
published: '2026-10-07'
collected: '2026-10-09'
category: Reasoning
direction: 循环Transformer · 推理深度扩展
tags:
- Loop-Transformer
- Residual-Connection
- Test-Time-Reasoning
- InfiLoop
- Reasoning-Efficiency
one_liner: 提出InfiLoop循环原生残差连接，解决循环Transformer迭代深度增长导致的性能退化，支持万级测试时推理迭代
practical_value: '- 业务中使用循环Transformer做Agent多轮思考、复杂推荐路径生成、迭代精排时，可替换原有carry-last状态传递为InfiLoop，仅新增极少量参数即可避免多轮迭代后的状态漂移与性能下降

  - InfiLoop的常数内存流式更新逻辑可复用在长序列推理、多轮状态聚合场景，如用户多轮交互兴趣累积、RAG多轮检索结果聚合，内存占用不随轮次增长

  - 内容加权+时间衰减的自适应更新机制可迁移到电商用户行为序列建模，自动给高相关历史行为加权、低质量行为降权，兼顾效果与计算效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped Transformer通过重复调用共享Transformer块实现推理深度扩展，无需新增参数，但现有carry-last规则（直接将上一轮输出作为下一轮输入）存在严重缺陷：迭代次数增加时，噪声更新会覆盖正确的中间推理结果，甚至抵消已完成的正确解，导致推理精度随深度上升反而下降，限制了测试时多轮迭代的性能收益。
### 方法关键点
- 提出InfiLoop循环原生残差连接替换carry-last规则：用共享伪query对每轮输出做内容打分，结合可学习的指数时间衰减，归一化加权聚合所有历史轮次状态作为下一轮输入
- 设计精确流式更新公式，仅需为每个token维护1个加权状态向量和1个归一化标量，聚合内存不随循环次数增长，复杂度O(Td)远低于全历史注意力残差的O(T²d)
- 等价于自适应残差更新，自动判断每轮新输出质量，高置信度输出获高权重，低质量更新被抑制，避免状态漂移
### 关键结果
7M参数的InfiLoop在四个推理基准上远超同参数baseline：Sudoku-Extreme精确准确率达97.9%（超FPRM 3.7个百分点），ARC-AGI-2 pass@2达13.6%（是同参数TRM的1.7倍）；测试时迭代到20000步以上精度仍持续上升，同等精度下所需层数仅为FPRM的一半。
> 最值得记住的结论：循环推理的性能瓶颈不在于深度本身，而在于跨轮次的状态传递机制，选择性聚合历史状态比盲目增加迭代次数更能提升推理效果
