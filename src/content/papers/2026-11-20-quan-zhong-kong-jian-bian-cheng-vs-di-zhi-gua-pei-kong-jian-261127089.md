---
title: Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming
  and Low-Rank Adaptation
title_zh: 权重空间编程 vs 低秩适配：空间推理任务的模型适配方法对比
authors:
- Yalin Yang
- Xiao Huang
- Yanan Wu
- Hao Yang
- Ryan Zhenqi Zhou
affiliations:
- West Virginia University
- Emory University
- University of Central Arkansas
- Cornell University
- Yale University
arxiv_id: '2611.27089'
url: https://arxiv.org/abs/2611.27089
pdf_url: https://arxiv.org/pdf/2611.27089
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM适配 · 权重编辑与LoRA对比
tags:
- LoRA
- weight-space programming
- spatial reasoning
- parameter-efficient fine-tuning
- model editing
one_liner: 对比零梯度权重编辑与带中间步骤监督的LoRA在空间推理任务的性能、迁移性与副作用
practical_value: '- 多步推理类业务（如导购路径规划、复杂商品属性匹配）做LoRA微调时，加入中间步骤监督比仅监督最终答案效果提升显著，且rank=1的极低秩即可达到接近天花板的性能，大幅降低微调成本

  - 若仅需修复模型特定缺陷（如输出死循环、高频拒答），优先考虑权重空间定向编辑而非微调，对原有业务能力的干扰远小于LoRA微调

  - 用LoRA适配新任务时需警惕任务模板入侵：如果训练触发模式（如数值对+关系查询）和已有业务任务相似，要加入少量原有任务样本做 rehearsal，避免原有能力被覆盖

  - 模型泛化能力优先级：新措辞>新属性组合>更高推理深度，做多跳用户意图理解等复杂任务微调时，要针对性覆盖高深度、新组合样本，不要依赖自然泛化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM适配主要分为梯度驱动类（如LoRA微调）和零梯度权重编辑类（如权重空间编程），两类方法的目标任务性能、跨场景迁移性、对原有能力的副作用缺乏同基准的严格对比；空间推理是典型的多步推理任务，有明确的符号化标准答案，适合作为两类方法的对比测试场。

### 方法关键点
- 基模型采用Qwen3.5-0.8B，对比基线为公开的权重空间编程补丁p50c，微调方案为rank 1/16的全层LoRA，监督信号包含完整推理中间步骤而非仅最终答案
- 任务分为两类：目标任务为参考系转换、StepGame多跳空间推理；离线任务为地图距离比较、商品属性距离比较，用于测试原有能力保留度
- 泛化测试设置三类OOD场景：未见句式模板、未见推理难度、未见属性组合

### 关键实验
- 目标任务上，p50c补丁将参考系任务准确率从0%提升到22.1%，StepGame从19.2%提升到33.7%；而仅含0.09%参数量的rank=1 LoRA在两个任务上分别达到100%、98.8%的准确率
- 泛化性上，LoRA对未见句式模板准确率达82%，对未见难度（训练1-5级测试6-10级）仅42%，对未见属性组合仅33%-50%
- 副作用上，p50c保留了离线距离任务92%+的准确率，而LoRA几乎完全丢失离线任务能力，准确率降到0-2%，出现严重的任务模板入侵

### 核心结论
零梯度权重编辑适合修复模型特定缺陷、对原有能力干扰极小，而带中间步骤监督的LoRA适合快速安装新能力，但会触发任务模板入侵、干扰原有相似任务的性能，需通过样本回放缓解。
