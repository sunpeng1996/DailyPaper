---
title: 'Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning'
title_zh: 识别能力边界：诊断与训练LLM终止无效推理
authors:
- Xinyan Guan
- Jiali Zeng
- Chunlei Xin
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
- Fandong Meng
affiliations:
- 中国科学院软件研究所
- 中国科学院大学
- 腾讯微信AI
arxiv_id: '2607.29211'
url: https://arxiv.org/abs/2607.29211
pdf_url: https://arxiv.org/pdf/2607.29211
published: '2026-07-31'
collected: '2026-08-03'
category: Reasoning
direction: LLM推理校准 · 能力边界对齐
tags:
- Futile Reasoning
- Capability Alignment
- RL
- GRPO
- Reasoning Calibration
one_liner: 提出CaRL对齐框架，训练LLM识别能力边界，主动终止超边界任务的无效推理
practical_value: '- 电商/广告Agent的推理链路可复用CaRL的奖励分层设计：正确应答得+1、合理拒答得0、错误应答得-1，避免用户问超边界问题时生成幻觉误导决策，同时不会过度降低有效应答率

  - 大模型推理服务的成本优化可借鉴Hindsight Refusal Augmentation思路：将历史无效推理的失败样本转化为拒答训练样本，不需要额外标注就能低成本让模型提前终止无效推理，减少长token生成的算力浪费

  - 生成式推荐场景下的输出校准可复用这套能力边界对齐逻辑：当用户请求无匹配商品/活动时，训练模型主动告知无结果而非生成虚假的商品信息，降低用户投诉率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM面对超出自身能力的任务时，不会主动终止，反而会生成看似合理实则错误的无效推理（Futile Reasoning），既误导用户又浪费大量算力。现有prompt引导方法效果极差，硬任务上仍有80%以上的无效推理尝试，且存在6倍的过度自信偏差，过度自信发生率（20%）是过度保守（3.4%）的6倍，硬任务上拒答召回率低于30%，急需更有效的干预方案。

### 方法关键点
1. 设计Capability-Calibrated Reward Shaping：采用分层奖励规则，正确回答得+1、有效拒答得0、错误回答得-1，激励模型优先选择拒答而非生成无效推理
2. 提出Hindsight Refusal Augmentation（后见拒答增强）：将所有生成错误答案的轨迹，保留推理过程后拼接拒答话术，转化为拒答训练样本，解决拒答样本稀疏的问题
3. 基于GRPO算法优化，不需要额外标注即可完成训练，可适配任意基座LLM

### 关键实验
在Countdown、Sudoku等推理任务上测试Qwen3-8B/14B，对比Vanilla、Standard RL、RFT等基线，Qwen3-14B的无效推理率从78.6%降至1.0%，同时准确率仅下降不到2%；域外任务上无效推理率降低44.5%，推理token长度减少25%以上，跨难度泛化性显著优于监督微调方案。

### 核心结论
当模型能力边界明确时，主动拒答远好于生成看似正确的幻觉，还能显著降低算力成本
