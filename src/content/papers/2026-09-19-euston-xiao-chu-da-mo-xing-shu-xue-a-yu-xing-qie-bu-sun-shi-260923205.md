---
title: 'Euston: Training Away Mathematical Sycophancy Without Losing the Mathematics'
title_zh: 《Euston：消除大模型数学阿谀性且不损失通用数学能力》
authors:
- Zehua Cheng
- Wei Dai
- Jiahao Sun
affiliations:
- University of Oxford
- FLock.io
arxiv_id: '2609.23205'
url: https://arxiv.org/abs/2609.23205
pdf_url: https://arxiv.org/pdf/2609.23205
published: '2026-09-19'
collected: '2026-09-22'
category: LLM
direction: 大模型对齐 · 阿谀性抑制
tags:
- LLM Alignment
- Sycophancy Mitigation
- GRPO
- Synthetic Data Generation
- Mathematical Reasoning
one_liner: 基于8B推理模型的抗数学阿谀训练方案，判别能力大幅提升且无统计显著的通用数学能力损失
practical_value: '- 做Agent工具调用/事实校验场景的对齐训练时，可复用「匹配式正负样本+GRPO+零API规则奖励」的配方，既能提升判别能力又不易损失通用能力

  - 训练分类/判别类LLM任务时，避免用单一类别样本训练，否则模型容易学到偷懒捷径（比如全输出某一类），平衡正负样本是核心前提

  - 做RLHF类训练时，必须周期性监控原模型的核心通用能力（比如推荐场景下的物品匹配精度），避免优化窄目标导致能力退化

  - 电商场景做商品合规校验、虚假宣传识别的LLM微调，可借鉴GraphSynth的负样本生成思路：控制正负样本仅核心属性有差异，避免模型靠表面特征判别'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前推理类LLM普遍被训练为「尽可能给出答案而非拒绝回答」，遇到错误数学命题时也会顺着推导错误结论，即数学阿谀性；直接用奖励引导模型输出错误判断的方案要么容易被「全输出错误」的捷径作弊，要么会严重损失模型原有的通用数学解题能力，尚无兼顾判别能力提升与通用能力保留的成熟方案。

### 方法关键点
- 数据层面：用GraphSynth生成3026组匹配的真/假数学命题对，正负样本仅在真值上有差异，结构、语义高度一致，避免模型靠表面特征判别，且训练集和测试集时间完全隔离避免泄露
- 训练层面：基于DeepSeek-R1-0528-Qwen3-8B底座，用GRPO算法微调，奖励为零API规则判断：仅当输出的`\boxed{}`标签内容和真值完全匹配时给1分，否则0分，训练189步仅需4张H100跑13.8小时
- 评估层面：同时监控判别能力、通用数学能力两类指标，避免优化窄目标损失通用能力

### 关键结果
- 平衡测试集（200真/200假）上的平衡准确率从29.5%提升到63.75%，判别gap从-0.5pp提升到27.5pp
- AIME 2026数学竞赛准确率仅从69.17%降到65%，降幅4.17pp无统计显著性，通用数学能力基本保留
- 输出截断率从25.8%降到8.3%，中位输出长度从19217token降到18296token，推理效率反而提升

> 最值得记住的一句话：判别类LLM训练的核心瓶颈是高质量匹配正负样本的质量和规模，而非优化器，劣质样本会让模型学到捷径同时严重损失通用能力。
