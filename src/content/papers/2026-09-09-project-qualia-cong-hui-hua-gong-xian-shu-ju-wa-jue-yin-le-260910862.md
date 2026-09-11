---
title: 'Project Qualia: Recovering Experiential Music Structure from Session Co-occurrence
  Data'
title_zh: Project Qualia：从会话共现数据挖掘音乐体验式相似结构
authors:
- Nizam Mohammed
- Abu B. S. Rahman
- Dimuthu D. K. Arachchige
affiliations:
- Independent Researcher
- Hampton University
arxiv_id: '2609.10862'
url: https://arxiv.org/abs/2609.10862
pdf_url: https://arxiv.org/pdf/2609.10862
published: '2026-09-09'
collected: '2026-09-11'
category: RecSys
direction: 音乐推荐 · 会话共现item表征学习
tags:
- Music Recommendation
- Session Co-occurrence
- Song2Vec
- Self-supervised Learning
- Item Embedding
one_liner: 基于会话共现训练Song2Vec，通过艺术家残差法提取独立于艺术家的音乐体验式相似信号
practical_value: '- 内容/商品会话推荐场景可复用该自监督范式：将单会话作为句子、item作为token，用Word2Vec快速预训练得到高质量item嵌入

  - 若item嵌入被品牌/艺术家/类目等强特征主导，可参考「减去对应类目中心向量取残差」的方法，提取跨类目的细粒度相似信号

  - 冷启动或拓展推荐多样性时，可基于残差空间的高相似度配对做跨品类/跨艺术家关联召回，提升推荐惊喜度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有音乐推荐系统依赖元数据、协同过滤等技术，无法捕捉超越流派/艺术家分类的用户体验式歌曲相似性，难以产出高惊喜度的推荐结果。
### 方法关键点
1. 构建大规模听歌会话数据集：从Last.fm爬取9396用户共12.9亿播放记录，预处理得到2860万会话、5.316亿训练样本；
2. 基于skip-gram Word2Vec训练Song2Vec，将单个会话视为句子、单曲视为token学习歌曲嵌入；
3. 提出艺术家残差法：将每首歌的嵌入减去对应艺术家的质心向量，过滤艺术家主导的强信号，提取更细粒度的体验式结构。
### 关键结果
原始嵌入空间跨艺术家平均余弦相似度为0.2487，残差空间降至0.0005；仍有4577对跨艺术家曲目相似度≥0.7，形成按流派、年代聚类的相干簇，跨作曲家古典钢琴曲相似度最高达0.95，验证了独立于艺术家的体验式相似信号存在。
