---
title: 'Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling
  at Equal Token Cost, from 1.5B to 7B'
title_zh: 等生成Token成本下1.5B~7B模型自优化/自反思效果不及重复采样
authors:
- Iliya Mirzaei
affiliations:
- Stony Brook University
arxiv_id: '2607.28576'
url: https://arxiv.org/abs/2607.28576
pdf_url: https://arxiv.org/pdf/2607.28576
published: '2026-07-30'
collected: '2026-07-31'
category: Reasoning
direction: LLM推理优化 · 成本对齐效果评估
tags:
- Reasoning
- Self-Refine
- Reflexion
- Self-Consistency
- Cost-Aligned Evaluation
- LLM Inference
one_liner: 控制生成Token成本对比7类推理方法，证明无自评估的重复采样准确率更优
practical_value: '- 业务侧LLM推理场景（Agent任务规划、推荐理由生成、Query改写纠错）优先将Token预算分配给多采样+多数投票，7B以下小模型比自反思/自优化策略准确率最高高17pp，ROI更优

  - 若采用Best-of-N选优策略，7B以下小模型直接用多数投票替代LLM自评估，无需额外设计评估prompt即可获得准确率提升，还能降低逻辑复杂度

  - 上线带自适应早停的推理策略（如动态触发的反思逻辑）时，必须统计自适应逻辑的实际触发率，避免策略退化为基础CoT却误判收益，AB测时需增加该指标做校验

  - 小模型端侧部署场景（如端侧推荐、离线Query改写）直接放弃复杂自反思prompt链路，用多采样投票即可用相同成本获得更稳定的效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Self-Refine、Reflexion、多Agent辩论等无训练推理提升方法，大多通过增加生成Token量获得效果收益，过往对比未严格对齐Token成本，无法证明其机制本身的价值，且缺乏1.5B、3B等小模型场景下的统计显著性验证，结论容易被噪声干扰。
### 方法关键点
- 覆盖Qwen2.5 1.5B/3B/7B三个尺寸开源指令模型，在GSM8K、MATH-500两个数学推理数据集各采样150题做配对测试
- 成本定义为单问题所有生成Token（含反思、评估、辩论等中间内容，不包含输入Token），基线为等成本的Self-Consistency（多独立采样+多数投票）
- 对比7类主流推理方法：CoT、Plan-and-Solve、Self-Refine、原生Reflexion、强制运行版Reflexion、Best-of-N（LLM自选最优解）、多Agent辩论
- 所有对比采用配对bootstrap置信区间检验，跨方法做Holm校正，控制多重比较的假阳性率
### 关键结果
36组等成本对比中无任何方法显著优于重复采样基线，10组显著更差的结果全部来自含自评估/自改写逻辑的方法；1.5B模型下Best-of-N自选择比同采样的多数投票准确率低8~11.3pp，7B模型下差距收窄到1.3~2pp，无统计显著性；强制运行的Reflexion、Self-Refine在7B模型下仍比基线低3.6~10.1pp。

最值得记住的结论：同等Token预算下，算力花在多生成独立答案再投票的ROI永远高于让模型反思、评估已有答案，7B以下小模型尤其明显
