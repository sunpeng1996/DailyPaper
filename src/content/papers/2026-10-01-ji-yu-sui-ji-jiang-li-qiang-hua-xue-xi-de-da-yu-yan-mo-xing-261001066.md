---
title: 'Probe with Participation Trophies: Random-Reward RL as a Probe of LLM Capability'
title_zh: 基于随机奖励强化学习的大语言模型潜在可达能力探测
authors:
- Yu Mao
- Lei Yu
- Zining Zhu
- Yusheng Zheng
- Haohang Li
- Freda Shi
- Yutong Yin
- Zhaoran Wang
- Jingcheng Niu
affiliations:
- University of Toronto
- Stevens Institute of Technology
- University of California, Santa Cruz
- University of Waterloo
- Northwestern University
arxiv_id: '2610.01066'
url: https://arxiv.org/abs/2610.01066
pdf_url: https://arxiv.org/pdf/2610.01066
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM能力探测 · 随机奖励RL探针
tags:
- LLM
- Reinforcement Learning
- Probing
- Spurious Reward
- Reachability
one_liner: 提出随机奖励RL的LLM能力探测框架，揭示训练三阶段规律，解释伪奖励悖论
practical_value: '- 做LLM Agent/生成式推荐的RLHF/GRPO调优前，可先用低成本随机奖励RL做探针，快速判断当前基座的潜在可优化空间，避免在dormant阶段的小模型上浪费真值标注成本

  - 相同初始性能的不同LLM基座可达能力差异可达46.5pp，选基座时不要只看静态评测分数，可复用该框架评估调优天花板，优先选可达性更高的基座降低后续调优成本

  - 垂域LLM（电商商品理解/客服/文案生成）训练时，可基于三阶段规律匹配训练策略：receptive阶段优先用真值奖励训练，进入autodidactic阶段后可减少标注量，用弱监督/半监督即可激活潜在能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
针对伪奖励悖论（随机奖励也能提升LLM性能）的现有解释（RL训练机制、数据污染）无法解释相同初始性能checkpoint调优后性能差异巨大的问题，且传统探针方法存在标签泄露争议，无法区分是探针学到任务还是模型本身具备潜在能力。
### 方法关键点
- 定义**reachability（可达性）**指标，衡量给定训练约束下从当前checkpoint能达到的最高任务性能
- 提出随机奖励RL探针，从理论上证明随机奖励信号不含任何正确性信息，彻底排除标签泄露，可探测模型无需正确性反馈即可激活的潜在能力
- 跨任务验证覆盖算术、代码生成、知识查询三类生成任务，基于OLMo、SmolLM等多个模型系列的全训练周期checkpoint开展实验
### 关键结果
- 实验数据集包含合成GSM算术题、MBPP代码数据集、合成多跳知识库查询数据集
- 揭示LLM训练的三阶段规律：① dormant阶段：真值/随机奖励调优增益均<1pp；② receptive阶段：仅真值奖励有效，算术任务最高增益达79.5pp；③ autodidactic阶段：随机奖励也可有效提升，算术任务最高增益达77.5pp
- 初始准确率均为3.5%的两个OLMo checkpoint，经相同真值奖励RL调优后最高准确率分别为8.5%和55%，差异达46.5pp
> 最值得记住的话：LLM的当前静态性能不等于其潜在可达能力，处于autodidactic阶段的模型仅需明确任务提示即可通过训练大幅激活已有知识，无需正确性反馈。
