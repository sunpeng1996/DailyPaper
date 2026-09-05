---
title: Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation
  in Code LLMs
title_zh: 面向代码大模型的两阶段强化学习鲁棒对抗测试用例生成
authors:
- Jiacheng Xu
- Wentao Zhang
- Zhiyi Lyu
- Fuxiang Zhang
- Chaojie Wang
- Yang Liu
- Bo An
affiliations:
- Nanyang Technological University, Singapore
- Skywork AI
arxiv_id: '2609.03955'
url: https://arxiv.org/abs/2609.03955
pdf_url: https://arxiv.org/pdf/2609.03955
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: 代码大模型 · 强化学习测试用例生成
tags:
- Reinforcement Learning
- Test Case Generation
- Code LLM
- Adversarial Training
- Two-stage Training
one_liner: 提出两阶段RL框架TCS，自动生成兼具合理性与判别性的代码LLM测试用例，提升代码生成效果
practical_value: '- 两阶段滚动策略对齐buffer的RL训练范式可迁移到电商推荐的难负例生成场景：第一阶段对齐业务规则生成合法候选，第二阶段聚焦当前模型bad
  case生成对抗样本，优化召回/排序模型鲁棒性

  - 基于当前模型失败模式做针对性对抗生成的思路，可用于LLM生成电商文案/商品标题的质量校验环节，自动挖掘生成结果的缺陷，筛选优质输出

  - 生成式测试+候选排序的链路可复用在Agent执行结果的自动校验流程中，无需人工标注即可实现多候选输出的自动择优'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
代码LLM的强化学习训练依赖测试用例提供可执行反馈，但高质量测试用例极度稀缺，需同时满足合法合理、可区分正确/错误代码两个核心要求，人工标注成本极高。
### 方法关键点
提出两阶段RL框架TCS，两个阶段均基于滚动的策略对齐buffer训练测试生成器：
1. 第一阶段生成与参考解匹配的合法测试用例，保证生成质量基线
2. 第二阶段限制buffer仅保留当前代码求解器的失败case，针对性学习生成对抗性反例测试用例，提升判别性
### 关键结果
在TACO、LiveCodeBench基准上，TCS生成的测试用例可同时提升代码生成pass@1指标与推理阶段多候选答案筛选效果，且生成器可跨模型复用做输出质量校验。
