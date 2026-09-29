---
title: Why Deterministic PRM Guidance Underperforms in Discrete Diffusion Reasoning
title_zh: 离散扩散推理中确定性PRM引导效果不佳的原因分析
authors:
- Yan Zhan
- Shaobo Liu
- Zhijun Gao
affiliations:
- Peking University
- Shenzhen University
arxiv_id: '2609.35472'
url: https://arxiv.org/abs/2609.35472
pdf_url: https://arxiv.org/pdf/2609.35472
published: '2026-09-27'
collected: '2026-09-29'
category: Reasoning
direction: 离散扩散大模型 · 推理奖励引导优化
tags:
- Process Reward Model
- Discrete Diffusion LLM
- Outcome Reward Model
- LLM Reasoning
- Test-time Optimization
one_liner: 同计算预算下离散扩散模型的确定性PRM引导效果显著弱于ORM重排并拆解两大成因
practical_value: '- 做Agent推理、生成式文案/内容重排场景优化时，优先用同计算预算的ORM重排做基线对标，不要盲目投入PRM中间引导的复杂开发，避免无收益的工程浪费

  - 针对离散扩散类生成模型的引导，尽量晚触发剪枝、保留更多候选，剪枝阶段保留top-4候选可将剪丢正确解的概率从20%降至6%

  - 过程奖励模型如果要承担最终排序职责，尽量针对最终状态单独微调，跨掩码比训练的PRM在最终排序上效果远差于专门的ORM

  - 因果结构的PRM不要用平均池化做读头，换用最后token池化可回收70%的ROC-AUC损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
离散扩散语言模型（dLLM）每步都会输出部分去噪的中间状态，业界普遍认为过程奖励模型（PRM）引导是提升其推理性能的天然方案，但此前没有在相同计算预算下与简单基线做公平对比，PRM引导的实际收益存疑。

### 方法关键点
- 提出统一前向传播次数的成本核算规则，将去噪、PRM打分、ORM打分都折算为相同单位的前向传播次数，消除打分模块的隐藏成本干扰
- 对比两类方案：确定性PRM引导（每b步生成K个候选、剪枝保留PRM最高分的1个）、独立采样加ORM重排（生成N个完整结果后用ORM选最优）
- 拆解性能gap的两个来源：中间状态信号衰减导致的候选池损伤、跨掩码训练的PRM作为最终排序器的效果缺陷

### 关键结果
在Dream-v0-Instruct-7B上测试，数据集覆盖GSM8K、MATH、MBPP：
- 同预算下，GSM8K上8候选时ORM重排准确率75.13%，PRM引导仅65.18%，差9.95pp；32候选时差12.69pp，MATH和MBPP上分别差9.85pp、12.16pp
- PRM的ROC-AUC随掩码率升高从0.77降至0.54，确定性top-1剪枝会让候选池的最优准确率上限从81.05%降至67.30%
- 跨掩码训练的PRM做最终重排效果远差于ORM，仅针对最终状态微调的PRM可达到和ORM相当的效果

**最值得记住的一句话**：同等推理计算预算下，优先把算力花在生成更多独立候选加最终ORM重排上，远好于用确定性PRM引导做中间剪枝。
