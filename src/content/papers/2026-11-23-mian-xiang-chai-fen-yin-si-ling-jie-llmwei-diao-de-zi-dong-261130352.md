---
title: 'AutoClip-DPZO: Practical Private Clipping Selection for Differentially Private
  Zeroth-Order LLM Fine-Tuning'
title_zh: 面向差分隐私零阶LLM微调的自动私有裁剪阈值选择方法AutoClip-DPZO
authors:
- Xinghe Chen
- Haichao Sha
- Zihao Wang
- Xiaokui Xiao
- XiaoFeng Wang
- Wei Dong
affiliations:
- Nanyang Technological University
- National University of Singapore
arxiv_id: '2611.30352'
url: https://arxiv.org/abs/2611.30352
pdf_url: https://arxiv.org/pdf/2611.30352
published: '2026-11-23'
collected: '2026-11-24'
category: Training
direction: 差分隐私LLM高效隐私微调优化
tags:
- Differential Privacy
- Zeroth-Order Optimization
- LLM Fine-tuning
- Clipping Threshold
- Privacy Preserving ML
one_liner: 提出无需重复微调的DPZO自动裁剪阈值选择方法，效用媲美非私有搜索得到的最优结果
practical_value: '- 做电商用户行为对齐、个性化Agent训练等隐私敏感垂域LLM微调时，AutoClip-DPZO可省去DPZO裁剪阈值的手动调参成本，仅需一次训练即可达到接近最优的效用，同时不额外消耗隐私预算

  - DPZO低显存的特性适合端侧/小算力环境部署，可用于消费级GPU上基于用户敏感数据的LLM微调（如个性化推荐prompt对齐、电商文案生成模型微调），规避用户数据外传的合规风险

  - 差分隐私训练中超参调优的思路可迁移：将裁剪阈值选择转化为私有分位数估计问题，无需反复跑训练搜索最优值，这套逻辑可复用在DPSGD等其他DP训练范式的超参优化中'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
差分隐私零阶优化（DPZO）是低显存LLM隐私微调的核心方案，但其效用极度敏感于裁剪阈值C，C仅变化2倍即可导致效用下降17.6个点。现有方法需要反复微调不同C的候选模型，不仅计算成本极高，还会消耗额外隐私预算，挤占最终模型训练的预算额度；传统DPSGD的自动裁剪方法不适配DPZO的低维噪声 regime，直接迁移会导致10个点以上的效用损失。
### 方法关键点
- 推导DPZO总误差函数，同时量化噪声方差与裁剪偏差，将C的选择转化为私有分位数估计问题，目标分位数仅由公开的隐私参数、随机方向数K、批次大小b决定，无需私有数据参与计算
- 引入校准因子修正传统三角不等式对裁剪偏差的过高估计，通过全局离线校准得到通用修正系数0.258，无需针对单任务单独调参
- 仅需消耗极小部分隐私预算完成一次私有分位数估计，无需反复微调候选模型，最终仅需一次DPZO训练即可得到接近最优的模型
### 关键实验
在RoBERTa、OPT系列模型（82M~6.7B参数）、9个文本分类/生成任务上测试，对比7个强化基线：
1. 效用媲美非私有搜索得到的最优C结果，平均效用仅下降0.48个点，部分场景反超搜索结果
2. 比每个场景下的最优基线效用平均提升3.7%，最高提升1.8个点
3. 相比搜索式阈值选择方法最高提速6.9倍，仅比固定C的DPZO微调多3%~27%的运行开销
### 核心结论
低算力环境下做用户敏感数据的LLM隐私微调，DPZO+AutoClip是兼顾隐私、成本、效用的高可落地方案
