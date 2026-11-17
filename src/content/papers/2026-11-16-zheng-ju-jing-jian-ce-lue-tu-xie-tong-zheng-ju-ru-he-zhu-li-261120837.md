---
title: 'Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates'
title_zh: 证据精简策略：图协同证据如何助力LLM候选排序
authors:
- Yuchong Hu
- Zhao Zhang
- Ziyao Zhao
- Haoyu Wang
- Jing Xiao
affiliations:
- University of Science and Technology of China
- Ping An Technology (Shenzhen) Co., Ltd.
arxiv_id: '2611.20837'
url: https://arxiv.org/abs/2611.20837
pdf_url: https://arxiv.org/pdf/2611.20837
published: '2026-11-16'
collected: '2026-11-17'
category: RecSys
direction: LLM4Rec 图协同证据排序优化
tags:
- LLM4Rec
- Graph Evidence
- Collaborative Filtering
- LLM Ranker
- Evidence Optimization
one_liner: 量化图协同证据的不同呈现形式对LLM推荐排序的影响，给出证据优化与融合方案
practical_value: '- 做LLM推荐重排序时，不要堆砌全量图路径，优先用「是否有支持、支持用户数、路径数」三个结构化数值特征，比原始路径省token，度匹配候选池NDCG@5可涨2.28~2.54个点

  - Prompt中加入无关文本会导致H@1下降3~6个点，但输出格式有效性几乎不受影响，业务prompt工程需严格控制冗余内容

  - LLM排序得分与传统图CF得分标准化后线性融合，可直接落地现有pipeline，整体H@1涨2.4~3.3个点，零支持候选池收益更高

  - 多候选均有图支持时，直接将数值化支持计数拼入prompt，比自然语言描述计数的NDCG@5高3~5个点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM推荐系统常直接将全量图协同路径、邻域信息拼接进prompt，既带来过高token开销，又容易引入噪声干扰排序效果，但行业内缺乏对不同证据形式、分配方式的量化效果评估，无法明确哪些证据是排序的核心增益来源，哪些是冗余无效的。

### 方法关键点
- 设计两组对照实验套件：Suite I基于Qwen3（0.6B/1.7B/4B）在Amazon Books数据集测试不同证据源、prompt负载、模型规模对排序效果的影响；Suite II基于Qwen3-4B、GLM-4-9B在Amazon Books、Amazon MovieTV两个数据集，对比原始路径、结构化统计、数值化计数三类图证据呈现形式的效果差异。
- 设计证据跨用户替换、计数重分配、度匹配候选池等对照实验，分离「识别有支持候选」和「多支持候选间排序」两个任务的效果贡献。
- 验证LLM排序得分与传统图CF得分的融合方案，评估两类信号的互补性。

### 关键结果
- 结构化统计证据比原始路径文本在度匹配候选池的NDCG@5分别提升2.28（Books）、2.54（MovieTV）个点；错误分配候选的计数会导致NDCG@5下降3.26~4.06个点。
- 测试时在prompt中加入无关文本，H@1从44.77%降至38.70%，但输出格式有效率仍保持99.9%。
- LLM排序得分与传统CF得分标准化后线性融合，整体H@1提升2.41~3.34个点，零图支持的候选池收益更高。
- 4B参数模型输出格式有效率达100%，1.7B仅43.6%，0.6B仅25.6%，小模型无法稳定支撑排序任务。

### 核心结论
LLM推荐排序的图协同证据不是越多越好，结构化、数值化的精简证据比全量原始路径效果更优，同时能大幅降低token开销。
