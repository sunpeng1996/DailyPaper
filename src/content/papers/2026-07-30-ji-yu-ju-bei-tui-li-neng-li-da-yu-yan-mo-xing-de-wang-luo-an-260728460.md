---
title: Cybersecurity Detection Classification with Reasoning-enabled Language Models
title_zh: 基于具备推理能力大语言模型的网络安全检测分类
authors:
- Amol Khanna
- Manu Nandan
- Cristian Viorel Popa
- Joan Pujol-Roig
- Diana Bolocan
- Laura Vasilie
- Alexandru Apostu
- Chase Helwig
- Mihaela Gaman
- Michael Brautbar
affiliations:
- CrowdStrike
arxiv_id: '2607.28460'
url: https://arxiv.org/abs/2607.28460
pdf_url: https://arxiv.org/pdf/2607.28460
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: 大语言模型推理与分类校准
tags:
- Chain-of-Thought
- Reinforcement Learning
- Self-training
- Prompt Optimization
- Classifier Calibration
one_liner: 结合自动prompt优化、自训练与可验证奖励RL训练CoT安全分类器，新增校准器解决CoT引发的标签概率退化问题
practical_value: '- 面向内容审核、广告合规校验、恶意订单识别等分类任务，引入CoT推理时可新增独立校准器读取推理链输出置信度，解决CoT导致的标签概率退化问题，提升高置信度场景召回

  - 垂直领域分类任务可优先选择中等规模模型做针对性微调，复用自动prompt优化+自训练+可验证奖励RL的微调范式，性价比优于直接调用通用大模型

  - 高可靠性要求的自动化决策场景可复用「CoT输出推理过程+校准器判断置信度」架构，仅高置信结果走自动处理，低置信转人工，降低业务误判损失'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
SOC面临严重告警疲劳，人工无法处理海量检测结果，现有直接输出标签的LLM分类方案未引入推理过程，误判率高无法满足自动化分诊要求。
### 方法关键点
1. 基于真实人工标注的Windows终端检测数据，结合自动prompt优化、自训练、带可验证奖励的强化学习，训练带CoT推理能力的分诊分类器；
2. 针对CoT推理导致自动化分类依赖的标签token概率退化问题，单独训练校准器读取完整推理链路，估计判决结果的正确概率。
### 关键结果
系统测试准确率达82.6%；在自动化分诊对应的高置信度工作点上，较直接输出标签的LLM分类器，良性召回提升43.0%，恶意召回提升18.3%；未训练的置信度判断会导致高置信度召回归零，30B参数微调模型效果显著优于前沿通用大模型。
