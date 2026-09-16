---
title: 'ECHO: Early-layer Collaborative Hierarchical Orchestration with Bonus Logits
  in Speculative Decoding'
title_zh: ECHO：基于早期层分层编排与奖励Logits的投机解码加速框架
authors:
- Ziyang Ma
- Zihong Zhang
- Zuchao Li
- Lefei Zhang
- Baoyuan Qi
- Siqi Li
- Simin Yu
affiliations:
- 武汉大学
- 小米
arxiv_id: '2609.17241'
url: https://arxiv.org/abs/2609.17241
pdf_url: https://arxiv.org/pdf/2609.17241
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM推理 · 投机解码无损加速
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Early Exit
- KV Cache
- Lossless Acceleration
one_liner: 无额外部署参数的分层双环投机解码框架，实现LLM推理2.4~2.9倍无损加速
practical_value: '- 推理优化：业务中部署的LLM Agent、生成式推荐文案模型可直接复用ECHO架构，无需新增参数即可实现2倍以上推理提速，降低高并发场景下的调用成本

  - 分层筛选思路：LLM4Rec场景可复用早期层输出做轻量级候选粗筛，最终层做精排，平衡推荐精度与响应时延，适配广告/搜索推荐的低时延要求

  - 状态复用方案：KV cache同步仅占1.15%开销的工程设计可直接复用，大幅降低分布式部署下多轮生成的通信成本

  - 混合候选构造：检索+Logits混合草稿树的思路可迁移到query补全、智能客服场景，提升候选召回准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有无草稿模型的投机解码存在候选过时、全量验证算力开销高的问题，自投机方法又需多次前向传播导致加速比不足，无法满足高并发LLM推理（如电商智能客服、生成式推荐文案生成、Agent多轮调用）的低时延需求。

### 方法关键点
- 分层双环架构：将LLM拆分为早期层敏捷验证器（内循环）和后续层权威验证器（外循环），内循环用早期层Bonus Logits低开销生成多步草稿树，外循环复用中间状态做全量验证，避免重复计算
- 双重Bonus Logits：回收早期层和最终层的输出Logits作为下一轮草稿树的根节点，解决候选过时问题，同时结合n-gram检索候选构造混合草稿树，提升候选接受率
- 无损验证机制：通过树注意力+因果注意力的分层验证设计，保证输出分布与原生模型完全一致，无精度损失

### 关键实验
在Llama-2/3、CodeLlama等7B-70B模型上测试，对比PLD、TokenRecycling、LayerSkip等SOTA基线，在Spec-Bench、HumanEval、GSM8K数据集上实现2.4×~2.9×整体加速，最高在Llama-2-13B上达到3.01×加速，平均接受Token数（MAT）提升到4~5，且分布式高并发场景下状态同步开销仅占1.15%。

### 核心结论
无需新增任何部署参数，仅通过复用LLM层间功能不对称性和中间状态，即可实现近3倍的无损推理加速，工程落地成本极低。
