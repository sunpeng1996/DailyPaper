---
title: Is One Score Enough? Assessing Singing Quality of Songs with Temporal Score
  Curves
title_zh: 单评分足够吗？基于时序评分曲线的歌曲演唱质量评估
authors:
- Yishan Lv
- Jing Luo
- Xinyu Yang
- Zhizheng Wu
affiliations:
- Xi'an Jiaotong University
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.16599'
url: https://arxiv.org/abs/2607.16599
pdf_url: https://arxiv.org/pdf/2607.16599
published: '2026-07-18'
collected: '2026-07-24'
category: Other
direction: 全长度歌曲演唱质量评估 · 时序评分建模
tags:
- Singing Quality Assessment
- Temporal Modeling
- Pseudo Label
- Self-Attention
- Two-Stage Framework
one_liner: 提出无需手动片段标注的两阶段全长度歌曲演唱质量评估框架，可输出时序质量曲线
practical_value: '- 做长内容（长音频/长视频/长图文）质量评估时，可复用两阶段框架：先做片段级伪标签打分，再聚合得到整体评分，降低细粒度标注成本

  - 片段特征到整体评分的聚合环节，可借鉴「可学习全局embedding + self-attention」的结构，自动加权高价值片段的质量特征

  - 需输出细粒度质量分布的业务场景（比如K歌类APP逐段评分、长内容质量劣化定位），可参考时序评分曲线的生成逻辑'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有演唱质量评估（SQA）方案仅适配短演唱片段，无法满足全长度歌曲的分段质量波动建模需求；片段级人工标注稀缺，直接为所有片段分配全局整体评分会忽略片段间质量差异，无法实现有效监督。
### 方法关键点
提出两阶段SongSQA框架：1）第一阶段用预训练教师模型生成伪标签训练Segment Score Predictor，无需手动片段标注即可输出片段级演唱质量分；2）第二阶段通过Song Quality Aggregator融合片段特征与预测分得到统一片段embedding，结合可学习全局歌曲embedding与self-attention建模片段表现与全局质量的关联，动态聚合特征输出整体评分，同时生成时序片段质量曲线。
### 关键结果
相比最优基线，KTAU相对提升最高达13.95%，所有数据集下其余评估指标均实现稳定提升。
