---
title: 'rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience
  Memory for Recommendation'
title_zh: rEDMRec：将大模型推理蒸馏为可编辑经验记忆的推荐框架
authors:
- Minh Hoang Nguyen
- Tung Le
- Huy Tien Nguyen
affiliations:
- University of Science, Ho Chi Minh City, Vietnam
- Vietnam National University, Ho Chi Minh City, Vietnam
arxiv_id: '2608.18952'
url: https://arxiv.org/abs/2608.18952
pdf_url: https://arxiv.org/pdf/2608.18952
published: '2026-08-19'
collected: '2026-08-20'
category: GenRec
direction: 生成式推荐 · 推理蒸馏与可编辑记忆
tags:
- LLM4Rec
- reasoning distillation
- editable memory
- multi-agent debate
- memory-augmented recommendation
one_liner: 将大模型教师的推荐推理蒸馏到四通道可编辑记忆，让轻量学生模型无需重训即可获得推理增益
practical_value: '- 可直接复用四通道记忆架构（长/短期偏好、物品感知、反事实），针对业务所用排序模型的容量灵活裁剪通道：强LLM可去掉冗余的长偏好/反事实通道降低干扰，小模型保留全通道补全能力短板

  - 记忆维护可借鉴多智能体辩论+增删改查操作的无训练优化方案，无需微调排序模型，仅通过优化记忆内容即可提升推荐效果，适合电商推荐快速响应用户兴趣漂移、badcase修正的需求

  - 可直接复用记忆优化的成本控制经验：用记忆duplicate率作为记忆质量前置评估指标，辩论agent数选4个、优化3个epoch即可获得80%以上的增益，平衡效果和推理成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有大模型推理增强推荐需要每次请求重新生成推理过程，推理成本高且结果一次性使用无法复用，用户兴趣漂移时也难以针对性修正；现有推理蒸馏方案将知识固化到模型参数中，更新需要重训，灵活性极差，难以适配业务快速迭代需求。
### 方法关键点
- 架构拆分：离线用大模型教师生成推理结果，蒸馏到四类独立可编辑经验记忆通道（长期偏好、短期上下文、物品感知、反事实hard negative对比），在线用冻结的轻量学生模型直接检索记忆完成排序，全程不调用教师模型，解耦推理成本与在线延迟
- 记忆控制器：支持Add/Delete/Modify/Keep四种原子操作，可选K-agent辩论+仲裁机制优化记忆内容，降低重复率、提升精准度，全程无需更新学生模型参数
- 分类型存储：前三类记忆用向量库存储，反事实记忆用向量+图混合存储，不同通道设置独立检索过滤规则
### 关键结果
在ML-1M、Amazon Beauty、Steam三个公开数据集，覆盖3B-20B参数量的10款学生模型上验证：1. 相比零样本、少样本、普通RAG，所有学生模型的HR@1均有提升，相比GraphRAG在大部分模型上领先，ML-1M数据集上Qwen2.5 3B的HR@1相对次优基线提升13.3%；2. 通道消融显示：短期上下文是唯一全容量段都有效的通道，长期偏好、物品感知、反事实通道的效果随学生模型容量提升出现反转（强模型移除后效果反而更好）；3. 辩论优化可将记忆重复率降低7.4个百分点，下游HR@1最高提升0.029，4个辩论agent、3个优化epoch即可达到性价比拐点。

> 最值得记住的一句话：大模型推荐的推理能力可以通过结构化可编辑记忆的方式沉淀复用，无需把所有知识都塞进模型参数，记忆优化的增益可以直接传导到下游排序效果
