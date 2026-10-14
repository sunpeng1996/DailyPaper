---
title: 'DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter'
title_zh: DeltaTTG：基于Token-to-Go进度度量的多轮Agent训练方法
authors:
- Xuyan Ye
- Xiyan Fu
- Shengda Fan
- Jiawei Cui
- Yankai Lin
- Wei Lu
affiliations:
- Nanyang Technological University
- Renmin University of China
arxiv_id: '2610.17666'
url: https://arxiv.org/abs/2610.17666
pdf_url: https://arxiv.org/pdf/2610.17666
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 多轮Agent RL信用分配优化
tags:
- ReinforcementLearning
- CreditAssignment
- MultiTurnAgent
- GRPO
- TTG
one_liner: 用无额外标注的TTG进度信号优化多轮Agent RL信用分配，效果提升且成本接近GRPO
practical_value: '- 电商搜索导购/客服多轮Agent训练可复用TTG思路：无需人工标注步骤奖励，直接从历史对话/交互轨迹提取剩余Token数作为进度信号，大幅降低过程监督成本

  - 现有GRPO训练的多轮Agent可快速接入DeltaTTG优化：仅需额外训练轻量TTG进度meter，推理阶段冻结，actor训练GPU成本仅比原生GRPO高3%以内，效果提升5-7个点

  - TTG进度meter可跨不同参数规模的actor复用：同领域训练一次meter即可支持从1.7B到14B不同大小的Agent训练甚至测试时动作选择，大幅降低训练边际成本

  - 长路径推荐场景（如多步加购、内容种草转化）可借鉴信用分配思路：用剩余转化路径长度替代TTG，将最终转化奖励按每步进度分配，解决长链路信用分配稀疏问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮Agent的RL训练长期依赖稀疏的终态奖励，步骤级信用分配是核心痛点：组内步骤对比需要可靠的状态匹配和足够多样的采样结果，直接步骤打分需要昂贵的外部评估器、人工标注或任务特定启发式规则，现有方案落地成本高、鲁棒性差。

### 方法关键点
- 提出Token-to-Go（TTG）作为进度监督信号：定义为轨迹从当前状态到任务完成还需要生成的Token数，无需额外标注，可直接从多政策采样的历史轨迹中提取
- 分两步训练TTG进度meter：先SFT学习从对话前缀到TTG值的映射，再用GRPO优化预测精度，训练好的meter在actor训练阶段完全冻结
- 符号感知的信用分配：用meter预测的相邻状态TTG差值衡量每步进度/倒退，将轨迹整体优势按进度权重分配到每一步，混合20%的均匀分配权重降低预测误差影响
- 仅修改GRPO的优势分配逻辑，不额外增加奖励信号，保证训练稳定性

### 关键实验
在ALFWorld、PaperSearchQA、BFCLv3三个基准上测试，对比GRPO、DAPO、GiGPO等主流RL baseline：用Qwen3-4B时平均得分超最强基线2.45分，比GRPO高5.7分；用Llama-3.1-8B-Instruct时平均得分超最强基线4.8分，比GRPO高7.2分；actor训练GPU耗时和GRPO基本持平，样本效率比GiGPO高40%；跨领域迁移下仍比GRPO高2-3个点。

最值得记住的一句话：无需额外标注的剩余工作量类信号是解决长序列/多轮任务稀疏奖励信用分配问题的高性价比路径。
