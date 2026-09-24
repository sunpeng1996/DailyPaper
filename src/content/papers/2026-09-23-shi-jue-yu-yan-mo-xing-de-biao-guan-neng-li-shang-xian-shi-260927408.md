---
title: What Looks Like a Capability Limit in Vision-Language Models Is a Readout Limit
title_zh: 视觉语言模型的表观能力上限实际源于输出读取范式限制
authors:
- Alfredo F. Frontera Del Valle
affiliations:
- Columbia University
arxiv_id: '2609.27408'
url: https://arxiv.org/abs/2609.27408
pdf_url: https://arxiv.org/pdf/2609.27408
published: '2026-09-23'
collected: '2026-09-24'
category: Eval
direction: 多模态大模型 · 基准评估偏差
tags:
- Vision-Language Model
- Benchmark Evaluation
- Output Convention
- Evaluation Bias
- Multimodal LLM
one_liner: 发现多模态基准的答案输出范式会显著影响模型得分，而非模型本身能力不足
practical_value: '- 做多模态商品理解、多模态Agent评测时，需对齐所有参评模型的答案输出范式，避免将输出习惯不匹配的模型误判为能力不足

  - 业务需多模态模型输出坐标、色值等结构化数值时，优先用LoRA做少量样本微调适配目标输出范式，不要直接调用通用模型，避免准确率暴跌

  - 多模态召回、商品属性打标场景下，优先用自然语言类语义标签对接模型，而非原生数值格式（像素坐标、色相角等），可大幅提升任务准确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态基准默认答案输出范式是中立的，得分直接等价于模型本身能力，该假设从未被验证，大量模型能力误判可能源于此。
### 方法关键点
在物体定位、颜色识别两类典型多模态任务上，对比同一模型在不同答案输出范式（自然语言描述、像素坐标、色相角等）下的得分差异；通过给不同输出范式绑定错误标签的方式，验证模型对各类范式的实际识别能力。
### 关键结果数字
1. Qwen3-VL-4B物体定位任务中，英文位置描述下准确率68.5%，像素坐标下仅20%（随机准确率11.1%）
2. 原本性能持平的模型在不同输出范式下得分差最高达54分，甚至出现排名反转
3. 除GPT-4o外，Gemini及多数开源多模态模型均存在输出范式惩罚，色相角类数值范式的识别率甚至低于随机水平
