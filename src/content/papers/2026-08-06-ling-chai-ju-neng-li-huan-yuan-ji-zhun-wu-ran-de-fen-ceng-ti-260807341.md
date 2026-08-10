---
title: 'Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation
  and Step-wise Mitigation of Benchmark Contamination'
title_zh: 零差距≠能力还原：基准污染的分层逐题概率评估与分步缓解
authors:
- Ruijie Hou
- Yueyang Jiao
- Zhao Wang
- Yingming Li
affiliations:
- Zhejiang University
arxiv_id: '2608.07341'
url: https://arxiv.org/abs/2608.07341
pdf_url: https://arxiv.org/pdf/2608.07341
published: '2026-08-06'
collected: '2026-08-10'
category: Eval
direction: 大模型基准污染评估与缓解
tags:
- Benchmark Contamination
- LLM Evaluation
- Decoding Strategy
- SA-PPG
- RailCap
one_liner: 提出精准评估基准污染的SA-PPG指标与无需预检测的生成时污染缓解策略RailCap
practical_value: '- 自研LLM用于Agent推理、推荐文案生成等业务时，可采用SA-PPG评估模型真实能力，避免基准数据污染导致的效果误判

  - 部署生成类LLM服务时可复用RailCap解码思路，生成过程中动态抑制记忆内容输出，提升文案原创性，避免输出训练数据中的雷同内容

  - 做业务效果评估时可复用分层逐题差量聚合的统计思路，避免平均指标掩盖局部偏差，更精准定位模型短板'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
公共基准测试数据常泄露到预训练语料，导致模型评估分数虚高，无法反映真实能力。现有污染缓解评估指标G-AP存在严重缺陷：离散对错标签无法表征逐题表现、平均后做差导致过抑制/欠抑制效果抵消、统一权重易被针对性优化，且现有缓解策略依赖预污染检测，效果受检测精度限制。
### 方法关键点
1. 提出SA-PPG评估指标：采样估计每道题的求解概率，与干净模型逐题做差，按干净模型求解概率分组聚合，消除指标偏差
2. 提出RailCap缓解策略：生成过程中动态判断污染，当采样落回贪心轨迹时，下一个token限制为次优输出，逐步累积抑制直到响应分布足够分散，无需提前检测污染位置
### 关键结果
多模型多基准测试显示，SA-PPG发现原有缓解策略的能力还原效果被大幅高估，RailCap取得最低SA-PPG值，还原效果最优。
