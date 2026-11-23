---
title: Evaluating Prompting Strategies for Zero-Shot Multilingual Aspect-Based Sentiment
  Analysis with Large Language Models
title_zh: 零样本多语言细粒度情感分析提示策略评估
authors:
- Jakub Šm{í}d
- Pavel Kr{á}l
affiliations:
- Department of Computer Science and Engineering, University of West Bohemia in Pilsen
- NTIS - New Technologies for the Information Society, University of West Bohemia
  in Pilsen
arxiv_id: '2611.27807'
url: https://arxiv.org/abs/2611.27807
pdf_url: https://arxiv.org/pdf/2611.27807
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM提示工程 · 多语言情感分析
tags:
- ABSA
- Prompt Engineering
- Zero-Shot Learning
- Multilingual NLP
- MoE
- LLM
one_liner: 系统评估4类提示范式与7款开源LLM的多语言零样本细粒度情感分析表现，验证单步提示最优
practical_value: '- 跨境电商多语言评论情感抽取场景优先选用monolithic单步提示，可同时提升准确率、降低token开销

  - 中小参数LLM做细粒度情感抽取不要增加迭代优化步骤，会引发过修正导致效果下降，仅大模型可尝试

  - 零样本多语言NLP任务优先选择同参数规模的dense架构LLM，效果优于MoE架构且推理更稳定'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有细粒度情感分析（ABSA）研究多聚焦英文场景或依赖任务特定微调模型，开源LLM在零样本多语言场景下的目标-方面-情感三元组抽取（TASD）能力缺乏系统性验证。
### 方法关键点
覆盖12种语言、3个业务领域，测试7款8B-35B参数的指令微调开源LLM（含dense、MoE架构），对比monolithic、CoT、sequential、sequential refine四类提示范式的表现。
### 关键结果数字
单步monolithic提示零样本性能最优，优于所有多步流程；同参数下dense模型效果显著超过MoE架构；多步策略会产生最高2.38倍token开销但无F1收益；初始方面词召回是任务核心瓶颈，小模型用迭代修正会出现过修正负收益，仅大模型可部分挽回损失。
