---
title: Unifying Generative Recall and Multi-Objective Ranking in a Single Decoder-Only
  Sequence
title_zh: 基于单Decoder序列的生成式召回与多目标排序统一框架
authors:
- Ruochen Yang
- Shuang Wen
- Pengbo Xu
- Yusheng Huang
- Jiangxia Cao
- Shuang Yang
- Zhaojie Liu
- Jiawei Sheng
- Tingwen Liu
affiliations:
- 中国科学院信息工程研究所
- 中国科学院大学网络空间安全学院
- Kuaishou Technology
arxiv_id: '2607.24439'
url: https://arxiv.org/abs/2607.24439
pdf_url: https://arxiv.org/pdf/2607.24439
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 召回排序统一架构
tags:
- Generative Recommendation
- Semantic ID
- LoRA
- Multi-Objective Ranking
- Unified Architecture
one_liner: 提出UniR2单Decoder统一框架，融合生成式召回与多目标排序，消除级联推荐系统的信息损耗与冗余计算
practical_value: '- 多阶段统一架构设计可复用：将用户上下文、SID轨迹、item特征拼接为单一输入序列，用Dual-Query Prefix-Causal
  Attention实现不同任务的可见性控制，既共享底层参数又避免任务冲突，适合工业级推荐系统精简链路

  - 任务优化隔离trick可直接落地：召回主干训练完成后再接入排序分支，排序侧仅通过LoRA更新低秩参数，不破坏生成式召回的语义稳定性，解决多任务优化的跷跷板问题

  - 推理效率优化可参考：缓存召回阶段生成的用户前缀与SID轨迹KV cache，排序阶段仅需计算新增item特征的token，同时将策略过滤与排序计算并行，端到端延迟降低54.29%

  - 采样策略可迁移：训练阶段全量样本供给排序任务做正负对比，召回任务单独下采样保留曝光分布拟合，平衡两个任务的训练目标需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐系统传统级联架构将召回、排序拆分为独立模块，存在目标不一致、阶段间信息损失、用户上下文重复计算等问题；当前生成式召回与Transformer排序的架构同质化高，具备天然融合基础，但直接参数共享会因任务信息可见性、优化目标差异导致性能跷跷板。

### 方法关键点
1. 统一输入序列：拼接用户上下文、item的SID生成轨迹、item特征三类token为单序列输入
2. DQ-PCA注意力机制：召回分支仅可见用户上下文+已生成的前缀SID，满足自回归生成要求；排序分支可见用户profile+完整SID轨迹+item特征，支持全信息特征融合，两类查询共享基础注意力权重
3. 优化隔离设计：先单独训练生成式召回主干，再接入排序分支；排序侧仅在注意力Q/K/V投影层加入LoRA做任务自适应，梯度不回传给召回主干，避免破坏生成语义

### 关键实验
在快手4亿用户规模的直播业务数据集上测试，离线召回HR@128相对SOTA提升3.86%，CTR AUC提升0.75%，礼物打赏GTR AUC提升0.16%；线上A/B测试快手主端播放量提升1.177%，点赞率提升2.56%，快手极速版打赏总额提升2.569%，端到端推理延迟降低54.29%。

生成式召回与多目标排序的融合核心是前向传播的表示耦合与反向传播的优化隔离，而非简单的参数共享。
