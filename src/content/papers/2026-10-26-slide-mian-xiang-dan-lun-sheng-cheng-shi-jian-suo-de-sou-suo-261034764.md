---
title: 'SLIDE: Search-to-List Item Distillation for Single-Rollout Generative Retrieval'
title_zh: SLIDE：面向单轮生成式检索的搜索到列表物品蒸馏方法
authors:
- Tianyu Zhan
- Gui Ling
- Ran Tao
- Kunhai Lin
- Tong Xiong
- Wang Yang
- Kaixuan Zhang
- Zhihong Chen
- Yuliang Yan
- Dan Ou
affiliations:
- Zhejiang University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2610.34764'
url: https://arxiv.org/abs/2610.34764
pdf_url: https://arxiv.org/pdf/2610.34764
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式检索 · Semantic ID 蒸馏优化
tags:
- Generative Retrieval
- Knowledge Distillation
- Semantic ID
- List-wise Generation
- Greedy Decoding
one_liner: 通过离线教师beam搜索构造列表蒸馏目标 实现性能超beam搜索的单贪婪解码生成式检索
practical_value: '- 工业生成式检索可直接复用范式：离线用大参数教师做item级beam搜索生成有序Semantic ID列表作为蒸馏目标，小参数学生单贪婪解码即可达到甚至超过beam搜索效果，大幅降低线上推理延迟与算力开销

  - 蒸馏目标设计trick：若核心优化HR@K，直接取K个教师beam搜索结果按分数排序构造目标即可，无需更长目标避免额外离线成本；保留教师输出顺序对头部HR和NDCG增益显著，不可随机打乱

  - 列表级RL优化收益更高：基于单贪婪解码的列表级生成做RL优化，HR@K提升幅度是item级beam搜索RL的5~10倍，适合后续CTR/CVR/多样性等业务指标迭代

  - 教师训练优化：训练教师时采用「转换>点击>曝光」的PF-Fine-Rank排序构造标签，可提升教师beam搜索召回质量，进一步传递给学生'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式检索依赖item级beam搜索生成候选，无法建模跨item依赖、难以优化列表级指标；直接训练列表式模型用单贪婪解码的性能比beam搜索低18.4%（淘宝搜索HR@20），核心原因是beam搜索探索空间更大、稀疏正信号的位置偏差导致尾部位置监督不足。

### 方法关键点
- 三步蒸馏框架：① 教师训练：用PF-Fine-Rank（转换>点击>曝光排序）的列表标签训练大参数教师模型；② 离线蒸馏目标构造：对每个请求用教师做item级beam搜索，取Top-K结果按beam分数降序拼接Semantic ID作为列表式硬标签；③ 学生训练：小参数学生用上述硬标签做列表式SFT，推理时单贪婪解码直接生成完整Top-K候选列表。
- 核心设计：搜索到列表转换把多路径beam搜索的独立候选转为单轨迹的序列生成目标，既补充了原始行为标签外的高相关监督信号，又解决了列表位置的监督偏差问题，同时离线教师scaling不影响线上部署成本。

### 关键实验
在公开数据集FORGE和淘宝搜索工业数据集验证，0.5B参数学生：① 用0.5B教师蒸馏后，淘宝搜索HR@10比直接训练的贪婪解码提升34.8%，仅比beam搜索低3.94%；② 用7B教师蒸馏后，HR@10超过beam搜索1.78%，HR@20提升0.5%；③ 基于该框架的列表级RL优化，HR@1相对提升7.67%，是item级RL提升幅度的9倍。

### 最值得记住的一句话
生成式检索无需线上beam搜索，通过离线蒸馏把beam的探索能力转移给小模型，单贪婪解码就能实现更高性能、更低延迟的线上服务。
