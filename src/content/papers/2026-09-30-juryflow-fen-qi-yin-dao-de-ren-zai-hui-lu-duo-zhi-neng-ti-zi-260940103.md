---
title: 'JuryFlow: Disagreement-Guided Human-in-the-Loop Multi-Agent Evaluation'
title_zh: JuryFlow：分歧引导的人在回路多智能体自动评估框架
authors:
- Mufeng Yang
- Junwei Yu
- Yepeng Ding
affiliations:
- University of Tsukuba
- The University of Tokyo
- Hiroshima University
arxiv_id: '2609.40103'
url: https://arxiv.org/abs/2609.40103
pdf_url: https://arxiv.org/pdf/2609.40103
published: '2026-09-30'
collected: '2026-10-01'
category: MultiAgent
direction: 多智能体 · 自动评估优化
tags:
- Multi-Agent
- LLM-as-a-Judge
- Human-in-the-Loop
- Uncertainty Quantification
- Evaluation Framework
one_liner: 通过分歧图定位高不确定性评估点，定向修正后迭代优化评估规则，大幅提升自动评估准确率
practical_value: '- 电商内容审核、生成式推荐文案评估场景可复用claim粒度分歧检测逻辑，基于熵值排序优先处理高争议点，减少人工审核量

  - 多智能体决策（如商品推荐策略投票、广告素材评分）场景可复用修正传播+动态rubric机制，单次修正自动覆盖同类case，持续降低决策错误率

  - 可复用多模型异构panel设计，相比同模型多prompt的ensemble，在易争议场景准确率提升更显著，优先选用不同厂商LLM组建评估panel'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自动评估单法官存在位置、冗长偏好等偏差，多法官panel常用多数投票直接丢弃冲突信息，全量人工审核成本过高，亟需在最小人工干预下解决评估分歧、持续提升评估准确率。

### 方法关键点
- 多智能体结构化判决：异构法官panel将候选响应拆分为原子claim，给出每个claim的判决、维度标签，无提前聚合
- 分歧图构建：节点为claim，权重为判决熵值（越高争议越大），边为标签Jaccard+embedding余弦相似度混合的结构相似度
- 最小干预选择：仅需人工/自动按熵值选1个核心争议claim，无需打标
- 传播式重评估：核心claim重判后，按边权重阈值传播到同实例相似claim，同时检索历史相似claim批量重判
- 增量rubric更新：将修正抽象为可复用规则，所有法官后续评估直接继承

### 关键实验
在MT-Bench、LLMBar两个基准上对比单最优法官、多数投票panel基线：JuryFlow在MT-Bench准确率比单法官高5.3pp、比多数投票高2.9pp；在易分歧的LLMBar数据集准确率比单法官高10.5pp、比多数投票高6.6pp；消融实验显示核心重判贡献3pp，传播贡献2.8pp，rubric更新贡献1.2pp。

**最值得记住的一句话：** 多智能体分歧不是噪声，而是精准定位高不确定性决策点的核心信号，定向修正+规则沉淀的效率远高于全量重评估或简单投票聚合。
