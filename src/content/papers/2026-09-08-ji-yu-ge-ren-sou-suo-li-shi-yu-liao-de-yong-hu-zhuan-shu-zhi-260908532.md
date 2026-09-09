---
title: 'Individual Text Corpora Predict User-Specific Knowledge: Benchmarks of Individualized
  Knowledge Simulation'
title_zh: 基于个人搜索历史语料的用户专属知识预测基准研究
authors:
- Christoph Wigbels
- Ali Abusaleh
- Markus T. Jansen
- Alexander Mehler
- Manuel Schaaf
- Markus J. Hofmann
affiliations:
- Bergische Universität Wuppertal
- Goethe-Universität Frankfurt
arxiv_id: '2609.08532'
url: https://arxiv.org/abs/2609.08532
pdf_url: https://arxiv.org/pdf/2609.08532
published: '2026-09-08'
collected: '2026-09-09'
category: LLM
direction: 个性化LLM · 用户知识建模
tags:
- Personalized-LLM
- RAG
- LoRA
- User-Profiling
- Knowledge-Simulation
one_liner: 基于用户搜索历史语料结合RAG验证可检测的个人知识信号，给出落地阈值与优化方向
practical_value: '- 构建用户画像/做个性化推荐时，可复用「搜索历史语料+RAG」的方案提取用户隐性知识/兴趣信号，当用户行为语料规模超过500万token时，知识预测效果会出现显著跃升。

  - 个性化类任务优先选用1B级小模型，通过LoRA做任务适配即可达到可用效果，算力成本远低于大模型全量微调，且小模型受通用参数知识干扰更小，更容易对齐用户个体特征。

  - 优化个性化LLM不要只看全局答案正确率，要同时优化「用户行为匹配准确率」和对数损失，避免模型输出被通用知识主导，忽略用户的个性化决策特征。

  - 预测用户知识缺口（如推未接触过的内容/知识类商品）时，不能仅依赖搜索历史，需补充兴趣标签等辅助特征，搜索行为的缺失无法直接对应知识缺口。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM内置的参数知识是全局训练数据的聚合结果，无法反映单个用户的专属知识结构，而自适应辅导、个性化推荐、精准营销等场景都需要准确建模用户的知识储备与兴趣边界，传统用户画像依赖显性标签，缺少对隐性知识的挖掘能力，利用用户自然产生的搜索历史等行为语料模拟个人知识是可行的探索方向。

### 方法关键点
- 数据：采集316名用户的谷歌搜索历史，爬取访问URL构建个人语料库（IC），平均规模320万token，配套36道知识类选择题（12道公开基准题+24道未公开防污染题）作为标注。
- 模型：对比多个小模型后选择Qwen3-1.7B，用LoRA（r=8，α=16）在129道公开知识题上做任务微调，适配选择题输出格式。
- RAG pipeline：个人语料按400token分片、50token重叠，用nomic-embed-text生成768维向量存入Qdrant，推理时召回Top5相关片段注入prompt，要求模型优先基于个人语料作答。
- 评估维度：除常规答案正确率，新增用户匹配准确率（Match Accuracy，模型答案与用户真实答案一致率）、知识缺口准确率（CK-accuracy，预测用户答题对错的准确率）、对数损失三个个性化专属指标。

### 关键结果
- LoRA微调后Qwen3-1.7B在公开题上正确率81%，超过用户平均的63%和德国常模样本的59%；但在未公开题上正确率60%，低于用户平均的65%，验证了公开基准题存在训练数据污染问题。
- IC-RAG的用户匹配准确率整体达31%，显著高于25%的随机水平，证明个人搜索语料存在可检测的知识信号。
- 个人语料规模超过500万token的用户，语料大小与CK-accuracy的相关系数达0.36，效果显著提升。

### 核心结论
个性化LLM的核心瓶颈不是答案正确率，而是校准能力——让模型输出符合单个用户的真实行为分布，而非全局最优的正确答案。
