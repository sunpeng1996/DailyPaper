---
title: Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning
title_zh: 面向端侧上下文学习的无梯度任务感知检索框架CoRA
authors:
- Xinyu Luo
- Hui Liu
- Yihua Shao
- Junyi Yang
- Arindam Basu
- Haoliang Li
affiliations:
- 香港城市大学
- 中国科学院自动化研究所
arxiv_id: '2607.27766'
url: https://arxiv.org/abs/2607.27766
pdf_url: https://arxiv.org/pdf/2607.27766
published: '2026-07-30'
collected: '2026-07-31'
category: RAG
direction: 检索增强 · 端侧无梯度ICL检索优化
tags:
- In-Context Learning
- On-Device AI
- Gradient-Free
- Retrieval Optimization
- Multimodal Retrieval
one_liner: 提出无梯度任务感知检索框架CoRA，无需微调或调用下游大模型即可实现端侧高质量ICL样例选择
practical_value: '- 端侧RAG/Agent的ICL样例检索可复用CoRA无梯度设计，无需微调检索模型，隐私性好计算开销低，适合端侧电商个性化prompt构建场景

  - 复用CKA层聚类选代表性层的trick，无需仅依赖最后一层embedding做检索，可整合多维度特征提升搜索query与item的匹配准确率

  - 端侧检索索引构建可复用双次流式计算方案，无需加载全量候选池，峰值内存不随候选池规模增长，适合移动端电商APP本地检索模块

  - 多模态检索场景可复用CoRA-M文本为主、视觉特征融合的设计，无需复杂跨模态对齐训练，可提升直播/短视频内容检索效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
端侧ICL需在调用大模型前检索样例构建prompt，现有方案存在明显缺陷：纯输入相似度检索未利用任务输入输出规律，效果差；微调检索器或反复调用下游大模型的方案不符合端侧算力、内存、隐私约束，难以落地。

### 方法关键点
- 基于层间CKA相似度聚类选择3个左右代表性编码器层，减少层间冗余，整合表层、语法、语义多维度特征信号
- 利用候选池输入输出对构建任务条件空间，通过闭式岭回归将输入特征对齐到该空间，再经低秩分解得到紧凑检索基，全程无梯度操作
- 仅离线建索引时使用候选输出，查询时仅需输入特征与预计算索引，支持双次流式索引构建，峰值内存不随候选池规模增长
- 扩展多模态版本CoRA-M，保留文本层选择逻辑，将视觉特征融入条件空间，统一支持文本、多模态检索场景

### 关键结果
在10个文本数据集、4个多模态基准上测试，下游覆盖Llama-3.2-1B、MobileLLM-Pro、Qwen3.5-2B、OpenFlamingo-3B等模型：文本分类/生成任务平均性能比最优基线（MLSM）最高提升3.8pct，多模态任务平均得分比最优基线（MMICES）最高提升2.6pct，Raspberry Pi 5端到端部署验证了落地可行性。

### 核心结论
无梯度闭式特征对齐即可实现媲美微调检索器的ICL样例检索效果，是端侧RAG/ICL落地的高性价比方案
