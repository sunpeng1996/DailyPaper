---
title: 'Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable
  Explanations'
title_zh: 面向AI生成可探索解释的交互性自动化评估框架
authors:
- Xiaozao Wang
- Zhewei Wang
- Hongyi Wen
affiliations:
- New York University Shanghai
arxiv_id: '2606.31012'
url: https://arxiv.org/abs/2606.31012
pdf_url: https://arxiv.org/pdf/2606.31012
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: LLM生成内容交互质量自动化评估
tags:
- Automated Evaluation
- Finite State Machine
- LLM Generation
- Interactive Content
- Knowledge Representation
one_liner: 提出基于有限状态机的EE-Eval框架，实现AI生成交互式学习材料交互质量的自动化评估，与人类判断一致性远超基线
practical_value: '- 评估电商导购Agent、会话推荐Agent的交互质量时，可借鉴FSM建模用户可控状态+转移的思路，替代仅看单轮回复质量的表层评估逻辑

  - 对比生成内容与预期目标的一致性时，可复用「图结构指标+节点语义嵌入相似度」的组合方案，同时覆盖结构与语义匹配度

  - 做商品互动导购文案、个性化互动教程等生成式内容的自动化评测时，可参考将隐性交互逻辑显性化的思路，降低人工标注成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM可快速生成交互式学习材料，但现有评估基准仅关注代码可执行性、视觉保真度等表层指标，无法评估用户可控状态转移、上下文敏感响应等核心交互质量，而后者直接影响用户对内容的理解效果。
### 方法关键点
提出EE-Eval自动化评估框架，将交互性形式化为用户可控状态与转移构成的有限空间，用Finite State Machine (FSM)表示；从生成的可探索解释中提取FSM，将隐性交互逻辑转化为可机器解析的显式图结构；通过对比生成FSM与编码了意图的理想FSM的图结构指标，以及状态、动作、反馈的embedding相似度，综合衡量结构与语义相似性。
### 关键结果
在127个概念、6个AI模型生成的数千份可探索解释上测试，EE-Eval区分交互质量的能力远高于表层指标，与人类对交互性、内容有效性的判断一致性大幅优于现有基线。
