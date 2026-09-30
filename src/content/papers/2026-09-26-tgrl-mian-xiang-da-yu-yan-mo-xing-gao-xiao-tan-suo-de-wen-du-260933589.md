---
title: 'TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration
  in LLMs'
title_zh: TGRL：面向大语言模型高效探索的温度分组强化学习
authors:
- Zihan Lin
- Xiaohan Wang
- Jie Cao
- Jiajun Chai
- Wei Lin
- Guojun Yin
- Ran He
affiliations:
- University of Chinese Academy of Sciences
- Meituan
- MAIS&NLPR, Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2609.33589'
url: https://arxiv.org/abs/2609.33589
pdf_url: https://arxiv.org/pdf/2609.33589
published: '2026-09-26'
collected: '2026-09-30'
category: Training
direction: LLM RL训练 · 高效探索优化
tags:
- RLVR
- Reinforcement Learning
- Efficient Exploration
- Temperature Control
- LLM Fine-tuning
one_liner: 通过高低温采样分组的奖励差提取探索增益，不增加rollout预算提升RLVR性能与训练效率
practical_value: '- 做电商导购Agent、智能客服的RL微调时，可直接复用高低温分组设计，无需增加rollout采样数量即可提升探索效率，解决RL过早收敛到局部最优的问题

  - 做RLHF/RLVR的token级credit分配时，可基于高低温next-token分布的JS divergence识别关键token，把梯度集中在对生成结果影响大的位置，降低无效梯度、提升训练速度

  - 生成式推荐场景（如个性化文案、商品推荐理由生成）的RL微调中，该方法可在相同算力预算下提升生成内容的多样性和匹配度，适配电商场景的高吞吐需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR是当前LLM后训练提升推理、多轮决策能力的核心范式，但高效探索一直是瓶颈：传统温度控制、多采样探索要么增加rollout阶段的样本成本，要么无法量化探索收益，导致RL优化易过早收敛到窄解码模式，限制模型性能上限。
### 方法关键点
- 每个prompt同时采样低温度（T0=0.3）参考组和高温度（T1=1.2）探索组，用两组平均奖励差作为prompt级探索增益的无偏估计，注入混合组优势计算
- 计算token级高低温next-token分布的JS divergence，识别温度敏感token，经对数压缩、轨迹内归一化得到token权重，将探索增益分配到对应位置
- 仅对高温度组的token按加权优势更新，低温度组仅参与组均值/方差统计、不参与梯度更新，避免梯度方向冲突
### 关键结果
跨数学推理、代码生成、长horizon Agent三类任务11个基准测试，对比PPO、GRPO、DAPO等强基线：32B模型6项数学基准平均提升1.6%，CodeForces评分提升196.7分，LiveCodeBench Pass@16提升4.4%，ALFWorld/WebShop成功率分别提升6.3%/4.9%，达到同等精度的训练速度比基线快36%，全程未增加rollout采样预算。
> 最值得记住的一句话：采样温度不只是解码参数，更可作为RL探索信号的可控干预手段，无需增加采样成本即可通过分组对比和细粒度credit分配大幅提升RL训练效率
