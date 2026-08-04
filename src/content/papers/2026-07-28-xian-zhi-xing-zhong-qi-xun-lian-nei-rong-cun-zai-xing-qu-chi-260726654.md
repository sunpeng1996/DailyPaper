---
title: 'Constitutional Midtraining: Content Presence Drives Alignment Gains'
title_zh: 宪制性中期训练：内容存在性驱动更持久的LLM对齐增益
authors:
- Desiree Cho
- Cameron Tice
- Bernie Hogan
- Hunar Batra
- Puria Radmard
- Jun Zhao
- Nigel Shadbolt
affiliations:
- University of Oxford
- Geodesic Research
- Oxford Internet Institute
arxiv_id: '2607.26654'
url: https://arxiv.org/abs/2607.26654
pdf_url: https://arxiv.org/pdf/2607.26654
published: '2026-07-28'
collected: '2026-08-04'
category: Training
direction: LLM对齐 · 中期训练优化
tags:
- LLM Alignment
- Midtraining
- Constitutional AI
- Model Safety
- Training Pipeline
one_liner: 120B规模下验证宪制性中期训练可产生持久LLM对齐增益，无额外能力损耗
practical_value: '- 做电商Agent/导购大模型对齐时，可在预训练收尾的中期阶段插入少量业务合规（反刷单、反虚假宣传、隐私保护）的规则类语料，比仅靠SFT/DPO做后训练对齐的效果更持久，不容易被后续业务场景微调侵蚀

  - 中期训练对齐时不用过度纠结语料的课程排序、是否加推理链，核心保证合规/价值观类语料的覆盖度即可，可大幅节省语料加工成本

  - 业务侧对大模型做合规对齐时无需担心对齐损耗通用能力，该方案在120B规模下验证MMLU/GSM8K等能力指标无下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有后训练对齐（SFT/RLHF/DPO）的效果较浅，极易被后续无关任务的微调侵蚀，预训练阶段植入的行为倾向后训练难以有效修改。中期训练（预训练收尾、后训练之前）是低成本对齐的潜力节点，但孤立的宪制性中期训练在大模型尺度下的对齐耐久性此前未被验证。

### 方法关键点
- 基于Anthropic宪制文档构建394M-token对齐语料库，包含带推理链（DR）和不带推理链（noDR）两个版本
- 采用2×2实验设计（课程排序vs均匀排序 × 带推理vs不带推理），在120B MoE模型上开展中期训练，对照组无中期干预
- 所有模型统一经过价值中立SFT、无关任务（GSM8K）微调两个后训练阶段，在三个阶段（中期训练后、SFT后、无关微调后）分别评估对齐效果

### 关键结果数字
- 宪制中期训练组在默认行为类对齐任务上的优势全程保持：勒索场景下对齐率比对照组高17.5pp（无关微调后），OOD对齐率高3.2pp，ID对齐率高1.2pp
- 需主动抵抗上下文压力的任务（对抗性prompt、价值冲突）的优势在SFT后消失
- 无能力损失：MMLU/GSM8K等通用能力指标全程不低于对照组，中期训练后ARC-Easy/PIQA甚至分别高8.2pp、12.6pp
- 内容远重于结构：课程排序、推理链优化仅带来短期微小收益，无长期耐久优势

### 最值得记住的一句话
仅需在中期训练阶段插入少量宪制/价值观类语料，就能以极低的成本获得比后训练更持久的对齐效果，且无能力损耗。
