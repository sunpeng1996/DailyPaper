---
title: 'Decoupling Solving from Abstention: Single-Rollout Conformal Risk Control
  for Hard-Budget LLM Reasoning'
title_zh: 解耦求解与弃权：硬预算LLM推理的单轮保形风险控制
authors:
- Qianyi Chen
- Bo Li
affiliations:
- School of Economics and Management, Tsinghua University
arxiv_id: '2611.31065'
url: https://arxiv.org/abs/2611.31065
pdf_url: https://arxiv.org/pdf/2611.31065
published: '2026-11-23'
collected: '2026-11-24'
category: Reasoning
direction: LLM推理 · 保形风险控制
tags:
- Conformal Risk Control
- Budgeted Reasoning
- RLHF
- Uncertainty Estimation
- LoRA
one_liner: 提出单轮Tail-CRC框架，解耦硬预算下LLM求解与弃权决策，实现可控错误率与推理效率提升
practical_value: '- 可复用「训练-校准解耦」架构：做生成式推荐、Agent推理时，先仅用正确输出的正向奖励训练模型最大化预算内有效输出，再单独做风险校准控制错误率，避免加错误惩罚导致模型不敢输出的探索饥饿问题

  - 可信度打分trick直接落地：取生成结果段token NLL的前10%均值作为不确定性评分，比直接用最终输出NLL、全段总NLL的区分度更高，无额外推理成本，可用于生成式推荐文案、Agent回复的质量过滤

  - 硬预算场景优化方案：电商客服Agent、实时广告文案生成等对推理耗时/token消耗有严格限制的场景，用预算强制终止+CRC校准的组合，可在错误率达标的前提下实现2倍左右的推理加速，降低部署成本'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM做CoT推理时受硬token预算限制，强制终止推理虽能提升输出完成率，但会大幅抬升错误输出率；现有方法要么用带错误惩罚的RL训练，导致模型为了避错故意耗尽预算陷入探索饥饿，要么多采样保形方法成倍增加推理成本，无法同时满足低错误率、高正确输出率、低推理成本三个核心需求。
### 方法关键点
- 两阶段解耦架构：第一阶段用纯二进制正确性奖励的RL（Dr. GRPO + Rank32 LoRA）训练适应硬预算的求解器，最大化预算内正确输出数量；第二阶段冻结求解器权重，单独做风险校准，无需重新训练即可调整风险阈值或适配新域
- 单轮不确定性打分：仅用单轮生成返回的token log概率，取答案段前10%最大NLL的均值作为不确定性评分，消除长度偏置，避免单token异常值干扰
- CRC校准：基于交换性假设用少量标注校准集计算阈值，保证有限样本下错误提交率不超过预设目标
### 关键实验结果
在Qwen3.5-4B、Qwen3-8B上测试，数据集为DAPO、跨域Omni-MATH，对比原生解码、预算强制、带惩罚RL等baseline：50步RL更新比纯预算强制的正确提交率提升15.0~29.6个百分点，生成成本降低3.5~12.6%；8B模型在Omni-MATH 4K/8K预算下，校准后错误提交率从30.3%/41.8%降至5.8%/6.5%；4K生成比无强制8K解码速度快2.05×（4B）/2.23×（8B）。

**最值得记住的一句话**：硬预算下LLM推理的求解能力和风险控制应该完全解耦，用纯正向奖励训出最大求解能力后再做校准，效果优于耦合错误惩罚的训练方案
