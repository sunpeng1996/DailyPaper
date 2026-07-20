---
title: 'Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy
  Optimization'
title_zh: 超越熵：基于对比策略优化的正确性感知优势塑形
authors:
- Weiwen Xu
- Jia Liu
- Hou Pong Chan
- Long Li
- Deng Cai
- Min Chen
- Hao Zhang
affiliations:
- The Chinese University of Hong Kong
- South China University of Technology
- Nanyang Technological University
arxiv_id: '2607.14614'
url: https://arxiv.org/abs/2607.14614
pdf_url: https://arxiv.org/pdf/2607.14614
published: '2026-07-15'
collected: '2026-07-20'
category: Training
direction: 大模型RL训练 · 正确性感知优势塑形
tags:
- Reinforcement Learning
- Policy Optimization
- GRPO
- Advantage Shaping
- LLM Reasoning
one_liner: 提出对比策略优化CPO，用token级对比分歧做RLVR的正确性感知优势塑形，性能远超熵基方法
practical_value: '- 电商/服务Agent的多轮推理RL微调场景：可用CPO替代GRPO中的熵正则，基于历史正确回复/标准答案生成对比分歧，提升推理准确率的同时保留跨场景泛化性

  - 生成式推荐的RLAIF微调场景：对已验证的正确推荐理由、客服话术等样本，利用CPO的token级优势塑形挖掘零优势组的训练价值，降低标注数据需求量

  - 搜索Query改写的质量校准场景：可复用对比分歧思路，对比改写前后的token概率差，准确定位导致改写效果差的关键token，做细粒度优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有可验证奖励强化学习（RLVR，如GRPO）普遍采用熵做优势塑形，但熵仅能衡量不确定性，无法区分有益的探索波动和有害的推理错误，和正确性信号天然错位，同时GRPO的二进制奖励方案存在零优势样本组无梯度、训练数据浪费的问题，亟需更可靠的正确性感知细粒度信号。

### 方法关键点
- 提出token级对比分歧：计算同一模型在原生生成分布、参考答案引导的生成分布下，对应位置token的对数概率差，理论和实验证明该值与token级正确性正相关，负分歧明确对应错误倾向的token
- 优势塑形设计：将轨迹级全局优势与token级对比分歧结合，加入裁剪机制保证塑形后的优势方向和轨迹级奖励一致，零优势样本直接用分歧作为训练信号，解决样本浪费问题
- 理论层面证明On-policy Distillation是CPO的特殊case，参考引导分布可替换为外部教师模型、批评反馈等任意比当前策略更具正确性信息的分布，适用性广

### 关键实验
基于Qwen2.5-Math-7B、Qwen3-Base-4B两个底座，在MATH、AIME、AMC等数学推理数据集，以及GPQA、MMLU-Pro等跨域推理数据集上测试，对比GRPO、DAPO、各类熵基RLVR方法，CPO平均性能分别比GRPO高7.7%、8.5%，同时跨域泛化性远优于基线，额外训练开销仅比GRPO高20%。

### 核心洞见
熵反映的是语言层面的不确定性，而对比分歧聚焦的是任务层面的正确性，后者才是RL训练中更应该优先优化的信号。
