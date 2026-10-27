---
title: 'ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic
  Reinforcement Learning'
title_zh: ProAS：面向多轮智能体强化学习的进度感知优势塑造框架
authors:
- Bowen Ding
- Mingda Wan
- Yuhan Chen
- Jiyao Yuan
- Qi Zhu
- Futing Wang
- Heyuan Deng
- Fei Mi
- Lifeng Shang
- Tao Lin
affiliations:
- Zhejiang University
- Westlake University
- Westlake Institute for Advanced Study
- Huawei Noah’s Ark Lab
arxiv_id: '2610.18683'
url: https://arxiv.org/abs/2610.18683
pdf_url: https://arxiv.org/pdf/2610.18683
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 多轮训练信用分配优化
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- GRPO
- Advantage Shaping
one_liner: 无额外critic开销的即插即用优势塑造框架，解决critic-free RL均匀信用分配问题，提升多轮Agent训练效率与性能
practical_value: '- 电商导购Agent、多轮搜索Agent训练可直接将ProAS接入现有GRPO/DAPO等critic-free RL pipeline，无需额外训练critic，即可提升任务成功率、降低训练成本

  - 可复用ARG设计思路：将电商多轮交互的成功路径（如搜索→筛选→加购→下单）抽象为动态更新的DAG子目标序列，自动标注动作合理性与进度贡献，无需稠密人工标注

  - 多轮任务RL遇到均匀信用分配问题时，可直接复用MUI+APR逻辑：正样本轨迹屏蔽无效动作的激励，负样本轨迹按Future-Drift（下游无效动作数）加权分配惩罚，效果优于简单掩码或位置加权

  - 若缺少黄金标注轨迹，可先用大模型蒸馏生成成功路径构建初始ARG，搭配动态更新机制即可获得显著收益，大幅降低标注门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent多轮训练主流采用GRPO等无critic的RL算法，存在**均匀信用分配困境**：正优势轨迹中的不合理动作会被误强化，负优势轨迹中所有动作被无差别惩罚，完全忽略不同动作的下游影响；而带critic的RL算法又存在计算开销大、长序列优化不稳定的问题，亟需无额外开销的细粒度信用分配方案。
### 方法关键点
- 动态更新的**Agentic Reference Graph (ARG)**：将任务进度抽象为有序子目标构成的DAG，从训练过程中产生的成功轨迹持续增量更新节点（子目标状态）和边（合法动作转移），自动标注每个动作的合理性（是否符合合法转移）和进度推进性（是否推进到新子目标且无冗余）
- 两个核心优势塑造机制：1）**Masking Unreasonable Incentives (MUI)**：正优势轨迹中，不合理动作的优势置0，避免误强化；2）**Asymmetric Penalty Redistribution (APR)**：负优势轨迹中，按每个动作的Future-Drift（下游非推进动作的总数）加权分配惩罚，越早期引发后续无效操作的动作惩罚越重
- 完全即插即用，无需修改原有RL算法核心逻辑，无额外critic训练开销
### 关键实验
在ALFWorld（家居具身任务）、WebShop（电商购物Agent任务）上基于Qwen2.5-1.5B/7B-Instruct验证，对比GRPO、DAPO、GiGPO、MiGPO等SOTA RL算法：
1. 性能提升：GiGPO+ProAS在ALFWorld上最高达94.3%成功率，超SOTA MiGPO 2.4个点、超GPT-5.6-Sol 15.4个点；在WebShop上最高达70.8%成功率，超MiGPO 13.1个点
2. 收敛加速：训练收敛速度最高提升2.44倍，平均提升1.5~2.2倍
3. 鲁棒性：即使ARG残缺40%、或用大模型蒸馏生成ARG，依然能获得显著收益，仅比完美ARG低3~4个点

> 最值得记住的一句话：无critic的RL算法优化无需新增额外模型，仅通过基于任务进度结构的优势塑造，就能同时实现性能提升和收敛加速
