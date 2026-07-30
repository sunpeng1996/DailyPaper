---
title: 'WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models'
title_zh: WhisperRec：面向基础推荐模型的高效隐式推理框架
authors:
- Hao Jiang
- Peiru Du
- Pengfei Yao
- Mengting Li
- Siyuan Lou
- Kuo Cai
- Sheng Yu
- Qiang Luo
- Jian Liang
- Ruiming Tang
affiliations:
- Kuaishou Technology
arxiv_id: '2607.26621'
url: https://arxiv.org/abs/2607.26621
pdf_url: https://arxiv.org/pdf/2607.26621
published: '2026-07-29'
collected: '2026-07-30'
category: GenRec
direction: 生成式推荐 · 隐式CoT推理优化
tags:
- WhisperRec
- Latent Reasoning
- Chain-of-Thought
- Semantic ID
- FRM
- GenRec
one_liner: 将显式CoT蒸馏为可学习隐式推理token，兼顾推荐效果与10倍+推理吞吐量
practical_value: '- 推理效率优化可参考：无需显式生成CoT文本，通过知识蒸馏将多视角推理能力压缩到3个左右隐式token，推理吞吐量可提升10倍以上，完全适配在线推荐低延迟要求

  - CoT监督构建Trick：采用多视角自适应CoT（意图探索、候选评估、转化归因），按样本难度分配推理预算，避免简单样本过度推理浪费算力、复杂样本推理不足

  - 训练范式可复用：三阶段对齐+课程学习后训练，先对齐单/多视角CoT知识，再对齐推荐目标，最后按用户活跃度从高到低训练，适配工业场景稀疏用户分布'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的基础推荐模型（FRM）大多采用显式CoT推理优化推荐效果，但存在两大痛点：一是显式生成冗长推理文本会带来极高推理延迟，无法满足工业在线推荐要求；二是固定模板的CoT容易过度强调用户历史主导偏好，忽略短期上下文兴趣，推理错误还会传播导致推荐偏差。

### 方法关键点
- 提出Multi-View Adaptive CoT（MV-ACoT）：从意图探索、候选评估、转化归因三个视角生成CoT监督，同时根据样本难度自适应调整推理复杂度，简单样本用轻量推理，复杂样本加大多维度推理
- 三阶段隐式推理对齐：先基于预训练FRM，用单视角CoT预热隐式token，再用多视角CoT训练共享隐式表示，最后对齐推荐目标让隐式token成为用户上下文和推荐决策的桥梁
- 多阶段课程式后训练：按用户活跃度从高到低做推荐SFT，同时1:1混合普通推荐样本和带隐式token的推荐样本训练，兼顾两种模式的性能

### 关键实验
在快手公开LLM-Rec基准和快手本地生活工业数据集上测试，对比GRU4Rec、BERT4Rec、OneRec、OneReason等基线，WhisperRec相比显式CoT的Think版本SID@64提升17.44%，相比无CoT的No-Think版本SID@64提升9.33%，同时推理吞吐量达到显式CoT方法的10倍以上。

### 核心结论
推理收益来自于和决策相关的表征优化，而非生成冗长的自然语言推理文本。
