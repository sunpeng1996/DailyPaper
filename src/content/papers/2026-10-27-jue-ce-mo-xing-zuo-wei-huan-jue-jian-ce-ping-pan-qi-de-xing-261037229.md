---
title: Decision Models as Judges for Hallucination Detection
title_zh: 决策模型作为幻觉检测评判器的性能与成本验证
authors:
- Haozheng Liu
- Zhaoqian Xue
- Zhongyin Wang
- Junting Mu
- Zihui Ma
- Shuya Feng
- Lingyao Li
affiliations:
- New York University
- University of Arizona
- University of Illinois Urbana-Champaign
- University of California, Irvine
- Emory University
arxiv_id: '2610.37229'
url: https://arxiv.org/abs/2610.37229
pdf_url: https://arxiv.org/pdf/2610.37229
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: LLM 幻觉检测 · 低成本评判方案优化
tags:
- Hallucination Detection
- LLM-as-a-Judge
- Decision Model
- Cascade Inference
- Cost Optimization
one_liner: 验证决策模型可作为低成本幻觉检测评判器，级联方案性能匹敌GPT-6-sol且成本仅为其1-3%
practical_value: '- 电商Agent/生成式推荐的文案幻觉检测场景，可优先用决策模型替代GPT类大模型做上下文不一致、事实错误类检测，成本可降97%以上

  - 可复用置信度级联推理架构：先让高置信度决策模型输出结果，低置信度case再转给大模型，平衡成本与检测准确率

  - 决策模型在逻辑、指令一致性类幻觉检测上性能较差，这类场景仍需保留大模型评判链路，不要盲目替换'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM-as-a-Judge方案推理成本高、自身存在幻觉与过置信问题，亟需低成本高可靠的替代评判方案，决策模型（输出固定标签+置信度、推理更快更便宜）是潜在方向但缺乏系统性验证。
### 方法关键点
构建覆盖5类幻觉、共9852条样本的二分类检测基准，对比5种决策模型与gpt-6-sol的幻觉检测性能，同时验证决策模型置信度级联架构的优化效果。
### 关键结果数字
1. 最优决策模型在上下文不一致类检测上平衡准确率与gpt-6-sol持平，事实错误类检测仅低3pp，逻辑/指令不一致类低4-8pp；
2. 决策模型过置信程度显著低于GPT-6系列模型；
3. 置信度级联方案较单最优决策模型准确率提升1.9-3.3pp，性能匹敌甚至超过gpt-6-sol，成本仅为其1-3%。
