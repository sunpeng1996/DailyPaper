---
title: Grounding User Preferences in Shared Multimodal Concepts for Recommendation
title_zh: 基于共享多模态概念落地用户偏好的推荐框架
authors:
- Ao Xu
- Jinhui Huang
- Wenqiang Tang
- Tiehua Mei
- Hongru Hou
- Hengrui Chen
- Jiaqing Liang
- Deqing Yang
affiliations:
- 复旦大学
arxiv_id: '2611.34436'
url: https://arxiv.org/abs/2611.34436
pdf_url: https://arxiv.org/pdf/2611.34436
published: '2026-11-25'
collected: '2026-11-26'
category: RecSys
direction: 多模态推荐 · 知识图谱用户偏好建模
tags:
- Multimodal Recommendation
- Knowledge Graph
- User Preference Modeling
- Cold Start
- Graph Neural Network
one_liner: 提出MKGE多模态知识图谱推荐框架，通过共享规范多模态概念建模用户偏好，提升全场景尤其冷启动推荐效果
practical_value: '- 可复用「Discover-Standardize-Constrain」三步法构建电商领域多模态概念KG：用MLLM抽取商品图文的风格、属性等语义标签，聚类合并同义表述生成规范词汇表，解决跨商品语义对齐问题，降低语义匹配噪声

  - 冷启动/低活跃度用户推荐可直接采用「CF路径+概念语义路径」的双路融合架构：在交互稀疏的电商美妆场景下，语义路径的贡献超过传统CF路径，NDCG@10相对纯CF方案提升10.9%

  - 工程落地可分离离线和在线流程：离线用MLLM完成概念抽取、用户偏好grounding，在线仅跑轻量GNN推理，单用户推理延迟仅51.3ms，GPU显存占用8.2GB，远低于MLLM直接推理的开销，适配高并发推荐场景

  - 用户偏好建模可拆分短/长期双时间粒度的概念标签：长期偏好保留跨2~3个月的高频稳定概念，短期偏好覆盖近1个月的兴趣变化，比单纯用频次/IDF筛选标签的方案NDCG@10提升3%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态推荐对物品的图文语义表征精度持续提升，但用户偏好仍以整item交互粒度建模，用户真正感兴趣的重复出现的语义因素被item其他属性纠缠，没有跨item可共享的持久身份标识，导致跨item的偏好证据无法有效积累，低交互冷启动用户的偏好建模准确率极低。

### 方法关键点
- 分三步构建领域规范多模态概念库：Discover阶段用MLLM从采样商品的图文对抽取关系-概念对，Standardize阶段聚类合并同义概念生成覆盖度≥90%的规范词汇表，Constrain阶段用固定词汇表给全量商品打标签，生成item-concept三元组
- 时序偏好grounding：按21天为时间桶抽取用户交互item关联的概念，分别生成短期（单时间桶最多10个概念）、长期（每4个时间桶更新，保留跨桶高频稳定概念）的user-concept关联
- 双路径GNN推荐：CF编码器仅在user-item交互图传播学习协同信号，KG编码器在包含user/item/concept的异构图传播学习语义匹配信号，两路表征融合后排序，辅以跨视图对比、item-concept对齐、概念门控正则三类辅助损失优化

### 关键结果
在ML-1M、Amazon Video Games、Amazon Beauty三个数据集上对比16个主流基线（含LightGCN、MMGCN、MLLMRec等），全指标最优：ML-1M Recall@10相对最优基线提升2.82%，美妆稀疏场景下NDCG@10/Recall@10分别提升2.68%/4.87%；低活跃度用户下相对无概念KG的方案NDCG提升24.74%，在线推理延迟仅51.3ms/user。

**最值得记住的结论**：将用户偏好落地到跨item共享的规范多模态概念上，是用多模态大模型能力低成本提升稀疏场景推荐效果的高性价比路径
