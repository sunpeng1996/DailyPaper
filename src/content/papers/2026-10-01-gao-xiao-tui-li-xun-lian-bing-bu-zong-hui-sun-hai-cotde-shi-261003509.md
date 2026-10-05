---
title: Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability
title_zh: 高效推理训练并不总会损害CoT的忠实度与可监测性
authors:
- Samuel Lewis-Lim
- Xingwei Tan
- Mario Sanger
- Zhixue Zhao
- Nikolaos Aletras
affiliations:
- University of Sheffield
- AstraZeneca
arxiv_id: '2610.03509'
url: https://arxiv.org/abs/2610.03509
pdf_url: https://arxiv.org/pdf/2610.03509
published: '2026-10-01'
collected: '2026-10-05'
category: Reasoning
direction: 大模型思维链（CoT）高效推理训练
tags:
- Chain-of-Thought
- Efficient Reasoning
- Faithfulness
- Monitorability
- Reinforcement Learning
- LoRA
one_liner: 对比三类高效CoT训练方法，证实适度压缩可保留可监测性，部分场景不降低忠实度
practical_value: '- 电商导购Agent/推理类推荐系统降本时，优先选用ThinkPrune或GLP方法做CoT压缩，可实现40%-65%的长度缩减且基本保留有害行为监测能力，适配实时推理场景

  - 若CoT用于推荐逻辑可解释/用户决策归因，需避免过度压缩CoT，尤其是高可靠性要求的场景（如金融、医疗商品推荐），防止忠实度下降引发的决策偏差

  - 搭建Agent行为监控系统时，不需要解析全量长CoT，适度压缩的CoT仍可检测90%以上的干预影响，可大幅降低监控模块的推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
CoT可提升LLM推理效果、支撑模型行为审计，但长CoT会大幅提升推理延迟与算力成本。现有高效推理训练通过压缩CoT长度降本，但业界普遍担忧该过程会让CoT丧失忠实度（无法反映模型真实决策逻辑）与可监测性（无法检测输入干预对输出的影响），不同压缩方法的实际影响差异此前缺乏系统性验证。

## 方法关键点
- 选取Qwen3-4B、Qwen3-8B、Olmo3-7B-Think三款开源推理模型，基于LoRA微调对比三类高效训练方法：固定生成预算的ThinkPrune、按示例指定长度目标的L1、组内相对长度奖励的GLP
- 评估维度：忠实度用NSG（标准化可模拟增益，衡量CoT对模型同类输入决策的预测提升度）；可监测性用g-mean2（衡量监控方仅通过CoT检测输入干预的能力）
- 训练集为AIME/AMC数学题，评估覆盖7个通用决策任务+2类干预场景（用户谄媚行为、医疗认知偏差）

## 关键结果
- 多数场景下高效训练会降低忠实度，但ThinkPrune（CoT缩短42%）、GLP（CoT缩短65%）在部分模型上无NSG损失甚至略有提升；忠实度下降的核心原因是模型决策一致性降低，而非CoT信息丢失
- 可监测性对压缩的鲁棒性更高：70%长度压缩下谄媚行为检测能力几乎无损失，仅极端压缩（相对base缩短70%以上）时认知偏差检测能力下降0.2以上，下降幅度与相对压缩比例的相关性（ρ=0.68）远高于绝对CoT长度

> 最值得记住的结论：高效推理训练是否损害CoT的审计价值，核心取决于压缩比例与使用场景，而非CoT的绝对长度
