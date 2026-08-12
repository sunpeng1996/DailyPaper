---
title: 'V-FiLLM: Verified Financial LLM Reasoning Benchmark'
title_zh: V-FiLLM：可验证的金融大语言模型推理基准
authors:
- Alicia Larsen
- Victoire Laurent
- Aulia Kharis Rakhamsari
- Lara Turgut
- Nino Antulov-Fantulin
affiliations:
- ETH Zürich
- Aisot Technologies Ltd
arxiv_id: '2608.11047'
url: https://arxiv.org/abs/2608.11047
pdf_url: https://arxiv.org/pdf/2608.11047
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 大语言模型评估 · 金融推理基准
tags:
- LLM Benchmark
- Financial Reasoning
- LoRA
- Table QA
- Reasoning Evaluation
one_liner: 提出基于真实表格可执行计算树的无标注金融LLM推理基准，验证LoRA微调增益
practical_value: '- 垂直领域推理能力评估可复用「可执行计算树自动生成标注样本」思路，省去人工标注成本，还可自定义难度维度，适用于电商营销计算、订单对账类Agent推理评估场景

  - 垂直领域LLM推理优化可尝试用已验证的Chain-of-Thought轨迹做轻量LoRA微调，成本低增益明显，可适配电商满减规则推理、折扣核算等场景

  - 结构化表格类QA系统需针对性优化数值鲁棒性，避免微小数值扰动导致推理结果失效，可用于电商库存统计、价格核算类Agent开发'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有STEM领域LLM评估基准成熟度高，但面向结构化数据的金融推理评估覆盖不足，人工标注成本高、错误率难控，且无法灵活调节评估难度维度。
### 方法关键点
提出V-FiLLM框架，基于真实金融表格生成可执行计算树，通过符号计算自动生成ground truth，再渲染为自然语言问题，全程无人工标注、无模型参与标注流程，可无限量生成样本；内置计算深度、表达式广度、金融概念复杂度、上下文大小4个可独立控制的难度调节维度。
### 关键结果
开源模型在V-FiLLM上的推理准确率随推理深度提升最高下降51%，遭遇对抗数值扰动时准确率最高下降47个百分点；基于验证过的思维链轨迹做轻量LoRA微调，在留存问题上准确率从81.1%提升至85.6%，在FinQA数据集上较基线模型提升5个百分点。
