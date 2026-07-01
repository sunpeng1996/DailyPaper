---
title: Robust Text Watermarking for Large Language Models via Dual Semantic Embeddings
title_zh: 基于双语义嵌入的大语言模型鲁棒文本水印方法
authors:
- Jonas Schäfer
- Cezary Pilaszewicz
- Gerhard Wunder
affiliations:
- Freie Universität Berlin, Department of Mathematics and Computer Science
arxiv_id: '2606.31602'
url: https://arxiv.org/abs/2606.31602
pdf_url: https://arxiv.org/pdf/2606.31602
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 大语言模型 · 鲁棒文本水印
tags:
- LLM
- Text Watermark
- Semantic Embedding
- Content Attribution
- Robustness
one_liner: 提出双嵌入水印DEW方案，实现抗改写、翻译且不影响文本质量的LLM生成内容隐水印
practical_value: '- 电商场景下LLM生成的商品文案、营销话术、Agent客服回复可嵌入DEW水印，实现内容溯源，防范竞品爬取盗用生成内容

  - 生成式推荐的个性化解释文案、种草类生成内容可植入DEW，解决内容侵权、不实传播后的责任溯源问题

  - 伪随机矩阵+密钥的水印混淆方案可直接复用，无需修改LLM原生生成逻辑，工程落地成本低'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM表层文本水印易被 paraphrasing、翻译等语义变换操作抹除，无法实现生成内容的可靠溯源与版权防护，无法满足负责任AI落地要求。
### 方法关键点
1. 提出Dual-Embedding Watermarking (DEW)语义水印框架，同时利用token-level embedding与上下文embedding，通过向量空间代数运算生成水印信号，语义偏移下水印呈现平缓衰减特性；
2. 采用密钥生成的伪随机矩阵投影嵌入向量实现水印混淆，具备抗破解能力；
3. 基于代数推导的统计分布实现水印检测，无需额外训练辅助模型。
### 关键结果
跨多LLM测试，改写后水印检测率显著优于传统语义水印，翻译后仍可稳定检测；生成文本质量与无水印基线持平，无用户可感知的质量下降。
