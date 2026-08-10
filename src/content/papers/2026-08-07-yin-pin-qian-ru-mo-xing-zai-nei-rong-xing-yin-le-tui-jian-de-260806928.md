---
title: 'From Classification to Recommendation: Empirical Analysis of Audio Embedding
  Models Application for Content-Based Music Recommendation'
title_zh: 音频嵌入模型在内容型音乐推荐中的应用实证分析
authors:
- Qingrui Li
- Haowei Lou
- Chengkai Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- University of New South Wales
- Macquarie University
arxiv_id: '2608.06928'
url: https://arxiv.org/abs/2608.06928
pdf_url: https://arxiv.org/pdf/2608.06928
published: '2026-08-07'
collected: '2026-08-10'
category: GenRec
direction: 生成式推荐 · Semantic ID 设计评测
tags:
- Audio Embedding
- Semantic ID
- Generative Recommendation
- Music Recommendation
- RVQ
one_liner: 系统评测6种音频编码器在3类音乐推荐系统的表现，给出Semantic ID设计实操指引
practical_value: '- 做内容驱动的生成式推荐（音乐、短视频、图文商品等）时，冷启动无交互数据场景优先选择领域对齐+跨模态对齐的预训练表征，比纯单模态自监督表征效果提升显著

  - 设计Semantic ID的RVQ结构时，优先增大codebook宽度，量化深度控制在2~3层即可，更深的层不仅不会提升推荐效果，还会带来训练不稳定、推理复杂度上升的问题

  - 如果推荐系统有充足的用户交互数据用于序列微调，预训练表征的选择对最终效果影响很小，可以优先选择计算成本低、部署简单的方案

  - 生成式推荐的Semantic ID可以仅保留前2层RVQ编码，即可覆盖绝大多数和用户偏好相关的信息，同时降低生成序列长度，提升推理速度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有预训练音频表征多针对分类、跨模态检索任务优化，其表征空间未适配推荐任务依赖的用户主观偏好匹配逻辑，且已有评测未覆盖基于Semantic ID的新兴生成式推荐范式，RVQ量化设计对生成式推荐效果的影响也缺乏系统性结论，无法给工业界提供实操指引。

### 方法关键点
- 覆盖6类代表性预训练音频编码器：语音域（Wav2Vec2、HuBERT）、音乐单模态自监督（Music2Vec、MERT）、跨模态对齐（通用CLAP-G、音乐域CLAP-Music）
- 评测3类主流推荐范式：无参数KNN内容推荐、序列推荐SASRec、基于Semantic ID的生成式推荐TIGER
- 控制变量测试RVQ的codebook宽度（64~4096）、量化深度（1~12）、前缀保留长度对生成式推荐效果的影响

### 关键结果
- 实验基于LFM1b（5k歌曲、8k用户、190w交互）、Music4All-Onion（5k歌曲、8.8k用户、197w交互）两个数据集
- 无交互微调时，CLAP-Music在KNN的Recall@50比语音类embedding高95%以上，是冷启动场景最优选择
- 经序列推荐交互微调后，不同编码器的性能差缩小至2%以内，预训练embedding的影响大幅降低
- 生成式推荐场景下，RVQ深度为3、codebook宽度1024/4096时效果最优，深度超过3层会导致最高70%的性能下降，仅保留前2层RVQ前缀比保留3层效果平均高5%

### 最值得记住的结论
Semantic ID设计优先分配容量给codebook宽度而非深度，下游有充足交互监督时预训练表征的选择优先级可让位于工程成本。
