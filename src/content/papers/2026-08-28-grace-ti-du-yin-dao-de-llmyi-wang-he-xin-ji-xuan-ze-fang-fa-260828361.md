---
title: GRACE:Gradient-guided Coreset Selection for LLM Unlearning
title_zh: GRACE：梯度引导的LLM遗忘核心集选择方法
authors:
- Praveen Bushipaka
- Andrea D'Angelo
- Lucia Passaro
- Tommaso Cucinotta
affiliations:
- University of Pisa
- Scuola Superiore Sant’Anna
- Aarhus University
arxiv_id: '2608.28361'
url: https://arxiv.org/abs/2608.28361
pdf_url: https://arxiv.org/pdf/2608.28361
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM遗忘 · 核心集选择
tags:
- LLM Unlearning
- Coreset Selection
- Gradient Guidance
- Orthogonal Matching Pursuit
- Rademacher Hashing
one_liner: 仅用少量不良行为样本自动构建遗忘/保留核心集，优化LLM遗忘的效用-遗忘权衡
practical_value: '- 处理电商LLM应用的合规遗忘需求时，可复用GRACE的梯度引导核心集选择逻辑，仅需少量侵权/不良内容样本就能生成遗忘集，无需遍历全量训练数据，大幅降低合规成本

  - 保留集选择的梯度投影+聚类OMP策略可迁移到推荐系统的增量微调场景：剔除目标概念梯度后选代表性样本，既能更新特定内容又不破坏整体推荐效果

  - 可直接对接现有GradDiff、NPO等主流LLM遗忘算法，无需修改算法逻辑就能获得5-6%的模型效用提升，同时遗忘效果不下降

  - 梯度用Rademacher哈希降维的trick可复用，把LLM大梯度压缩到64k维，相似度计算效率提升上百倍，适合工业级大模型的数据筛选场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM遗忘方法默认遗忘/保留集已预先给定，但实际场景下的合规请求（如GDPR被遗忘权、版权内容删除、不良内容清除）通常仅提供少量不良行为示例，无法定位所有相关训练样本，手动构建数据集成本极高；现有基于余弦相似度的样本选择方法未考虑梯度冗余，易导致遗忘不充分或通用效用大幅下降。

### 方法关键点
- 先从少量不良行为种子样本计算平均梯度作为遗忘方向gf，用余弦相似度召回top-n候选遗忘样本，再通过非负正交匹配追踪（NNOMP）筛选紧凑遗忘核心集，保证所有样本梯度正向匹配gf，无冗余
- 剩余样本先投影剔除gf方向分量，仅保留与遗忘无关的梯度分量，再通过K-means聚类拆分梯度空间，每个簇内用OMP选代表性样本组成保留核心集，确保保留集覆盖通用能力且不混入遗忘相关内容
- 输出的两个核心集可直接输入任意支持保留集的LLM遗忘算法，无额外适配成本

### 关键实验
在MUSE（哈利波特版权内容遗忘）、WMDP-Bio（生物安全风险内容遗忘）两个数据集，对比Embedding检索、RASLIK两个基线，在LLaMA 3.1 8B、Qwen 2.5 3B两个模型，以及GradDiff、NPO等4种遗忘算法上测试：遗忘检索准确率最高超基线20个百分点，模型效用平均提升5-6个点，遗忘质量与基线差距小于0.012，基本无损失。

### 核心结论
LLM遗忘的效果主要由遗忘算法决定，而数据选择对模型效用的影响远大于对遗忘质量的影响，选择与遗忘方向正交的保留集可在不牺牲遗忘效果的前提下显著提升通用性能。
