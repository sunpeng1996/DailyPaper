---
title: Translating Natural Language to Strategic Temporal Specifications via LLMs
title_zh: 基于大语言模型的自然语言到策略时序规范转换方法
authors:
- Marco Aruta
- Francesco Improta
- Vadim Malvone
- Aniello Murano
- Vladana Perlic
affiliations:
- University of Naples Federico II
- LTCI, Télécom Paris, Institut Polytechnique de Paris
arxiv_id: '2606.30441'
url: https://arxiv.org/abs/2606.30441
pdf_url: https://arxiv.org/pdf/2606.30441
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体系统 · 自然语言转时序规范
tags:
- Multi-Agent System
- LLM Fine-tuning
- Formal Specification
- Temporal Logic
- LLM Judge
one_liner: 小参数量开源LLM微调框架，将自然语言多智能体策略需求转为ATL/ATL*规范，性能追平闭源few-shot方案
practical_value: '- 垂直域规则/规范转换类任务可优先用3-7B小参数开源模型微调，效果可追平闭源大模型few-shot能力，大幅降低成本并支持本地化部署

  - 做LLM生成效果评测时优先选择Llama-3.3-70B这类对齐人类标注的开源大模型作为judge，可避免强闭源模型过拒问题，降低评测偏差

  - 无公开标注数据集的垂直域任务，自行构建小批量专家校验数据集做微调，即可支撑结构化输出类转换需求'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
多智能体系统（MAS）验证需严格的策略时序规范，手动编写规范门槛高、易出错，当前无成熟的自然语言转MAS规范方法，且无对应训练数据集。
### 方法关键点
1. 构建专家校验的NL转ATL/ATL*规范数据集，用于微调开源小参数LLM；2. 对比微调小模型与闭源模型few-shot效果，采用LLM judge结合专家标注做效果评估。
### 关键结果数字
3-7B参数开源模型微调后语义准确率达0.84，与闭源few-shot baseline的0.86统计上无显著差异；LLM judge可靠性与生成器强度负相关，Llama-3.3-70B最贴合人类标注，强闭源模型易过度拒判正确输出
