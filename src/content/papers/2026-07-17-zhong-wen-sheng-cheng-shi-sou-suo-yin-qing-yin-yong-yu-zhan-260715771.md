---
title: What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale
  Empirical Study
title_zh: 中文生成式搜索引擎引用与展示机制大规模实证研究
authors:
- Tao Zhen
- Yue Liu
- Gege Zhang
- Yixuan Niu
affiliations:
- Aidso Wendao Research Institute
- Beijing Aichacha Technology Co., Ltd.
arxiv_id: '2607.15771'
url: https://arxiv.org/abs/2607.15771
pdf_url: https://arxiv.org/pdf/2607.15771
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: 生成式搜索引擎行为实证评估
tags:
- Generative Search
- Citation Analysis
- Empirical Study
- Search Evaluation
- Chinese LLM
one_liner: 对四大主流中文生成式搜索平台开展大规模实证，揭示引用选择、品牌曝光、跨端一致性等核心规律
practical_value: '- 做生成式搜索优化（GEO）可重点提升内容匹配度、跨源出现频次、语义角色契合度，无需过度依赖传统搜索质量分

  - 高时效性品类（生鲜、促销等）内容曝光半衰期仅39天，需每30天左右更新推广物料；低时效性品类可按2个月维度迭代

  - 同平台App与Web端引用源存在系统性差异，品牌投放、内容布局需针对两端分别优化

  - 13%品牌曝光无对应引用池匹配，可尝试适配大模型偏好的无引用触发式品牌露出玩法'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
生成式QA系统正逐步替代传统排序搜索成为核心信息入口，其引用选择、内容展示规则尚不透明，缺乏针对中文生态的大规模实证分析，无法支撑GEO（生成式搜索引擎优化）等业务落地。
### 方法关键点
覆盖4个主流中文生成式搜索平台的8个Web/App接口，采集614条查询、每查询-平台-接口组合3次重复的共21.4万条原始记录，清洗得到16.1万条引用级数据集，分析引用行为、来源归因、实体曝光、跨接口一致性。
### 关键结果数字
品牌整体选择率8.3%，含联系方式的检索源仅12.4%会透出联系方式；高时效性查询引用半衰期39天，低时效性为68天；13%品牌曝光、71%联系方式曝光无法匹配到对应检索源；同平台App与Web端引用源存在系统性差异。
