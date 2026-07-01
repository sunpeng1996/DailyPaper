---
title: 'TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning'
title_zh: TRIAGE：面向智能体强化学习的角色类型信用分配框架
authors:
- Yuanda Xu
- Zhengze Zhou
- Hejian Sang
- Xiaomin Li
- Jiaxin Zhang
- Xinchen Du
- Zhipeng Wang
- Alborz Geramifard
affiliations:
- LinkedIn Corporation
- Harvard University
- Johns Hopkins University
arxiv_id: '2606.32017'
url: https://arxiv.org/abs/2606.32017
pdf_url: https://arxiv.org/pdf/2606.32017
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 智能体强化学习 · 信用分配优化
tags:
- GRPO
- Credit Assignment
- Agentic RL
- LLM-as-Judge
- Process Reward
one_liner: 在GRPO基础上引入语义角色分类的分段信用分配，显著提升多场景Agent任务成功率
practical_value: '- 电商导购Agent、搜索工具调用Agent训练时，可直接复用四角色分类体系对用户交互动作（搜索/点击/加购/重复操作）做分层信用分配，避免成功轨迹的冗余操作被强化、失败轨迹的有效探索被惩罚

  - 不需要训练定制化过程奖励模型，用轻量结构化LLM judge做角色分类+固定规则映射奖励的方案，实现成本极低，可快速嵌入现有GRPO训练管线

  - 优化电商多步转化任务时，可复用框架的回归惩罚机制，抑制成功路径中的重复点击、无效跳转等冗余操作，实验显示可降低14.8%的交互步数，同时提升转化成功率

  - 角色分类judge无需大模型，带thinking能力的8B模型即可达到接近32B模型的效果，推理成本低，适合规模化落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有GRPO将最终验证结果作为全轨迹所有动作token的统一优势信号，存在两个结构性缺陷：失败轨迹中的有效探索会被连带惩罚，成功轨迹中的冗余/回归操作会被错误强化，导致Agent训练时容易抑制必要的信息收集动作、保留无效操作，在多步交互的电商导购、搜索QA、具身任务中表现受限。

### 方法关键点
- 定义四角色分段分类体系：将每个环境交互段分为决定性进展（如下单、提交答案）、有效探索（如搜索商品、查看详情）、无进展操作（如重复点击已选属性）、回归操作（如错误加购、误跳转）四类
- 用结构化LLM judge作为角色分类器，仅输入分段的前后5步上下文，不需要访问最终结果，输出角色标签
- 角色到奖励采用固定规则映射（(1,0.5,-0.1,-0.5)），和原GRPO的轨迹级优势加权融合后作为分段优势，核心优化方向仍由最终结果保证，仅用角色信号修正局部信用
- 理论证明角色条件信用是仅用角色标签能得到的MSE最优分段修正，只要judge可靠就能降低优势估计误差、减少策略梯度方差

### 关键实验结果
在ALFWorld、Search-QA、WebShop三个基准测试，对比GRPO、PPO、GiGPO、共享骨干价值基线等方法：
- Qwen2.5-7B模型上，ALFWorld成功率从79.6%提升到87.5%，Search-QA从43.3%提升到48.1%，WebShop从70.1%提升到77.2%
- Qwen3-1.7B小模型上，WebShop成功率从37.5%提升到55.9%，增益达18.4个点
- 成功轨迹的交互步数相对GRPO降低10.4%（ALFWorld）~14.8%（WebShop）
- 消融实验表明回归惩罚是核心增益来源，贡献60%以上效果提升，探索奖励提供稳定次要增益

最值得记住的一句话：Agent训练的信用分配不能仅依赖最终结果，给交互动作增加语义角色维度的分层奖励，以极低额外成本即可大幅提升多步任务的性能与效率
