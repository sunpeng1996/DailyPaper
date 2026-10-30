---
title: 'PRISM: Personalized Item Representations in User History'
title_zh: PRISM：面向用户历史的个性化物品表征方法
authors:
- Renzhi Wu
- Zikun Cui
- Junjie Yang
- Li Sheng
- Yongjun Xie
- Jerry Fu
- Nipun Mathur
- Sri Reddy
- Hong Li
affiliations:
- Meta MRS
- Facebook Discovery
arxiv_id: '2610.39175'
url: https://arxiv.org/abs/2610.39175
pdf_url: https://arxiv.org/pdf/2610.39175
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 序列推荐 · 个性化历史表征
tags:
- Sequential Recommendation
- Personalized Embedding
- User History Modeling
- Scaling Law
- Autoencoder
one_liner: 复用上游排序隐层状态生成个性化历史物品嵌入，提升序列推荐效果
practical_value: '- 可复用「复用上游排序隐层状态生成个性化物品嵌入」的设计，避免额外训练单独用户-物品模型的算力开销，适配工业级多阶段推荐链路

  - 多视角融合+自编码器压缩的trick可直接迁移：将用户塔、用户-物品塔、同请求会话交互的全层隐态归一化后拼接，用轻量自编码器压缩为128维INT8量化嵌入，存储和推理开销极低

  - 个性化历史长度的幂律缩放结论可直接指导业务选型：26-240事件区间内NE增益服从0.468指数的幂律，可根据算力预算选择最优历史长度，无需盲目拉长序列'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统序列推荐的物品初始嵌入为全局共享，无法体现同一物品对不同用户、甚至同一用户不同时间的关系差异，限制了输入层的个性化表达能力；而单独训练用户-物品模型生成个性化嵌入算力开销极高，无法落地亿级流量场景。

### 方法关键点
- 设计三个互补表征视角：用户塔捕捉事件发生时的用户全局兴趣、用户-物品塔建模用户与当前物品的交互关系、同请求候选混合模块引入会话上下文信息
- 隐层压缩机制：将三个模块的全层隐态分别归一化后拼接，用带stop-gradient的自编码器压缩为定长个性化嵌入，仅编码器用于线上推理，解码器仅参与训练阶段的重建任务
- 下游复用逻辑：存储压缩后的嵌入、时间戳与版本信息，下游序列模型将其与时间编码、元信息编码拼接后作为额外输入，原存储的嵌入固定不更新

### 关键实验
在Meta亿级流量的核心推荐场景Surface 1上测试，对比基线VISTA，PRISM实现平均NE下降0.15%（VISTA仅下降0.07%），其中点赞任务NE下降0.22%、评论任务下降0.20%；历史长度26-240事件区间内，NE增益服从指数为0.468的幂律，长度从26提升到240时NE增益从0.06%升至0.17%。

### 核心结论
个性化历史物品表征是推荐系统新的可扩展维度，通过复用上游计算即可实现效果与效率的平衡。
