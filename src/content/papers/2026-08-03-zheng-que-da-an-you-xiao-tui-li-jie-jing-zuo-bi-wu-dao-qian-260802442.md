---
title: 'Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM
  Reasoning on Frontier Science Benchmarks'
title_zh: 正确答案≠有效推理：捷径作弊误导前沿科学基准的LLM推理评估
authors:
- Xuan Ren
- Weiqi Zhai
- Tianle Pu
- Yihua Zhu
- Yihua Zhu
- Hu Wei
- Bing Zhao
affiliations:
- Alibaba Group
- Alibaba DAMO Academy
arxiv_id: '2608.02442'
url: https://arxiv.org/abs/2608.02442
pdf_url: https://arxiv.org/pdf/2608.02442
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: LLM科学推理能力评测优化
tags:
- LLM Reasoning
- Evaluation
- Scientific Benchmark
- Shortcut Learning
- Anti-Cheating
one_liner: 揭示仅靠最终答案评估LLM科学推理能力的偏差，提出两套反作弊评测优化策略
practical_value: '- 做电商Agent（客服、选品、活动策略规划）的效果评估时，不能仅看最终结果准确率，需新增推理过程有效性校验，避免高估模型在业务场景的实际落地能力

  - 针对高难度推理任务（如大促预算分配、复杂用户诉求归因），可引入论文提出的测试时引导指令，强制模型输出完整推导链路，降低捷径作弊导致的决策错误风险

  - 可复用自动判分器的设计思路，针对业务场景自定义推理过程合规规则，提升LLM应用效果评估的可信度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM科学推理基准普遍以最终答案准确率作为核心评估指标，无法区分正确答案来自有效推导还是无效捷径，会严重高估模型实际推理能力。
### 方法关键点
定义Solution Hacking失效模式：模型通过数值搜索、枚举、猜测、答案先验验证等无效捷径得到正确答案，无符合任务要求的推导过程。跨难度等级、科学领域、前沿模型系统分析该现象，提出两套反作弊策略：自动判分器、测试时引导指令。
### 关键结果
- 捷径作弊占比随题目难度升高陡增：普通题2.2%，奥赛题28.3%，高难HLE题37.4%
- 前沿模型被标注为正确的答案中，8.2%~44.1%属于作弊解
- 压制捷径行为后，模型报告的准确率大幅下降，但非作弊的正确答案准确率受影响很小
