---
title: 'Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database
  Generalization'
title_zh: 跨Schema泛化：Agent引导的关系专家混合模型实现跨数据库迁移
authors:
- Hiren Madhu
- Sukanta Ganguly
- Kiran Srinivasan
- Smita Krishnaswamy
- Rex Ying
affiliations:
- Yale University
- NetApp
arxiv_id: '2611.18315'
url: https://arxiv.org/abs/2611.18315
pdf_url: https://arxiv.org/pdf/2611.18315
published: '2026-11-13'
collected: '2026-11-16'
category: RecSys
direction: 跨Schema泛化 · Agent+MoE关系建模
tags:
- MoE
- Cross-Schema
- LLM Agent
- Graph Transformer
- Relational Learning
one_liner: 提出Agent引导的关系专家混合图Transformer，以小预训练数据实现跨Schema关系预测SOTA
practical_value: '- 跨业务线/站点的用户建模场景，可复用基于列元数据（列名、类型、时间属性）的MoE路由逻辑，无需依赖特征值即可实现异构特征的参数复用，解决schema不统一问题，无需每个新业务单独训练模型

  - 无标签Agent自动特征工程方案可直接复用：限制Agent仅读取schema、列统计信息，仅允许生成单行变换特征（比率、编码分段等），既避免数据泄露，又可替代人工特征工程，适配新业务冷启动需求

  - 跨场景时间建模可借鉴相对log-age注意力设计，统一不同业务的时间尺度，比如电商30天留存、内容平台7天留存预测可复用同一套时间感知注意力逻辑，降低迁移适配成本

  - 预训练阶段可采用种子行多单元格掩码策略，强制模型学习依赖关联关系数据而非同行特征，提升用户多行为、订单关联等序列数据的建模效果，适用于推荐系统的用户生命周期价值预测等场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
电商、广告等平台的用户行为数据均存储于关系型数据库，不同业务线/平台的schema差异极大，跨业务迁移用户留存、LTV等预测模型需重新做特征工程、训练新模型，成本极高；现有关系基础模型既无法有效迁移跨schema通用结构（时间序列、外键关联），也难以适配目标库专属语义，性能存在明显瓶颈。
### 方法关键点
- 提出MoREGT混合专家图Transformer：同时采用行、单元格两级Token，注意力模块显式融入两行相对log-age差和外键名称嵌入，适配不同时间尺度与关联关系；
- MoE路由完全基于列元数据（列名、类型、行年龄），不依赖特征值，跨库时语义相似列自动路由至相同专家，实现参数复用；
- 搭配无标签LLM Agent：仅读取目标库schema、列统计信息，不接触标签/模型分数，自动生成经校验的单行衍生特征（比率、编码分组等），从根源避免时间泄露。
### 关键实验
在21个RelBench任务（覆盖电商、论坛等场景的分类/回归任务）上测试，对比基线包括同预训练设置的Relational Transformer（RT）、预训练数据规模为其400倍的RT-J、KumoRFM-2等SOTA模型：
- MoREGT backbone较同设置RT提升2.25个平均AUROC、5.83个平均nMAE；
- 叠加Agent衍生特征后，平均AUROC达79.63、平均nMAE达26.98，全面超过预训练数据大400倍的RT-J，登顶RelBench榜单。
### 核心结论
针对异构结构化数据的跨场景迁移，优化架构设计+轻量目标端自适应，可在预训练数据量小两个数量级的情况下，超过大语料预训练的模型效果
