---
title: When Does Tool Use Increase the Expressive Power of Finite-Precision Recurrent
  Models?
title_zh: 有限精度循环模型的工具调用表达能力增益边界研究
authors:
- Nikola Zubić
- Qian Li
- Yuyi Wang
- Davide Scaramuzza
affiliations:
- University of Zurich
- Shenzhen Research Institute of Big Data
- Tengen Intelligence Institute
- CRRC Zhuzhou Institute
arxiv_id: '2607.06155'
url: https://arxiv.org/abs/2607.06155
pdf_url: https://arxiv.org/pdf/2607.06155
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: Agent工具调用表达能力理论边界
tags:
- Tool Use
- Expressivity
- Recurrent Model
- SSM
- Turing Completeness
- Finite Precision
one_liner: 严格证明有限精度循环模型的工具调用表达能力增益二分边界
practical_value: '- 做Agent工具选型时，固定规则类有限状态工具（如计算器、固定接口查询）可直接内化进模型逻辑，无需额外调用开销；仅对长序列推理、多步规划等场景外挂可读写的无限状态存储（如scratchpad、向量数据库），平衡能力与延迟

  - 用Mamba等selective SSM做电商导购Agent、用户长兴趣建模的控制器时，可外挂用户行为序列缓存、推理草稿存储，仅需极少内部参数即可实现接近图灵完备的长序列处理能力，大幅降低推理成本

  - 若需在模型内部实现任意状态转移逻辑，不要尝试对数级维度压缩，理论下界为状态数减1的循环维度，避免无意义的架构优化投入'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM驱动的Agent系统普遍通过工具调用拓展能力，但工具选型、架构设计缺乏严谨的理论指导：有限精度循环模型（包括SSM、RNN等所有有限精度序列模型）本身等价于有限状态机，工具调用到底能带来多大的表达能力提升、需要付出多少内部内存成本，一直没有明确的量化结论。
### 方法关键点
1. 将任意有限精度循环模型抽象为有限状态控制器，通过有限的命令/观测接口与外部工具交互，覆盖所有固定精度的SSM、RNN类架构
2. 对外部工具做二分分类：有限状态有界接口工具、仅支持基础读写/移动操作的无限状态磁带工具
3. 严格推导两类工具下控制器的表达能力边界与内存开销，同时证明selective SSM可精确实现所需的有限状态控制器逻辑
### 关键结果
1. 有限状态工具几乎无表达能力增益：仅需增加`log2|M|+O(1)`位内部内存即可将工具完全内化，增强后系统仍为有限状态
2. 单个最小无限状态工具即可让系统达到图灵完备，仅需`O(log|Q|+log|Γ|)`位内部内存；对`EQ_n`相等性判断问题，无工具时需要`2^n`个内部状态，外挂磁带工具后仅需常数规模控制器
3. 无外部内存时，实现任意B状态转移映射至少需要B-1维的循环维度
### 核心结论
工具对有限精度循环模型的表达能力增益完全由工具的状态空间与接口决定，有限状态工具可被完全内化，仅无限状态外部存储能带来本质性的能力跃升
