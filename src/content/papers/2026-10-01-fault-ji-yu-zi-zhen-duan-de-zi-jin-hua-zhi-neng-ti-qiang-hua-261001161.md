---
title: 'My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement
  Learning'
title_zh: FAULT：基于自诊断的自进化智能体强化学习信用分配方法
authors:
- Yihua Zhu
- Qianying Liu
- Weixu Qiao
- Xuan Ren
- Weiwei Xu
- Wenbo Li
- Wei Wang
- Ruijia Chen
- Xinmiao Luan
- Yin Luo
affiliations:
- Alibaba Group
- Kyoto University
- NII LLMC
- Peking University
- University of California, Los Angeles
arxiv_id: '2610.01161'
url: https://arxiv.org/abs/2610.01161
pdf_url: https://arxiv.org/pdf/2610.01161
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent强化学习 · 信用分配优化
tags:
- Agentic_RL
- Credit_Assignment
- Self_Diagnosis
- Reinforcement_Learning
- LLM_Agent
one_liner: 提出自诊断引导的终端信用重分配框架，解决长序列智能体强化学习的信用分配痛点
practical_value: '- 电商多步交互Agent（导购、智能下单决策等）训练可复用FAULT信用分配思路，将终端转化（下单/加购）奖励按过程错误（推品错误、问答错误等）拆分到对应步骤，解决全成功/全失败批次无训练信号的问题，大幅提升长路径任务训练效率

  - 做Agent RL训练时，可引入轻量自诊断SFT阶段，让模型学会结构化输出轨迹中的错误类型+对应步骤+证据，无需额外引入昂贵的过程标注，还能提升错误定位准确性

  - 多步推荐/搜索任务（如用户多轮检索后的成交转化优化）可参考错误定价机制，统计不同过程错误（query改写错误、召回错品等）对最终转化的影响权重，针对性优化对应模块'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agentic RL依赖终端奖励训练，存在两个核心信用分配痛点：一是同批次所有轨迹结果相同时（全成功/全失败），GRPO等组归一化方法无有效训练信号，ALFWorld场景下这类批次占比达59%~64%；二是终端奖励无法定位具体错误步骤，长序列任务下梯度信号被严重稀释，训练效率极低。现有自然语言反思类方法输出无结构化，无法直接量化为信用权重，且错误可靠性无验证。

### 方法关键点
- 冷启动阶段：用大模型生成带证据的结构化错误标注，构造固定错误分类体系，通过SFT让模型同时具备任务执行和自诊断能力，初始化不同错误的权重。
- 错误定价：基于历史批次的终端结果，回归拟合不同错误类型对任务成功的影响系数，转化为相对惩罚权重，定期在线更新。
- 信用重分配：将终端奖励的总惩罚预算按错误权重拆分到对应步骤，结合任务级+同上下文状态级的双通道优势计算更新策略；诊断器和策略共享权重但不接收策略梯度，避免模型故意少报错误。

### 关键实验
在ALFWorld、WebShop、搜索QA三个基准上对比GRPO、GiGPO、SEED等基线：ALFWorld场景下训练信号覆盖率达95%（GRPO仅41%、GiGPO仅72%），错误步骤MRR达0.494（GiGPO仅0.303）；4B参数下ALFWorld成功率91.0%、WebShop得分88.5，均领先基线，且任务序列越长增益越显著。

### 核心结论
长路径Agent RL优化的核心痛点不在奖励设计，而在如何把终端可信信号精准分配到过程中的对应决策步骤，自诊断是低成本实现细粒度信用分配的可行路径
