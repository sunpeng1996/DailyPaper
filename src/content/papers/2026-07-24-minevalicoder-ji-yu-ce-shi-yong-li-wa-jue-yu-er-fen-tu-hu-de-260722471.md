---
title: 'MineValiCoder: Reliable Code Generation with Test Case Quality Mining and
  Bipartite Graph-Based Mutual Validation'
title_zh: MineValiCoder：基于测试用例挖掘与二分图互验证的可靠代码生成
authors:
- Zhen Zhao
- Qihang Yang
- Feifei Dai
- Xiangfang Li
- Bo Li
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- University of Electronic Science and Technology of China
arxiv_id: '2607.22471'
url: https://arxiv.org/abs/2607.22471
pdf_url: https://arxiv.org/pdf/2607.22471
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: LLM代码生成 · 测试驱动开发优化
tags:
- Code Generation
- Test-Driven Development
- Bipartite Graph
- Closed-loop Optimization
- LLM
one_liner: 提出融合测试用例质量过滤与二分图互验证的闭环TDD框架，显著提升LLM代码生成可靠性
practical_value: '- 二分图互验证思路可迁移到RAG检索结果与生成答案的一致性校验，解决多源信号冲突问题

  - 测试用例自验证过滤逻辑可复用在LLM生成内容预检环节，降低错误反馈对优化的干扰

  - 闭环迭代+多候选打分框架可套用到Agent工具调用结果的可靠性评估流程中'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于LLM的测试驱动开发（TDD）代码生成方案要么依赖人工测试用例，要么自动生成的测试用例质量混杂：错误测试会误导代码优化，质量不一致的测试会导致代码选择信号冲突，无法在仅输入自然语言需求的场景下稳定输出可靠代码。
### 方法关键点
提出闭环TDD框架MineValiCoder，包含三个核心模块：
1. TCQM模块通过自验证过滤错误测试用例，提供可靠监督信号
2. 并行TDD迭代优化模块基于有效测试反馈迭代优化代码，生成多样化高质量候选
3. BiCoTeV模块建模代码-测试交互做互验证打分，稳定筛选最优代码
### 关键结果
在4类LLM、主流代码生成基准上显著超越SOTA：HumanEval Pass@1达96.34%，MBPP达87.40%，APPS达64.00%，LiveCodeBench达51.33%，有效缓解LLM随机性问题。
