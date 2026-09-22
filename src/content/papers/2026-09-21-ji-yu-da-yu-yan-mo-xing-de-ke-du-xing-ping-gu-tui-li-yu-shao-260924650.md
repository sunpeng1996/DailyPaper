---
title: 'Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting'
title_zh: 基于大语言模型的可读性评估：推理与少样本提示的作用
authors:
- Raphaël Thieffry
- Matej Martinc
affiliations:
- Université Paris-Saclay
- Jožef Stefan Institute
arxiv_id: '2609.24650'
url: https://arxiv.org/abs/2609.24650
pdf_url: https://arxiv.org/pdf/2609.24650
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM任务优化 · 少样本与推理Prompt
tags:
- LLM
- Readability Assessment
- Chain-of-Thought
- Few-shot Learning
- Multilingual
one_liner: 系统评测开源LLM可读性评估能力，验证原生推理与单样例少样本的增益效果
practical_value: '- 做LLM-as-Judge类任务（电商文案质量打分、商品描述可读性分级、用户评论合规判定等）时，优先选用带原生推理能力的小参数开源LLM，效果远优于普通模型加诱导CoT
  prompt，还可降低推理成本

  - 少样本提示无需堆砌样例，每分类仅需1个标注样例即可拿到80%以上的少样本增益，额外增加样例收益边际递减，还会占用上下文窗口增加截断风险

  - 低资源语言/垂直细分领域无标注训练数据时，原生推理LLM+单样例少样本的组合可直接作为无训练基线方案，效果优于传统规则方法，尤其适合规则不适用的复杂场景

  - 分类任务的prompt中必须明确给出分级定义与评价标准，实测去掉定义会导致Spearman相关性下降0.1以上，XML结构化prompt效果略优于纯文本prompt'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统可读性评估公式跨领域、跨语言泛化能力差，监督模型依赖稀缺的领域标注数据，低资源语言几乎没有可用的评估工具；现有LLM可读性评估研究未系统探索推理机制与少样本策略的实际增益，无法支撑工业落地选择。
### 方法关键点
- 评测5款开源LLM（参数9B~30B，覆盖英语专属到多语言支持），跨4个数据集（3个英文通用数据集、1个低资源斯洛文尼亚语教材数据集）开展离散可读性等级分类任务
- 对比4种输出模式：直接回答、诱导推理、原生推理、两阶段推理，统一用vLLM约束输出格式避免解析错误，所有模型全程冻结无微调
- 测试0~3shot少样本设置，控制样例选择变量对齐不同模型的评测条件
### 关键结果数字
- 原生推理模式比直接回答平均提升Spearman ρ 0.136、加权Kappa 0.186，诱导推理和两阶段推理几乎无增益甚至出现负向效果
- 1shot（每类1个标注样例）设置比0shot平均提升ρ 0.043，再增加样例ρ基本持平，仅F1微涨
- 最优配置（Qwen3.5-9B+原生推理+1shot）在斯洛文尼亚语数据集上ρ达0.753，比传统公式最高值高0.311，接近监督模型效果
### 核心结论
无训练的LLM分类任务最优策略是选择原生推理小模型+每类1个标注样例，增益集中在传统规则最弱的低资源/垂直场景
