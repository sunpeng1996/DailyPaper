---
title: 'LazUnirec: Unifying Retrieval and Ranking in Multi-scenario Industrial Recommendation'
title_zh: LazUnirec：多场景工业推荐下的统一检索与排序框架
authors:
- Xiaodong Li
- Junfeng Zhang
- Shichao Nie
- Ziyue Guo
- Yiming Liu
- Xinxin Xu
- Xurong Li
- Jinyuan Dang
- Zhanming Ou
- Jianan Yan
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2611.32590'
url: https://arxiv.org/abs/2611.32590
pdf_url: https://arxiv.org/pdf/2611.32590
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 工业推荐 · 召回排序统一建模
tags:
- Unified-Retrieval-Ranking
- LoRA
- MoE
- Multi-scenario-Rec
- Gradient-Conflict
one_liner: 通过任务公私参数拆分、梯度不确定性估计解决统一检索排序的梯度冲突，线上GMV最高提升4.01%
practical_value: '- 梯度冲突缓解方案可直接复用：Attention层加任务级LoRA，FFN层用任务私有+共享专家的稀疏MoE，实测降低30%+强梯度冲突，无需改造原有Transformer结构，改造成本低

  - 多任务梯度加权方案可迁移：基于历史梯度方向的EMA方差计算动态权重，自动给更稳定的梯度更高权重，无需手动调多任务loss权重，适配多场景多任务训练

  - 线上部署优化组合可落地：KV cache复用跨阶段/跨请求的用户序列编码+Kernel融合+跨场景拼batch，实测可将单模型QPS提升1倍以上，适配大流量多场景推荐

  - 跨任务蒸馏路径可复用：用排序的CTR logits做教师信号listwise蒸馏召回的偏好分布，可让召回HR@100提升2%以上，补充召回侧的细粒度信号'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐传统级联召回排序架构存在目标不一致、用户序列重复编码、算力浪费的问题，近年统一召回排序的方案存在严重梯度冲突，Attention和FFN层的普通梯度冲突率分别达45.85%、47.54%，强冲突率接近40%，导致联合训练效果受损，多场景下问题更突出。

### 方法关键点
- 输入层设计统一序列：拼接用户交互序列、触发token、召回query token、排序候选token，加结构化掩码控制信息流动，避免不同任务token互相干扰
- Transformer层拆分公私参数：Attention层用LoRA调制，共享基础QKV参数，召回、排序任务各加私有低秩适配；FFN层用任务自适应稀疏MoE，每个任务配1个私有专家+动态路由选2个共享专家，兼顾知识共享和任务特异性
- 梯度优化加不确定性估计：基于历史梯度方向的EMA方差计算每个任务每个场景的梯度可靠性，动态调整loss权重，高波动梯度自动降权，解决冲突时的更新方向问题
- 跨任务知识蒸馏：用排序的CTR logits做教师信号，listwise蒸馏召回的候选偏好分布，实现排序的细粒度信号向召回迁移

### 关键实验
基于阿里国际站多场景连续25天工业日志训练，对比UniPinRec、UniR2、OneTrans-V2等SOTA统一模型，离线召回HR@100最高提升8.19%，排序CTR AUC最高提0.31%；线上A/B测试无触发场景GMV提4.01%，触发式场景GMV提3.06%，部署优化后QPS合计提升128%。

统一召回排序的核心瓶颈是梯度冲突，通过"公私参数拆分+动态梯度加权+跨任务蒸馏"的组合方案，能在降低算力成本的同时拿到显著业务收益。
