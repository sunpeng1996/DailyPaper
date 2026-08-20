---
title: 'UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource
  Music Understanding'
title_zh: UniVerse：面向文化包容的低资源音乐理解LALM基准与优化
authors:
- Ziya Zhou
- Shangda Wu
- Shenyang Xu
- Yutong Zheng
- Dafang Liang
- Suin Chung
- Danbinaerin Han
- Junyan Jiang
- Yongyi Zang
- Ruibin Yuan
affiliations:
- HKUST
- Sogang University
- KAIST
- NYU Shanghai
- Central Conservatory of Music
arxiv_id: '2608.17852'
url: https://arxiv.org/abs/2608.17852
pdf_url: https://arxiv.org/pdf/2608.17852
published: '2026-08-18'
collected: '2026-08-20'
category: Multimodal
direction: 多模态大模型 · 低资源文化内容理解
tags:
- LALM
- Low-Resource Learning
- Multimodal
- MoE
- Benchmark
one_liner: 构建多文化低资源音乐理解基准与自动训练集，优化大音频语言模型跨文化适配能力
practical_value: '- 低资源小众品类（如非遗文创、小众音乐周边）推荐场景，可复用「专家引导+自动化」的数据集构建pipeline，快速补全少样本标注

  - 跨文化/跨区域多模态推荐优化，可借鉴imbalance-aware训练策略搭配MoE架构，提升长尾小众内容的识别准确率

  - 多模态内容理解benchmark构建可参考半自动化标注流程，平衡标注质量与生产效率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有大音频语言模型（LALM）对不同文化背景的低资源民间音乐适配性差，难以捕捉其结构与风格特征，同时缺乏专属评估基准与训练方案，而民间音乐普遍存在资源稀缺、地域分布不均、记录不完善的问题。
### 方法关键点
1. 构建UniVerseBench评估基准，覆盖38+文化和语言实体，包含5042条问答对，采用专家引导的高度自动化流水线生产
2. 搭建全自动模型生成的多轮对话训练集UniVerseSet
3. 分别在密集架构和MoE架构上验证多模态不平衡学习策略的适配效果
### 关键结果
自动化数据构建结合不平衡感知训练可带来显著效果提升，但模型仍难以捕捉细粒度声学特征，表面模态对齐与深层内容理解之间仍存在明显差距
