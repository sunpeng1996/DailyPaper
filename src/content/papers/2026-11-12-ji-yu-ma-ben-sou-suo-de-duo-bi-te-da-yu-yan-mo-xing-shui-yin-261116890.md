---
title: 'Look It Up: Multi-bit LLM Watermarking via Codebook Search'
title_zh: 基于码本搜索的多比特大语言模型水印方案
authors:
- Jarosław Janas
- Paweł Morawiecki
- Josef Pieprzyk
affiliations:
- Institute of Computer Science, Polish Academy of Sciences
- CSIRO
arxiv_id: '2611.16890'
url: https://arxiv.org/abs/2611.16890
pdf_url: https://arxiv.org/pdf/2611.16890
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: LLM水印 · 多比特短文本溯源
tags:
- LLM-Watermark
- Codebook-Search
- Multi-bit-Watermark
- Content-Provenance
- Text-Attribution
one_liner: 通过码本映射与距离匹配实现短文本场景下多比特LLM水印的高效嵌入与提取
practical_value: '- 电商生成式商品短文案、Agent客服短回复场景可直接嵌入该水印，解决AI生成违规/侵权内容溯源难的痛点

  - 存在轻度改写的场景（如搜索query改写、营销文案二次优化）优先选用Levenshtein距离匹配码本，提升水印识别率

  - 端侧小模型水印场景可选用无码本存储的BCH变体，大幅降低存储开销，适配端侧资源约束'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多比特LLM水印方案需依赖长生成文本或高成本解码才能可靠恢复载荷，无法适配电商短文案、Agent短回复等短生成文本的内容溯源需求。
### 方法关键点
1. 构建码本映射机制：将n-bit载荷映射为更长的u-bit码字，生成阶段通过token级logit偏置完成水印嵌入，不影响文本生成质量
2. 提取阶段无需复杂解码：将待检测文本提取的比特序列与预计算秘密码本做最近邻匹配，支持Hamming/Levenshtein两种距离度量
3. 提供轻量变体：无需存储码本的BCH编码变体，适配资源受限的部署场景
### 关键结果
200-token生成文本上16-24bit载荷恢复率接近100%，127-token基础模型生成文本上表现优异；指令微调模型短文本场景性能下降，低熵输出会降低嵌入可靠性；Levenshtein变体抗删除、轻度改写能力更强，抗插入、重度改写能力仍不足
