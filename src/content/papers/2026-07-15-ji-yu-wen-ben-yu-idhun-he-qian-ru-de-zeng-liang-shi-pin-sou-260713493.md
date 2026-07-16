---
title: Personalizing Incremental Video Search with Hybrid Text and ID Embeddings
title_zh: 基于文本与ID混合嵌入的增量视频搜索个性化系统
authors:
- Vivek Kanojiya
- Vishalaksh Aggarwal
- Daeho Baek
- Lyndon Kennedy
- Xuetao Yin
affiliations:
- Apple
arxiv_id: '2607.13493'
url: https://arxiv.org/abs/2607.13493
pdf_url: https://arxiv.org/pdf/2607.13493
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 增量视频搜索 · 混合嵌入个性化排序
tags:
- Hybrid Embedding
- Personalized Search
- Learning to Rank
- Contrastive Learning
- XGBoost
- Incremental Search
one_liner: 面向增量视频搜索短前缀场景，基于文本+ID混合嵌入实现低时延个性化排序
practical_value: '- 电商搜索的下拉提示、短前缀联想等增量搜索场景优先做个性化优化，1-3字符短前缀的业务收益是长query的5-6倍，ROI远高于其他场景

  - 可直接复用混合嵌入的轻量接入方案：无需改动现有排序架构，仅将两路user-item cosine相似度特征加入XGBoost ranker即可，低时延还能拿到大部分收益

  - 用LLM标注无偏的嵌入质量评估数据集，不需要依赖有曝光偏差的点击日志，即可快速迭代不同嵌入模型的效果

  - 用户表示初期不用上复杂的序列模型，用历史item嵌入的mean pooling就足够好用，工程成本极低，收益显著'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
增量搜索要求每输入一个字符就返回结果，1-3字符的短前缀query词汇匹配信号极弱，非个性化排序只能依赖全局热度，用户往往需要输入更多字符才能找到目标内容，是搜索体验的核心瓶颈，且这类短前缀流量占比高，优化ROI远高于成熟的长query场景。

### 方法关键点
- 训练两路互补item嵌入：TextEmb基于多语种语义编码器，输入item元数据（标题、品类、演职人员等），通过对比学习训练，覆盖全品类和冷启动item；IdEmb是基于item ID的协同嵌入，仅用用户搜索会话的连续转化对训练，捕捉跨语义的行为共现信号
- 在线用户表示用最近观看历史的item嵌入做mean pooling，计算两路user-item cosine相似度作为新增特征，直接接入原有pairwise XGBoost ranker，不改动现有检索排序架构，时延开销极低
- 构建LLM标注的无偏嵌入评估数据集，基于item元数据判断相似性，避免点击日志的曝光偏差，用于嵌入模型的快速迭代

### 关键结果
离线时序拆分测试集上，对比非个性化基线，有历史用户的NDCG@10提升2.99%、MRR提升3.30%；1-3字符短前缀query的NDCG@10涨幅达8.63%，是长query（>3字符）涨幅的近6倍。线上3周A/B测试显示，点击率提升1.14%、转化率提升1.23%，转化item排名提升2.91%，均达到统计显著性。

### 核心结论
低词汇信号的短前缀增量搜索是个性化优化的最高ROI场景，混合语义+协同嵌入的轻量接入方案可以用极低工程成本拿到显著业务收益。
