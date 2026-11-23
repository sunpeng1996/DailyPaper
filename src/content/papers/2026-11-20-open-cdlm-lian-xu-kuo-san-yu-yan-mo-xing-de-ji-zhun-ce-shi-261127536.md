---
title: 'Open CDLM: A Benchmark and Library for Continuous Diffusion Language Models'
title_zh: Open CDLM：连续扩散语言模型的基准测试与开源库
authors:
- Hao Jiang
- Ruixi Chen
- Jiayi Han
- Yulei Sun
- Yujian Chen
- Gen Li
- Brian. K Chen
- Guang Cheng
- Weijian Luo
- Tianyang Hu
affiliations:
- Polyadic Research Group
- SAGA Lab, The Chinese University of Hong Kong, Shenzhen
- Peking University
- National University of Singapore
- Xiaohongshu
arxiv_id: '2611.27536'
url: https://arxiv.org/abs/2611.27536
pdf_url: https://arxiv.org/pdf/2611.27536
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 扩散语言模型 · 评估基准建设
tags:
- Continuous Diffusion Language Model
- Evaluation Benchmark
- Open-source Library
- Kernel Text Discrepancy
- Text Generation
one_liner: 推出开源基准Open CDLM及配套库，解决连续扩散语言模型现有评估偏差问题
practical_value: '- 生成式推荐/广告文案生成场景下，可复用KTD指标替代传统困惑度/熵，检测生成内容的模式崩溃问题，避免大量重复内容输出

  - 自研扩散类LLM生成器时，可直接复用Open CDLM的评估框架，快速完成模型拟合度、生成多样性/覆盖率的统一测评，减少重复开发

  - 业务侧做生成模型A/B测试时，可参考文中对困惑度上界的局限性分析，避免仅用单一指标得出错误的模型优劣结论'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
连续扩散语言模型（CDLM）现有评估方案存在严重偏差：基于似然的评估依赖变分上界，其松弛度会干扰模型对比；基于生成样本的传统指标（困惑度、unigram熵）无法检测生成模式崩溃，即便每次输出完全相同文本仍能得到高分。

### 方法关键点
推出开源评估基准Open CDLM及配套库：1. 似然评估侧明确困惑度上界的适用场景与评估流程对结论的影响；2. 样本评估侧引入Kernel Text Discrepancy（KTD）对比生成与真实文本分布，同时新增多样性、有效性、覆盖率诊断维度。

### 关键结果
OpenWebText受控实验显示，用单条文本副本替换整个生成集合时，传统生成指标反而提升，仅MAUVE可检测到该崩溃问题，其对其他扰动的响应依赖文本表示与扰动类型。
