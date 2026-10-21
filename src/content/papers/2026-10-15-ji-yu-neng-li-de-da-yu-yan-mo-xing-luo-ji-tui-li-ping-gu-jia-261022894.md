---
title: Competence-Based Evaluation of Logical Reasoning in Large Language Models
title_zh: 基于能力的大语言模型逻辑推理评估框架
authors:
- Jize Jiang
- Chengxiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.22894'
url: https://arxiv.org/abs/2610.22894
pdf_url: https://arxiv.org/pdf/2610.22894
published: '2026-10-15'
collected: '2026-10-21'
category: Eval
direction: LLM逻辑推理 · 能力评估范式
tags:
- Logical Reasoning
- LLM Evaluation
- Competence Test
- Robustness
- Parameterized Generation
one_liner: 提出能力导向的CBE评估范式，通过参数化生成和等价表述测试LLM逻辑推理的泛化稳定性
practical_value: '- 可复用CBE的等价表述测试方法，验证电商/广告场景下LLM对用户Query改写、Prompt扰动的输出一致性，避免单一场景准确率虚高导致的线上效果不符合预期

  - 搭建业务场景自定义LLM能力评估体系时，可参考参数化问题生成方案，控制问题核心规则不变的前提下扩展测试集规模，有效降低测试集污染风险

  - 微调业务专用LLM时，可借鉴GRPO增加跨等价输入一致性奖励的训练策略，提升模型在同义输入下的输出鲁棒性，泛化效果远优于纯SFT'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM逻辑推理评估仅输出单一准确率，混淆了语言理解、记忆、捷径利用和真实推理能力，无法反映模型的推理泛化性——大量实证显示，同个推理问题仅调整表述形式就可能导致模型结果波动，单场景准确率无法支撑对模型真实推理能力的准确度量。

### 方法关键点
- 能力导向评估（CBE）范式脱离固定测试集的准确率限制，核心测试模型是否能在同规则的问题族中稳定应用同一种推理能力
- 配套参数化问题生成器，固定所需推理能力的前提下可自由缩放问题复杂度，同时生成答案完全一致的等价表述prompt，只有跨所有等价表述均回答正确才判定为能力达标
- 定义R（双表述均正确）、D（双表述均错误）、U（单表述正确）三类拆分指标，输出模型的能力边界轮廓而非单一分数

### 关键实验结果
在基础排序推理任务上测试6款GPT、Qwen模型，对比CoT、LoRA SFT、GRPO等干预方案：
- n=1024的前后排序任务中，GPT-4.1原始prompt准确率77.5%，但跨等价表述双正确率仅56.8%，近1/3结果依赖表述形式
- 启用CoT可将GPT-5.4的跨表述准确率从79.2%提升至96.0%，但n=2048时仍存在明显性能下降
- 带跨表述一致性奖励的GRPO微调可将Qwen3.5-9B的跨表述不变性从60.0%提升至83.5%，远优于纯SFT无明显提升的效果

### 核心结论
单一场景的准确率无法反映模型的真实推理能力，高准确率可能仅对应有限复杂度范围内的局部性能，而非对推理规则的稳定掌握。
