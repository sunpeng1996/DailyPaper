---
title: Measuring the Gap Between Human and LLM Research Ideas
title_zh: 大语言模型与人类科研创意的差距量化研究
authors:
- Ziyu Chen
- Yilun Zhao
- Arman Cohan
affiliations:
- Yale University
- University of Chicago
arxiv_id: '2607.01233'
url: https://arxiv.org/abs/2607.01233
pdf_url: https://arxiv.org/pdf/2607.01233
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: LLM科研创意生成能力量化评估
tags:
- LLM Ideation
- Evaluation Framework
- Research Taste
- Distribution Alignment
- Creative Generation
one_liner: 构建科研创意评估框架与双轴科研品味分类法，量化LLM与人类的创意分布差异
practical_value: '- 可复用双轴分类思路，量化业务中LLM生成的营销文案/推荐创意与头部运营人员的偏好差异，针对性优化prompt与微调策略

  - 评估创意类LLM产出时，除单样本质量打分外，可新增分布对齐度指标，避免LLM产出同质化，覆盖更多用户偏好区间

  - 可基于该评估框架搭建业务创意质检模块，自动识别LLM过度集中的桥接/合成类创意，补充人工创意拓宽供给池'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM创意生成效果评估仅对单样本做新颖性、可行性、专家偏好打分，未系统性量化LLM产出与人类专家创意的分布差异，无法刻画两者在创意品味层面的差距。
### 方法关键点
1. 构建大规模科研创意评估框架：对每篇高质量人类科研论文，反向追溯启发其核心创意的相关先验工作集；
2. 控制输入相同的先验工作集，分别获取人类论文创意与LLM生成创意；
3. 提出双轴科研品味分类法，从机会模式、研究范式两个维度标注所有创意，量化两类创意的分布差异。
### 关键结果
跨多个主流LLM测试均观测到一致的分布缺口：LLM生成的创意高度集中在桥接类机会、合成类方法维度，人类创意则更均匀覆盖全量缺口挖掘、贡献构建路径；LLM合理创意的覆盖范围显著窄于人类，且存在系统性的分布偏移。
