---
title: Can Open-Weight Models Compete on Financial Text Comprehension?
title_zh: 开源权重大模型能否在金融文本理解任务上比肩闭源模型
authors:
- Jan Spörer
affiliations:
- University of St. Gallen, Switzerland
arxiv_id: '2608.08634'
url: https://arxiv.org/abs/2608.08634
pdf_url: https://arxiv.org/pdf/2608.08634
published: '2026-08-09'
collected: '2026-08-11'
category: Eval
direction: 大模型评测 · 金融领域文本理解
tags:
- LLM
- Evaluation
- Financial NLP
- Open-weight Model
- Hallucination
one_liner: 更新金融文本理解基准并测试20款大模型，验证开源非推理模型可达到顶尖金融理解性能
practical_value: '- 垂类LLM选型不必盲目迷信闭源/带推理架构模型，可优先测试开源非推理模型的成本收益比，适配电商客服、交易文本理解等场景

  - 垂类RAG系统失败瓶颈近半来自检索环节，可优先优化检索模块准确率，降低后续大模型错误率

  - 自研垂类评测基准可参考「私有直到发布」的设计思路，避免训练集污染导致评测结果失真'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有开源大模型在通用基准上追平闭源模型，但在真实金融文本理解任务上的可靠性缺乏实测，且传统公开基准易被训练集污染，评测结果可信度不足

### 方法关键点
更新Financial Touchstone基准，包含来自495份国际年报的2967条问答三元组，采用发布前私有策略避免污染，覆盖10家厂商的20款大模型（含开源GLM4.7/5、Kimi K2.6、DeepSeek V3.2及闭源Qwen3-Max、Claude Opus等）

### 关键结果数字
1. Claude Opus 4.6准确率最高（88.4%），Gemini 2.5 Pro幻觉率最低（0.08%）
2. 开源Kimi K2.6准确率排第三，非推理开源模型GLM5、Mistral3分列四五，打破「推理架构/闭源是强金融理解能力前提」的认知
3. 检索是核心瓶颈，占所有失败案例的48.9%
4. 国产大模型地缘内容过滤会拒绝0.08%的合法金融问题，拒绝行为与访问路径强相关
