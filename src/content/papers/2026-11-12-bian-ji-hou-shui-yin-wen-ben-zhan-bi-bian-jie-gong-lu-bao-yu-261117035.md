---
title: 'Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration
  Sensitivity'
title_zh: 编辑后水印文本占比边界：功率包络与校准敏感性
authors:
- Kuancheng Ye
affiliations:
- University of California, Irvine
- Donald Bren School of Information and Computer Sciences, UCI
arxiv_id: '2611.17035'
url: https://arxiv.org/abs/2611.17035
pdf_url: https://arxiv.org/pdf/2611.17035
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: LLM水印检测 · 语料级占比估算
tags:
- LLM Watermark
- Statistical Bound
- Corpus Audit
- Detection Calibration
one_liner: 推导未知编辑量下两类LLM水印的语料占比边界与校准方案
practical_value: '- 电商生成式文案（商品描述、直播间话术）审计可复用该语料级水印占比估算方法，批量统计AI生成内容占比，规避合规风险

  - Agent生成用户回复/推荐文案时，可参考三类编辑预算（留存下限、熵预算、替换预算）的设定逻辑，在不破坏水印的前提下优化文案自然度

  - 大流量场景下的生成内容审计优先使用独立人工样本校准的零假设，避免10万级以上样本量下检测覆盖率失效'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM水印检测仅支持单文档是否含水印的二分类判断，缺乏语料级水印文本占比的量化方法，且无法应对文档被未知程度编辑的审计场景。
### 方法关键点
结合最不利next-token分布与序列耦合，推导以留存下限、熵预算、原位替换预算三类指标为索引的功率包络，支持精确零假设/独立人工样本校准零假设两种模式，可输出固定语料的有限样本边界与流数据置信序列。
### 关键结果数字
模拟场景下最优阈值精度与12组阈值组合相当；水印占比为0.2时精确零假设边界约为[0.14, 0.38]；2000文档量下0.01的零假设误差无影响，10万文档量下需独立人工样本校准维持检测覆盖率。
