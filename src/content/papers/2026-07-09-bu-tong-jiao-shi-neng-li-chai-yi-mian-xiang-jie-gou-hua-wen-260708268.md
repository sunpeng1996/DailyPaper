---
title: 'Different Teachers, Different Capabilities: Sub-1B On-Device Distillation
  for Structured Text Enrichment'
title_zh: 不同教师能力差异：面向结构化文本增强的1B以下端侧蒸馏
authors:
- Vinay Kumar Chaganti
affiliations:
- Independent Researcher
arxiv_id: '2607.08268'
url: https://arxiv.org/abs/2607.08268
pdf_url: https://arxiv.org/pdf/2607.08268
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 端侧小模型蒸馏 · 结构化文本增强
tags:
- Knowledge-Distillation
- On-Device-LLM
- Small-Language-Model
- Structured-Generation
- LLM-Evaluation
one_liner: 通过对比三类教师的0.6B端侧蒸馏效果，给出结构化文本增强任务的分字段最优引擎路由方案
practical_value: '- 做端侧结构化提取（如商品标签生成、详情摘要）时，优先选推理型LLM做教师蒸馏，能比同规模非推理教师多拿近20个点的生成质量提升，无需盲目堆教师参数量

  - 类别不均衡的分类/标签任务，蒸馏小模型效果大概率打不过few-shot prompting，可直接用few-shot代替蒸馏节省训练成本，尤其适合商品风格、情感标签这类偏主观的标注任务

  - 蒸馏小模型的多seed一致性可作为低开销置信度信号：3个seed输出一致的标签准确率比不一致的高20+点，不一致结果直接路由给大模型fallback，用极低开销提升整体准确性

  - 做LLM生成的faithfulness评估时必须用全文本输入，只用截断的前N字符会产生虚假的幻觉率波动结论，该评估坑需避开'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
高流量结构化文本提取（如商品标签生成、内容摘要、工单分类）调用大模型的latency和成本极高，端侧小模型速度快40倍但质量不足，现有蒸馏研究多输出单一聚合指标，未拆分不同子任务的能力差异，也未对比few-shot、约束解码等低成本落地方案，结论无法直接复用。

### 方法关键点
- 教师分三类：8B推理型DeepSeek-R1、同规模非推理型Llama-3.1-8B-Instruct、120B带合成数据增强的商业管线
- 学生统一用0.6B Qwen3，QLoRA蒸馏（rank=32，response-only损失），跑3个种子消除随机波动
- 评估采用跨模型家族三法官盲评，拆分摘要生成、5类分类标签子任务单独打分，所有模型采用部署态4bit量化实测性能

### 关键结果
在494篇新闻构成的RSS-News数据集上测试，蒸馏后0.6B模型单条推理仅0.8s，比8B教师的39s快近50倍；摘要质量追回基模型到教师gap的58%，比约束解码高16.8分，比few-shot高4.9分；分类任务整体效果不如few-shot，仅urgency、frame两类标签有明显提升；推理型教师的蒸馏学生摘要质量更高，但1200字符以下短文本幻觉率比非推理教师学生高19pct。

最值得记住的结论：不要用单一聚合指标评判蒸馏效果，拆分不同子任务的能力差异做分字段路由，才是端侧小模型落地的最优解，无需追求小模型在全任务上超过大模型
