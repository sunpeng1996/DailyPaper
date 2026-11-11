---
title: 'Multimodal Judges Flag, Humans Decide: A Review-and-Edit Framework for AI-Generated
  Product Video Ads'
title_zh: AI生成商品视频广告的人机协同审核编辑框架
authors:
- Anoubhav Agarwaal
- Sukesh Perla
- Karthikeyan Mohanraj
- Susmita Ghose
affiliations:
- Anoki Inc.
arxiv_id: '2611.13178'
url: https://arxiv.org/abs/2611.13178
pdf_url: https://arxiv.org/pdf/2611.13178
published: '2026-11-09'
collected: '2026-11-11'
category: GenRec
direction: 生成式广告 · 人机协同审核编辑
tags:
- Multimodal LLM
- Generative Ad
- Human-in-the-loop
- Video Ad
- E-commerce
- Content Audit
one_liner: 提出多模态AI初审+人工复核的商品视频广告审核编辑框架，适配电商规模化生成
practical_value: '- 可直接复用6维分层审核维度：商品、场景质量、发音、脚本、音效、字幕，每个维度对应最小修复单元，避免全量重生成，降低生成内容返工成本

  - AI审核模型优先调优recall而非precision：漏检违规内容的成本远高于误判的人工审核成本，可复制到所有生成式广告内容的风控链路

  - 局部修复的工程实践：仅修改有问题的视频片段、脚本行、字幕，其余合格内容完全保留，比全量重生成效率提升至少50%，可直接落地到图文/短视频生成管线

  - 人机协同标注提效方案：AI预打标可使人工审核注意力保持稳定，不会随工作时长下降，标注量提升2倍以上，可复用在内容标注平台'
score: 9
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前生成式管线已可将电商商品页批量转化为短视频广告，但纯人工审核漏检率高、注意力随工作时长衰减，纯AI审核精度不足，且粗粒度的「合格/不合格」判定会浪费大量可通过局部修复复用的内容，无法适配电商百万级商品的规模化生成需求。
### 方法关键点
- 设计6维度分场景审核规则：每个维度对应最小问题单元（场景/脚本行/字幕/全广告），AI法官与审核员共用同一套规则，问题可直接映射到对应修复工具
- 人机协同审核链路：多模态AI法官（视觉语言/语音/文本模型）预标注问题，人工仅需对标注结果点选接受/驳回，同时补充AI漏检问题
- 局部修复机制：仅修改问题对应的最小单元，其余内容完全保留，修复后重新进入审核链路
- 所有AI法官优先优化召回率，避免漏检高风险的商品不符、虚假宣传问题，误判由人工修正
### 关键结果
基于120条生成广告（共562个场景，含120个盲标注场景）测试：
1. 有AI辅助时人工标注的商品问题率达60%，是纯人工的2.3倍，且审核员注意力不会随工作时长衰减
2. 自研多模态产品审核模型AUC达0.84，通用视频质量、图片相似度等baseline仅0.48~0.57
3. 局部修复工具对乱码商品文字的修复成功率达69%（18/26）
### 核心记忆点
在生成式电商内容的规模化落地中，高召回AI初审+最小单元局部修复的人机协同模式，ROI远高于纯AI或纯人工审核
