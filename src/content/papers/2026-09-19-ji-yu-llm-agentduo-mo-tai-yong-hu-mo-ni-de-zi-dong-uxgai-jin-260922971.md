---
title: Automatic multimodal UX improvement recommendations from LLM agent user simulations
title_zh: 基于LLM Agent多模态用户模拟的自动UX改进推荐框架
authors:
- Anu Chowdhury
- Bin Wu
- Hossein A. Rahmani
- Emine Yilmaz
affiliations:
- University College London
arxiv_id: '2609.22971'
url: https://arxiv.org/abs/2609.22971
pdf_url: https://arxiv.org/pdf/2609.22971
published: '2026-09-19'
collected: '2026-09-22'
category: Agent
direction: Agent 用户模拟 · UX优化
tags:
- LLM Agent
- Multimodal
- User Simulation
- UX Optimization
- Recommendation
one_liner: 提出多模态用户模拟框架AMUSER，自动生成高优先级可落地UX改进建议，成本较纯文本方案低89%
practical_value: '- 电商/网站UX优化可直接复用AMUSER框架，用多模态Agent模拟不同年龄段、消费能力、熟悉度的用户 personas，自动发现路径摩擦点，成本仅为真人测试的10%左右

  - 做多模态用户模拟时，仅需在模拟阶段输入视觉信息，推荐生成阶段可移除截图仅保留动作、思考、情绪文本日志，既保留多模态的信息增益，又避免多图输入带来的性能下降，同时进一步降低推理成本

  - 用LLM-as-a-Judge评估优化建议时，添加“非常严格判断，仅当3名标注员均同意时才判定为有效”的校准prompt，可降低43%的假阳性，大幅提升评估结果的可信度

  - 电商产品/页面优化可复用其建议优先级排序逻辑，高优先级建议的有用率达78%，91%的建议均可在2周的产品迭代周期内落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
线上网站UX真人测试成本高、主观性强、难规模化，现有纯文本LLM用户模拟方案缺少视觉输入，无法捕捉布局、视觉注意力类UX问题，且需人工分析日志提取优化建议，落地效率极低。

### 方法关键点
- 构建AMUSER多模态框架，分三个模块：persona分析模块预生成对应人群的行为特征与偏好，输入模拟Agent；模拟模块调用多模态LLM完成指定网页任务，每步输出动作、用户思考、情绪标签，留存全量交互轨迹与截图；推荐模块基于轨迹自动生成UI/UX/产品三类改进建议，按高中低优先级排序。
- 设计融合专家标注与LLM-as-a-Judge的评估协议，针对LLM Judge的正向偏见添加校准prompt，将其与人类标注的一致性提升至人类标注水平的67%-82%。

### 关键结果
- 实验覆盖10个英国头部银行、时尚电商网站，共145次模拟，生成1200条建议，覆盖6类常见任务、5类用户 personas。
- 对比纯文本模拟方案UXAgent、静态HTML分析 baseline：AMUSER的NDCG@3达0.758，分别较后两者高111%、177%；单轮模拟成本仅0.48美元，较UXAgent低89%。
- 消融实验验证多模态不对称效应：模拟阶段输入视觉信息可大幅提升建议质量，推荐阶段输入截图反而使NDCG@3下降2个百分点。

### 核心结论
多模态对用户模拟的增益主要来自上游模拟阶段的信息留存，下游分析阶段反而可能因多图输入的性能损耗降低产出质量
