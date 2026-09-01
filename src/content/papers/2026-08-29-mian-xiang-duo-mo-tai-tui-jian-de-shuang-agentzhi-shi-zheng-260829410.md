---
title: Agents as Knowledge Integrator and Utilizer in Multimodal Recommendation
title_zh: 面向多模态推荐的双Agent知识整合与利用框架
authors:
- Jinfeng Xu
- Zheyu Chen
- Shuo Yang
- Jinze Li
- Puzhen Wu
- Zewei Liu
- Zheng Lin
- Jianheng Tang
- Jing Yang
- Wei Wang
affiliations:
- The University of Hong Kong
- Beijing Institute of Technology
- Peking University
- Universiti Malaya
- Macao Polytechnic University
arxiv_id: '2608.29410'
url: https://arxiv.org/abs/2608.29410
pdf_url: https://arxiv.org/pdf/2608.29410
published: '2026-08-29'
collected: '2026-09-01'
category: RecSys
direction: 多模态推荐 · Agent知识增强
tags:
- Multimodal Recommendation
- Agent
- Knowledge Memory
- Graph Enhancement
- Reranking
- LLM4Rec
one_liner: 双Agent架构将LLM行为感知知识转化为图、表示、重排信号，显著提升多模态推荐性能
practical_value: '- 可直接复用双Agent离线构建知识记忆的思路：训练阶段仅用训练集的用户交互+多模态内容生成用户偏好、商品属性KV记忆，无测试数据泄露风险，适配电商多模态推荐场景合规要求

  - 行为感知同质图构建方法可低成本迁移到现有图推荐骨干：将LLM生成的用户/商品语义编码后计算相似度建图，替换原有纯模态相似度的item-item/user-user图，实测可给现有SOTA基线带来3%~4%的Recall@20提升

  - 冻结记忆的多阶段优化方案可降低落地成本：知识记忆、图结构均离线预生成，训练阶段仅优化推荐骨干，与现有训练链路完全兼容，无需重构全流程

  - 稀疏用户、冷启动商品场景可优先试用：在0-5次交互的新用户、无交互冷启商品下效果增益更明显，比现有基线冷启Recall@20最高提升15%以上，适合电商新品、新用户推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐大多直接注入图文特征或基于模态相似度建图，存在明显语义gap：视觉/文本的显著特征（如营销话术、外观配色）往往和用户实际交互动机弱相关，导致构建的图关联不准、排序信号与推荐目标脱节；现有LLM增强推荐方案要么仅做特征增强，要么直接用LLM重排，未将LLM输出的语义知识转化为可复用的推荐结构，难以兼容现有推荐链路，冷启动、稀疏场景效果受限。
### 方法关键点
- 双Agent离线分工：Integrator Agent仅用训练集的用户交互+商品多模态内容，抽取文本/视觉/跨模态三类行为感知的用户偏好、商品属性，存入KV结构的可复用知识记忆，不参与训练迭代
- Utilizer Agent基于记忆实现三层增强：1）编码记忆后计算相似度，构建行为感知的user-user、item-item同质图；2）用记忆修正原有纯模态相似度的item-item图，生成统一关联图；3）将记忆编码拼入用户/商品初始表征输入图推荐骨干训练，最终基于记忆对候选列表重排
- 训练时仅用训练数据更新记忆，验证、测试阶段记忆完全冻结，杜绝数据泄露
### 关键结果
在Amazon三个公开多模态数据集（Baby、Sports、Clothing，稀疏度99.88%~99.97%）上对比17个SOTA基线，Recall@20最高提升9.9%（Sports数据集），NDCG@20最高提升10.1%；生成的知识图可直接迁移到SMORE、MENTOR等现有推荐骨干，平均提升Recall@20 3.5%；0-5次交互的稀疏用户、冷启动商品下增益更显著，冷启场景Recall@20最高提升15.9%。

**最值得记住的一句话**：多模态推荐中LLM输出的语义知识不要仅作为增强特征或重排输入，转化为行为感知的图结构和可复用记忆能带来更大的性能增益。
