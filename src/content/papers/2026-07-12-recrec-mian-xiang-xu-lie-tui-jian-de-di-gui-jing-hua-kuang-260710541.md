---
title: 'RecRec: Recursive Refinement for Sequential Recommendation'
title_zh: RecRec：面向序列推荐的递归精化框架
authors:
- Pervez Shaik
- Prosenjit Biswas
- Abhinav Thorat
- Ravi Kolla
- Niranjan Pedanekar
affiliations:
- Sony Research India
arxiv_id: '2607.10541'
url: https://arxiv.org/abs/2607.10541
pdf_url: https://arxiv.org/pdf/2607.10541
published: '2026-07-12'
collected: '2026-07-14'
category: RecSys
direction: 序列推荐 · 递归偏好建模
tags:
- Sequential Recommendation
- Recursive Modeling
- Latent Representation
- Parameter Efficiency
- Preference Modeling
one_liner: 轻量递归精化序列推荐模型，带证据锚定校正门防漂移，3.9M-14M参数即超主流SOTA
practical_value: '- 可直接复用证据锚定校正门设计：在迭代式用户偏好建模、多步推理的Rec/Agent场景中，加入锚定原始交互上下文的门控，大幅降低语义漂移风险，新增参数量可忽略

  - 递归精化替代加深模型架构的思路：算力有限的场景下，无需盲目堆叠Transformer层/扩大模型规模，用共享参数的递归模块做多步偏好精化，参数效率可提升90%以上

  - 工程落地参考：训练时加入每步递归的深度监督，解决递归模块的梯度消失问题；同时可根据业务 latency 要求动态调整递归步数，在性能和耗时之间做灵活权衡

  - 小参数模型优化方向：对比7B级LLM4Rec，仅用3.9M参数就能达到相当甚至更优的序列推荐效果，适合端侧推荐、低算力部署的业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐方案分为两类：一类采用单步编码交互序列的架构，依赖加深模型层数、扩大参数规模提升效果，缺乏迭代校正偏好表示的机制，易出现推理偏差；另一类基于LLM做多步推理，效果好但推理/训练成本极高，难以落地到高并发的线上推荐场景，亟需兼顾效果、参数效率和部署成本的新方案。
### 方法关键点
- 将用户偏好建模为可迭代更新的持久隐状态，通过共享参数的递归模块做多步精化，替代单步编码生成的固定偏好表示
- 引入证据锚定校正门，每步递归更新时自适应插值原始交互上下文和精化后的隐状态，从机制上避免递归过程的语义漂移
- 训练时采用深度监督，每一步递归输出的偏好表示都直接参与交叉熵损失计算，解决递归模块梯度消失问题，加速模型收敛
### 关键实验结果
在Luxury Beauty、Video Games、Steam Games三个公开电商/游戏数据集上测试：
- 参数量仅3.9M~14M，比传统SOTA（ReaRec等）参数少22%以上，比7B级LLM4Rec基线小99%，性能全面领先；Steam数据集上HR@1达0.59，比ReaRec高8.6%，与7B级TallRec效果相当
- 训练效率比7B级LLM4Rec高98%以上，Video Games数据集训练仅需210分钟，远低于LLM基线的上万分钟
- 消融实验显示移除校正门后HR@1下降22%，是性能提升的核心贡献组件
### 核心结论
与其盲目堆叠模型深度或扩大参数规模，轻量化的递归精化+原始上下文锚定的设计，能以极低的成本实现序列推荐的效果与效率的双重提升
