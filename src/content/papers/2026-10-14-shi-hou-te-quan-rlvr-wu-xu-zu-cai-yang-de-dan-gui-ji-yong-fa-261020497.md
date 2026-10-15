---
title: 'Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling'
title_zh: 事后特权RLVR：无需组采样的单轨迹Token信用分配方法
authors:
- Wei Chen
- Yubing Wu
- Zhou Xu
- Haoyue Zhang
- Delu Zeng
- Jiahao Wang
- Junmei Yang
- Pan tiewen
- Jingfeng Liu
- Zhiheng Zhou
affiliations:
- South China University of Technology
- Tsinghua University
- The Hong Kong University of Science and Technology
- Huawei 2012 Laboratories
- Shenzhen Technology University
arxiv_id: '2610.20497'
url: https://arxiv.org/abs/2610.20497
pdf_url: https://arxiv.org/pdf/2610.20497
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: LLM强化训练 · 信用分配优化
tags:
- RL
- GRPO
- Credit Assignment
- LLM Training
- RLVR
one_liner: 提出无需组采样的单轨迹RL训练方法HP-RLVR，训练速度比GRPO最高提升2.3倍
practical_value: '- 做电商导购Agent、推荐理由生成、搜索query改写的RL优化时，可直接用HP-RLVR替代GRPO，将每个prompt的rollout数从8降到1，大幅降低训练算力成本

  - Token级信用分配逻辑可复用：用因果上下文和事后上下文的归一化JSD作为token权重，无需额外学习critic或过程标注，适合只有终端验证信号的业务场景（如推荐文案转化奖励分配）

  - 可用历史平均奖励作为基线替代组内相对基线，避免组内结果全同时梯度为0的问题，适配业务中reward分布偏平的场景（如大部分推荐文案点击率相近）'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR基于终端验证奖励训练LLM，但现有组相对方法（如GRPO）需要每个prompt采样多个轨迹，采样成本高，且组内结果全同时会丢失梯度信号；同时全局奖励分配到token的粒度过粗，过程标注成本又过高，亟需更高效的单轨迹信用分配方案。

### 方法关键点
- 单轨迹采样：每个prompt仅需1次rollout，无需组采样
- 双视角打分：冻结生成策略快照，分别基于因果历史（生成时可见上下文）、事后上下文（真实生成未来+验证器反馈）对每个token位置的词表分布打分
- 信用分配：用两个分布的归一化JSD作为token权重，乘以基于历史平均奖励的中心化reward得到token级优势，权重范围[0,1]，无需学习critic或参考解
- 训练目标：基于PPO surrogate优化，轨迹级平衡损失避免长样本权重过高

### 关键实验
基于Qwen3 1.7B/4B/8B模型，对比G=8的GRPO，在数学、代码生成、ALFWorld三个任务测试：8B模型上HP-RLVR训练速度比GRPO分别快1.21倍（数学）、1.46倍（代码）、2.30倍（ALFWorld），rollout数仅为GRPO的1/8；数学任务准确率全面优于GRPO，8B模型Avg@12达65.73% vs GRPO的63.07%；ALFWorld任务中4B、8B GRPO分别有43.2%、49.0%的梯度记录为0，HP-RLVR无零梯度记录。

**最值得记住的一句话**：单轨迹RL训练的核心是用事后上下文作为训练特权信息，既能大幅降低采样成本，又能避免组相对方法的梯度消失问题。
