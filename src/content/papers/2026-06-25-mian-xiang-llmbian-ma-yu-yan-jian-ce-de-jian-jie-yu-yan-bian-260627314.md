---
title: 'Beyond Surface Forms: A Comprehensive, Mechanism-Oriented Taxonomy of Indirect
  Linguistic Encoding for LLM-Based Coded Language Detection'
title_zh: 面向LLM编码语言检测的间接语言编码机制导向综合分类法
authors:
- Hamid Reza Firoozfar
- Mohammadsadegh Abolhasani
- Reza Mousavi
- Paul Jen-Hwa Hu
affiliations:
- The University of Utah
- The University of Virginia
arxiv_id: '2606.27314'
url: https://arxiv.org/abs/2606.27314
pdf_url: https://arxiv.org/pdf/2606.27314
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM内容安全 · 编码语言检测
tags:
- Coded Language Detection
- Indirect Linguistic Encoding
- LLM Prompting
- Content Moderation
- Taxonomy
one_liner: 基于底层编码机制的ILE分类法，融入LLM prompt可显著提升编码语言检测效果
practical_value: '- 电商内容审核（商品文案/评论/直播话术）可借鉴机制导向分类思路，梳理违规内容的常见编码逻辑（谐音、代指、拆字、暗语等）形成分类体系注入LLM
  prompt，替代纯词库方案，降低新型规避词漏检率

  - 针对不断迭代的规避式表达，基于编码机制分类构建检测框架，无需频繁更新词表，可大幅降低内容安全运营的维护成本

  - 落地LLM文本分类/检测类任务时，可将底层机制分类作为prompt的结构化脚手架，相比表层标签分类或few-shot示例能进一步提升准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
社交媒体用户为规避算法审核、影子封禁、限流等，大量使用间接语言表达（ILE，如algospeak、委婉语、对抗性混淆）传递敏感含义。这类表达迭代极快，基于表层词表或历史样本训练的检测器通常数周内就会失效，现有ILE分类多围绕沟通目标划分，难以支撑对新型编码表达的泛化检测。

### 方法关键点
机制导向的ILE综合分类法跳出表层沟通目的的限制，从意义编码与解码的底层操作逻辑维度对间接表达进行归类；将该分类体系作为结构化脚手架融入LLM prompt，用于编码语言检测任务。

### 关键结果
基于2000条人工标注的TikTok、Bluesky帖子，在3个LLM上与4种现有分类法、无分类基线对比：
- 文档级、span级检测性能均达最优，相比最佳基准准确率提升4.7%，F1提升5.4%
- 验证了机制导向分类是检测新兴编码语言的稳定支架，可有效支撑内容审核工作
