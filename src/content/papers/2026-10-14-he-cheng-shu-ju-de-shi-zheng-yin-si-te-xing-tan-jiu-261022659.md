---
title: Exploring The Empirical Privacy Landscape of Synthetic Data
title_zh: 合成数据的实证隐私特性探究
authors:
- Zihao Zhao
- Avi Schwarzschild
- Casey Meehan
- Katherine Lee
- Zhili Feng
- Dylan Sam
affiliations:
- Johns Hopkins University
- OpenAI
arxiv_id: '2610.22659'
url: https://arxiv.org/abs/2610.22659
pdf_url: https://arxiv.org/pdf/2610.22659
published: '2026-10-14'
collected: '2026-10-23'
category: Training
direction: LLM训练隐私 · 合成数据优化
tags:
- Synthetic Data
- Privacy Protection
- DP-SGD
- LLM Training
- Privacy Leakage
one_liner: 对比数据与训练级隐私干预方案，验证隐私感知合成数据改写可实现更优的能力-隐私权衡
practical_value: '- 处理电商/广告领域敏感用户数据训练LLM时，优先采用隐私感知改写的合成数据替代直接微调，可在能力损失可控的前提下降低隐私泄露风险

  - 选择合成数据改写基座时，优先选能力更强的通用模型，无需盲目增加测试时计算量，其隐私防护效果更稳定

  - 验证隐私泄露可采用canary埋点方案，可快速对比不同数据处理/训练策略的隐私风险，适配电商用户行为数据隐私合规场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM适配高敏感领域需训练敏感数据，现有隐私干预方案的能力-隐私权衡效果缺乏系统的实证对照。

### 方法关键点
以嵌入canary泄露探针的合成医疗记录为测试基准，横向对比三类隐私干预方案：直接微调、DP-SGD训练、合成数据改写（含朴素改写、隐私感知改写），从下游任务能力、隐私泄露率两个维度量化评估。

### 关键结果
1. 直接微调下游能力最优，但隐私泄露率最高；
2. DP-SGD可显著降低泄露，但下游能力损失幅度最大；
3. 带唯一标识感知替换指令的隐私感知合成数据改写，相较朴素改写的隐私防护效果在不同基座下均有提升，且能力损失远低于DP-SGD，是现有方案中权衡最优的路径；
4. 能力更强的改写模型可进一步降低下游泄露风险，提升测试时算力无稳定增益。
