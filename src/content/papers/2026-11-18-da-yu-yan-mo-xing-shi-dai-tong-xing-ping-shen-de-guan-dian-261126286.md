---
title: 'Twice-Told Critiques: Claim-Level Homogenization of Peer Review in the LLM
  Era'
title_zh: 大语言模型时代同行评审的观点层面同质化问题研究
authors:
- Ilya Gusev
affiliations:
- Keenable
- Amsterdam
arxiv_id: '2611.26286'
url: https://arxiv.org/abs/2611.26286
pdf_url: https://arxiv.org/pdf/2611.26286
published: '2026-11-18'
collected: '2026-11-21'
category: LLM
direction: LLM应用影响 · 内容同质化分析
tags:
- LLM
- Peer Review
- Content Homogenization
- Text Detection
- Empirical Study
one_liner: 实证发现LLM普及后顶会与期刊同行评审意见重叠度上升，LLM生成评审多样性更低
practical_value: '- 业务中使用LLM生成用户评价、商品评论、客服话术时，需提前评估同质化风险，避免内容趋同降低用户信任度

  - 可复用论文中Claim-Level的相似度计算方法，用于检测UGC/PGC内容、推荐理由、广告文案的同质化程度，支撑内容生态治理

  - 用LLM辅助生成推荐理由、商品卖点、广告文案时，可引入多样性约束模块，避免不同商品/场景的输出趋同，提升内容转化率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
同行评审核心依赖不同评审人输出差异化意见，LLM普及后大量评审借助LLM生成，其意见多样性变化尚无量化实证结论。
### 方法关键点
采用观点级（Claim-Level）相似度计算而非整段文本匹配，精准度量评审批评意见的重叠度；使用MELD LLM生成文本检测器区分人工与LLM生成的评审，对比两类内容的重叠度差异。
### 关键结果
ICLR 2026-2027年同阶段评审重叠度从12.0%升至21.3%，单篇第三份评审新增问题从6.12个降至5.46个；LLM标记的评审重叠度比人工评审高3.0~5.4个百分点，NeurIPS、ICML及F1000、PLOS等多个期刊均观测到评审同质化逐年上升趋势。
