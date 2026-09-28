---
title: 'CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized
  Text Generation'
title_zh: CARD：结合簇级适配与奖励引导解码的个性化文本生成框架
authors:
- Yutong Song
- Jiang Wu
- Weijia Zhang
- Chengze Shen
- Shaofan Yuan
- Weitao Lu
- Jian Wang
- Yu Wang
- Nikil Dutt
- Amir M. Rahmani
affiliations:
- University of California, Irvine
- Independent Researcher
- University of Amsterdam
- TikTok
arxiv_id: '2601.06352'
url: https://arxiv.org/abs/2601.06352
pdf_url: https://arxiv.org/pdf/2601.06352
published: '2026-09-19'
collected: '2026-09-28'
category: LLM
direction: LLM个性化生成 · 解码级偏好控制
tags:
- LoRA
- Personalized Generation
- Reward-guided Decoding
- User Clustering
- PEFT
one_liner: 分簇训练共享LoRA作为先验，解码阶段用轻量用户向量实现高效个性化生成
practical_value: '- 可复用「用户分簇+共享LoRA」架构到电商个性化文案生成、商品评论改写场景，无需存储每用户大参数，冷启动用户直接分配到对应簇即可获得基础个性化效果，大幅降低部署成本

  - 偏好对构造trick可直接复用：用簇级生成结果作为负例、用户真实文本作为正例，自动隔离语义差异仅保留风格偏差信号，无需人工标注即可获取高质量偏好训练数据

  - 解码阶段仅对Top-k候选token的logit做修正的工程优化，可将个性化计算复杂度降到O(kJ)（k远小于词表大小），能直接集成到现有LLM推理服务，不会明显增加推理延迟

  - 128维轻量用户偏好向量可存储在端侧，无需上传用户原始历史数据，符合隐私合规要求，适合端侧个性化Agent、电商APP端内个性化推送文案生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化文本生成方案存在明显缺陷：RAG类方法依赖检索质量，个性化程度浅；PEFT类方法需要为每个用户存储独立参数，规模化部署成本高、冷启动困难，且普遍缺乏低成本的高质量偏好标注信号，细粒度个性化和规模化部署的矛盾突出。

### 方法关键点
- 先基于用户历史文本的embedding做聚类，每个簇训练专属LoRA适配器作为群体共性偏好先验，低资源用户可直接复用簇参数解决冷启动问题
- 偏好对构造无需人工标注：同一prompt下，用簇LoRA的生成结果作为负例，用户真实输出作为正例，自动隔离语义差异，仅保留风格偏差作为监督信号
- 训练共享映射头和128维用户偏好向量，推理阶段冻结基座LLM和簇LoRA参数，仅对输出Top-k token的logit做低秩修正，通过超参β控制个性化强度

### 关键实验
在LaMP和LongLaMP共6个长短文本个性化生成任务上，对比RAG、PEFT、解码对齐等7类基线，10/12个指标位列第一；LaMP4新闻标题生成任务ROUGE-1达0.218，较非个性化基线提升49.3%；单用户仅需存储128维偏好向量，推理延迟接近原生模型，冷启动场景下仅需5条用户历史即可达到接近峰值的效果。

### 核心结论
个性化信号天然具备分层特性，群体共性先验加轻量解码级个体控制，是兼顾个性化效果、部署效率、规模化能力的可行路径。
