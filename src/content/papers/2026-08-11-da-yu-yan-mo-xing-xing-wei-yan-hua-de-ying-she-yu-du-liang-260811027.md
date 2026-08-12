---
title: Mapping and Measuring the Behavioral Evolution of Large Language Models
title_zh: 大语言模型行为演化的映射与度量方法研究
authors:
- Dong Qiao
- Chris Ding
- Jicong Fan
affiliations:
- School of Data Science, The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2608.11027'
url: https://arxiv.org/abs/2608.11027
pdf_url: https://arxiv.org/pdf/2608.11027
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: LLM行为评估 · 无标注度量
tags:
- LLM
- Behavioral Evaluation
- Unsupervised Metric
- Model Comparison
- Embedding
one_liner: 提出三类无标注度量方案，量化32款不同家族LLM的行为差异与代际演化规律
practical_value: '- 可复用无标注行为差异度量方案，用于对比不同迭代版本的业务LLM（如文案生成、Agent决策模型）的行为漂移，避免全量人工标注

  - 小参数量Encoder（73×更小）即可保留模型行为相似度排序，可低成本落地业务侧LLM迭代的自动评估链路

  - 推理导向模型输出分布更紧凑的结论，可指导业务Agent/LLM微调目标设计，降低生成结果的不可控性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM榜单仅输出能力得分，无法体现不同模型的行为差异、跨代演化规律，也无法支撑模型间的关系分析。

### 方法关键点
采集6个模型家族共32款LLM对1万条通用prompt的返回结果，构建三类互补的行为差异度量指标：对齐后的单prompt平均距离、PCA压缩的prompt级分歧摘要、无需对齐的Gromov-Wasserstein内部响应几何差异，同时可搭配token级MMD交叉校验，整套方案无标注依赖。

### 关键结果数字
三类度量一致性高，token级MMD与句级平均距离的Spearman相关系数达0.98；同家族模型聚类效果显著，GPT-2为全局离群点；跨家族模型行为距离随时间递减，近期推理导向模型的响应分布紧凑度更高；最小Encoder仅为原尺寸1/73时仍可保留相似度排序、离群点识别、时间趋势等核心结论。
