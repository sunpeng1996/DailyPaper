---
title: 'Aligning Language Models with General Preferences: An Empirical Study of Direct
  Nash Optimization'
title_zh: 通用偏好对齐方法Direct Nash Optimization实证研究
authors:
- Austin Tsai
- Saurav Nanda
- Ganapathy Parthasarathy
- Bhuvnesh Kumar
- Parivesh Choudhary
affiliations:
- Synopsys, Inc.
arxiv_id: '2611.05373'
url: https://arxiv.org/abs/2611.05373
pdf_url: https://arxiv.org/pdf/2611.05373
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: 大语言模型 · 偏好对齐训练
tags:
- DNO
- preference alignment
- DPO
- LLM training
- iterative alignment
one_liner: 独立复现DNO-Prct对齐方法，验证跨模型效果、组件价值，支持开源标注器替代闭源模型
practical_value: '- 电商Agent/生成式推荐场景做LLM偏好对齐时，可直接复用DNO-Prct迭代流程：每轮on-policy采样+大模型打分+margin过滤+DPO更新，无需额外训练Reward
  Model，降低对齐成本

  - 无闭源大模型标注能力时，可换用同系列更大的开源模型做标注，能保留62%~82%的对齐增益，适合业务侧低成本迭代

  - 对齐优化优先级：优先保留教师gold response、历史数据look-back、允许学生响应优于教师的配对规则，去掉任意一个会掉6~10个点的LC胜率，远大于调整采样数、margin的影响

  - 小参数模型对齐可采用DNO，实现8B模型效果超过同系列70B基线，适合生成式推荐、Query生成等场景降本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLHF、DPO等偏好对齐方法依赖固定偏好数据集/奖励模型，无法处理非传递偏好，还会随策略分布偏移出现效果衰减；DNO作为基于纳什均衡的新型对齐方法，此前仅在单模型+闭源标注器下验证效果，无独立复现，跨模型兼容性、组件价值、开源标注可行性均不明确。

### 方法关键点
- 复现实用版DNO-Prct迭代流程：每轮从当前策略采样K个响应，加入教师gold response，用标注器打分，选择分差满足margin的正负对，混合30%前一轮、15%前二轮的历史对，用DPO目标更新，参考策略为上一轮checkpoint
- 实验覆盖Llama 3.1 8B Instruct、Mistral 7B Instruct v0.1两个开源基座，标注器分别采用GPT-4o、同系列大参数开源模型
- ablation覆盖采样数、margin、gold response、look-back、配对选择规则等核心组件

### 关键结果
- 基于UltraFeedback数据集，对比SFT、离线DPO、SPIN等baseline，3轮迭代后Llama 3.1 8B的AlpacaEval 2.0 LC胜率从31.7%升至45.3%，超过同系列70B基线；Mistral 7B从6.8%升至18.4%，接近Mixtral 8x7B水平
- 用同系列开源大模型做标注器，Llama侧保留62%的LC增益，Mistral侧保留82%，无需依赖闭源模型
- ablation显示：去掉gold response、look-back、仅保留教师优先对，LC胜率下降6~10点；调整每prompt采样数（1~7）、margin（1~5）对效果影响仅2点左右

DNO对齐的核心增益来自gold response、历史数据复用、允许学生胜出的宽松配对规则，而非采样数、margin等超参，且完全可基于开源模型闭环实现
