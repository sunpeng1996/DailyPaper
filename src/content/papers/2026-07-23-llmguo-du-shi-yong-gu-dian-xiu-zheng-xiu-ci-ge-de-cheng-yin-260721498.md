---
title: 'Artificial Epanorthosis: Why large language models overuse a classical rhetorical
  figure, and how to mitigate it'
title_zh: LLM过度使用古典修正修辞格的成因分析与缓解方案
authors:
- Federico Boggia
affiliations:
- University of Pisa
arxiv_id: '2607.21498'
url: https://arxiv.org/abs/2607.21498
pdf_url: https://arxiv.org/pdf/2607.21498
published: '2026-07-23'
collected: '2026-07-25'
category: LLM
direction: LLM生成风格校准 · 轻量适配
tags:
- LLM
- LoRA
- controllable generation
- RLHF
- style calibration
one_liner: 定位LLM过度使用修正修辞格的成因，提出从prompt到LoRA的多粒度校准方案
practical_value: '- 电商商品文案、营销话术生成场景可复用该思路，用LoRA适配+强度系数α，快速校准话术的夸张/平实程度，适配不同平台、客群的风格要求

  - 可直接复用单条prompt引导的轻量方案，无需训练即可降低LLM生成营销文案时的过度「鸡汤化」问题，实测可降低50%-75%的冗余修辞

  - 多级别风格控制栈（prompt→best-of-n→rewrite→LoRA）可直接迁移到Agent的回复生成场景，按需切换不同交互场景的话术风格，避免生硬套话'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM生成文本普遍过度使用epanorthosis（先否定原表述再升级为更夸张表达的古典修辞格，如「我们不卖产品，我们打造体验」），这类套话会降低文本可信度，尤其在电商文案、客服回复场景容易引发用户反感；现有研究未明确该现象的成因，也缺乏低成本的缓解方案，且过度抑制会破坏合法的内容修正功能。

### 方法关键点
- 定义Epanorthosis Index（EI），以不同体裁的人类文本修辞密度为基线，量化LLM的修辞偏离程度，EI>1为过度使用，<1为使用不足，优化目标为对齐人类基线而非完全消除该修辞
- 设计梯度化缓解技术栈，从轻量到重度分别为：单条引导prompt、best-of-n候选筛选、后处理重写、SFT训练的轻量LoRA风格适配器，支持通过缩放系数α连续调节修辞抑制强度
- 明确该现象的核心成因为训练数据中营销文案占比过高、RLHF偏好奖励自信夸张的表达，自回归生成逻辑仅为放大因素而非根本原因

### 关键实验结果
- 对Claude系列模型的测试显示，其在演讲类文本中EI达2.2（超人类2倍，意大利语下接近3倍），在非正式问答场景EI仅0.2（仅为人类的1/5）
- 单条引导prompt即可将意大利语演讲、议论文本的该修辞密度降低70%-72%，效果显著
- 基于Qwen2.5-7B训练的LoRA适配器，调节α到0.75即可将议论文的修辞密度校准到人类基线水平，最大可降低98%的冗余修辞

**最值得记住的一句话**：LLM生成风格优化的目标是对齐人类在对应场景的行为基线，而非追求单一指标的归零，轻量适配方案完全可以实现细粒度的风格控制。
