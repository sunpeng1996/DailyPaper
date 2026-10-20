---
title: 'When Semantics Fall Short: Persona-Guided Cross-Domain Sequential Recommendation
  with Large Language Models'
title_zh: 语义失效下基于Persona引导的大语言模型跨域序列推荐
authors:
- Jundong Chen
- Honglei Zhang
- Shuai An
- Enneng Yang
- Han Yu
affiliations:
- 北京交通大学
- 中山大学
- 南洋理工大学
- 教育部交通大数据与人工智能重点实验室
arxiv_id: '2610.25221'
url: https://arxiv.org/abs/2610.25221
pdf_url: https://arxiv.org/pdf/2610.25221
published: '2026-10-18'
collected: '2026-10-20'
category: RecSys
direction: 跨域序列推荐 · LLM引导用户画像
tags:
- Cross-Domain Recommendation
- Sequential Recommendation
- Persona
- LLM4Rec
- User Modeling
one_liner: 提出Persona引导的跨域序列推荐框架PerCDR，跳出语义对齐范式，较SOTA最高提升15.4% NDCG@10
practical_value: '- 跨域推荐场景可直接复用「全局Persona引导+局部语义关联」范式，避免全局语义对齐的领域隔离问题，尤其适配多品类电商跨域召回/排序场景

  - 可直接复用论文给出的Persona生成prompt，仅输出不涉及具体物品/品牌/领域的用户行为动机描述，大幅降低Persona的领域特异性

  - 工程实现上Persona和语义嵌入可离线生成，训练阶段无需调用LLM，仅新增两个轻量化辅助损失，推理延迟几乎无上涨，适合业务快速上线

  - 多目标优化时可参考η/λ取0.5左右的经验值，局部语义邻居K取10即可平衡性能和计算开销'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强跨域序列推荐（CDSR）依赖全局item语义对齐，存在两个固有缺陷：1.语义领域隔离：不同域的item描述维度差异大（如厨房品侧重功能、食品侧重品类），全局对齐难度高；2.语义-行为不一致：同域内语义相似性和行为一致性强，但跨域用户常跳转语义无关的item（如买勺子后买花生油），全局语义对齐反而破坏真实跨域行为规律，亟需跳出语义对齐范式的新方案。

### 方法关键点
- LLM驱动表征构建：离线用LLM embedding生成item冻结语义表征，用轻量LLM推理从用户跨域行为序列生成无领域依赖的Persona锚点，再经embedding得到Persona表征
- 联合行为建模：学习可训练的跨域行为嵌入，用两个辅助损失正则：①局部语义关联（LSA）：仅在同域内约束item的行为嵌入和语义嵌入的Top10邻居相似度一致，避免全局语义对齐的隔离问题；②全局Persona引导（GPG）：用Persona感知注意力给用户不同时序行为加权，通过对比学习让跨域行为表征向同一Persona锚点对齐，挖掘跨域可迁移行为规律
- 域偏好适配：用独立编码器学习单域语义偏好，通过门控网络自适应融合跨域联合预测得分和单域偏好得分，修正推荐结果

### 关键实验
在亚马逊3组公开跨域数据集（CD-Movie、Food-Kitchen、Cloth-Sport）上对比11个SOTA基线（含SASRec、C2DSR、LLM4CDR、SemaCDR等），PerCDR在所有数据集上显著优于最优基线：NDCG@10最高提升15.40%（Movie域）、最低提升4.30%（Kitchen域），H@10最高提升8.77%（Movie域），所有提升均通过0.05显著性检验。

最值得记住的一句话：跨域推荐的核心是迁移用户行为动机而非对齐item语义，语义信息更适合做局部同域行为增强而非全局跨域桥梁。
