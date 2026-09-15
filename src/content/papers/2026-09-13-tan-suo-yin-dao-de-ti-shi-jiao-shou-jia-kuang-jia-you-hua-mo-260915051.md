---
title: 'Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal
  Reinforcement Post-Training'
title_zh: 探索引导的提示脚手架框架 优化多模态大模型RL后训练效率
authors:
- Yuanhao Yue
- Qianli Ma
- Chengyu Wang
- Haoting Wang
- Lei Shen
- Jun Huang
affiliations:
- Alibaba Cloud Computing
- Shanghai Jiao Tong University
- Fudan University
- Xi'an Jiaotong University
arxiv_id: '2609.15051'
url: https://arxiv.org/abs/2609.15051
pdf_url: https://arxiv.org/pdf/2609.15051
published: '2026-09-13'
collected: '2026-09-15'
category: Training
direction: 多模态大模型 · RL后训练优化
tags:
- Reinforcement Learning
- MLLM
- GRPO
- Prompt Scaffolding
- Curriculum Learning
one_liner: 提出轻量探索潜力评分与动态提示改写框架 显著提升多模态大模型RL后训练的域内与跨域性能
practical_value: '- 电商导购Agent、商品文案生成等RL对齐场景可直接复用EPS指标，基于现有GRPO的rollout统计量即可计算，无额外开销，可快速过滤低效用训练prompt，提升训练效率30%+

  - 低效用prompt无需直接丢弃，可调用能力更强的大模型作为teacher改写为脚手架版本（保留原任务意图，仅补充引导信息不泄露标准答案），反向扩充训练池，比传统token级知识蒸馏的跨域泛化效果提升10%以上

  - 动态prompt池的异步更新架构可直接复用进工业界RL训练pipeline，改写逻辑与主训练流程解耦，几乎不影响主训练吞吐量，适合大规模训练场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）的RL后训练（如GRPO）默认所有训练prompt的学习效用一致，实际存在大量饱和（模型当前已能稳定答对，梯度收益极低）或过难（模型完全无法答对，奖励信号噪声大）的prompt，浪费大量rollout预算，训练效率低下，且跨域泛化效果差。尤其多模态场景下prompt难度受文本复杂度、视觉内容双重影响，效用随模型训练进程动态变化，静态训练数据集无法适配模型的动态能力。
### 方法关键点
- 提出轻量**Exploration Potential Score（EPS）**：基于KL正则化策略提升理论推导，直接复用GRPO训练中已收集的rollout奖励统计量计算，公式为「奖励的softmax加权和 - 奖励均值」，无额外推理或采样开销，可准确衡量prompt当前的可提升空间，EPS≤0判定为低效用prompt。
- 自适应提示脚手架框架：低效用prompt送入teacher模型，结合学生的rollout结果、对应奖励改写为脚手架版本（保留原任务意图，仅补充推理引导，不泄露最终答案），异步更新回动态训练池；同时定期重评估储备池中的旧prompt，模型能力提升后重新激活加入训练，形成适配模型能力的动态课程数据飞轮。
### 关键实验
基于Qwen3-VL 2B/4B backbone，在Geo3K、MMK12多模态推理数据集上做GRPO后训练，对比纯GRPO基线：域内相对提升最高9.7%，跨域MathVision数据集提升11.5%，MMMU-Pro数据集提升11.1%，参数更小的2B模型相对收益更显著。
### 最值得记住的一句话
RL后训练中，对低效用训练prompt做自适应改写优化，比单纯优化策略算法或奖励函数的边际收益更高，训练数据的动态 curation 是被严重低估的优化方向
