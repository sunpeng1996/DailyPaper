---
title: Federated Recommender Agents
title_zh: 联邦推荐智能体：基于自然语言知识共享的隐私保护推荐框架
authors:
- Jaehyung Lim
- Woojoo Kim
- Junyoung Kim
- Dongha Kim
- Wonbin Kweon
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology
- Sungkyunkwan University
arxiv_id: '2610.39289'
url: https://arxiv.org/abs/2610.39289
pdf_url: https://arxiv.org/pdf/2610.39289
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 联邦推荐 · LLM Agent 隐私协同
tags:
- Federated-Recommendation
- Recommender-Agent
- LLM4Rec
- Privacy-Preserving
- Knowledge-Sharing
one_liner: 提出无需更新LLM参数的联邦推荐Agent框架，通过结构化知识共享实现隐私保护下的跨用户协同
practical_value: '- 做隐私合规的端侧电商推荐场景时，可直接复用C-T-R结构化知识单元，不用传输用户原始行为和偏好，仅上传抽象后的通用决策逻辑，可满足GDPR、CCPA等隐私法规要求

  - 端侧小参数量LLM部署推荐Agent时，可复用双内存设计：语义内存存储用户偏好、决策内存存储用户选择倾向，拆分后个性化信息保留率比统一内存高10%以上，推荐准确率提升显著

  - 跨用户知识聚合无需做模型参数联邦更新，改用自然语言知识分层蒸馏+跨分支判别优化，可大幅降低端侧算力开销，适配手机、智能设备等资源受限终端部署

  - 冷启动/稀疏行为用户的推荐场景，可直接复用全局共享的决策推理库，无需依赖用户大量历史行为，稀疏场景下NDCG@10比基线最高提升9.19%，可有效缓解冷启动问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的推荐Agent依赖中心化收集用户行为与偏好数据，存在隐私合规风险；孤立部署在端侧的推荐Agent无法跨用户学习通用决策经验，而传统联邦推荐方案需要频繁更新LLM参数，端侧算力开销过高，无法落地资源受限的终端场景。

### 方法关键点
- 设计Condition–Transition–Reasoning（C–T–R）结构化知识单元：抽象用户行为上下文、决策跳转方向、选择逻辑，隐去具体用户/物品ID，作为跨用户共享的最小单元
- 端侧双私有内存设计：语义内存存储用户偏好，决策内存存储不同上下文下的用户选择倾向，所有私有数据全程保留在本地
- 服务端分层知识整合：按Condition→Transition层级组织全局知识库，同分支内蒸馏合并重复推理，跨分支做判别优化，明确不同跳转逻辑的适用边界
- 全流程冻结LLM参数：所有个性化和协同学习通过更新自然语言知识实现，无Fine-tuning算力开销

### 关键实验结果
在亚马逊3个领域（CDs & Vinyl、Musical Instruments、Office Products）的稠密/稀疏共6个数据集上，对比11个基线（含传统联邦推荐、联邦化序列模型、联邦化LLM推荐方法），最优变体NDCG@10比最强基线提升1.54%~9.19%，MRR提升3.01%~16.29%，稀疏用户场景下增益更突出；ablation验证双内存、分层知识整合模块均带来显著性能提升。

### 核心结论
联邦推荐Agent的协同完全可以通过可解释的自然语言知识共享实现，无需传递隐私数据也无需更新LLM参数，兼顾隐私、性能和落地可行性
