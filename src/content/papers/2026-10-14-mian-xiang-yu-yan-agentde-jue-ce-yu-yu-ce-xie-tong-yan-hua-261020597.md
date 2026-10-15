---
title: Co-Evolving Acting and Forecasting for Language Agents
title_zh: 面向语言Agent的决策与预测协同演化训练框架COPE
authors:
- Haofei Yu
- Yixing Chen
- Yining Zhao
- Xuyan Ye
- Yuxiang Liu
- Zhigang Hua
- Yan Xie
- Shuang Yang
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- University of California San Diego
- Meta AI
arxiv_id: '2610.20597'
url: https://arxiv.org/abs/2610.20597
pdf_url: https://arxiv.org/pdf/2610.20597
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: 语言Agent · 样本高效强化学习
tags:
- LLM Agent
- Reinforcement Learning
- GRPO
- Sample Efficiency
- Action Forecasting
one_liner: 在GRPO基础上添加成功轨迹多步动作预测损失，单骨干无推理开销，大幅提升Agent训练样本效率
practical_value: '- 电商导购/客服Agent的RL训练可直接复用COPE思路：在GRPO基础上增加成功轨迹的多步动作预测辅助损失，无需额外模型、推理完全无开销，能直接提样本效率与效果

  - 辅助损失归一化Trick可直接落地：按每组成功轨迹数平均预测损失，避免训练后期成功样本增多导致梯度失衡，大幅提升训练稳定性

  - 动作短、观测长且噪的场景（如电商网页交互Agent、APP操作Agent），优先选择动作预测而非观测预测作为辅助目标，避免无效token占用训练算力，投入产出比更高

  - 超参数可直接参考官方设置：预测窗口K=2，损失权重λ=1e-2，在多数场景下能稳定超过baseline，无需大量调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前长 Horizon 语言Agent的RL训练依赖大量轨迹交互，成本极高；标准GRPO仅用终端稀疏奖励，中间步骤的监督信号完全浪费。此前的两类辅助目标均有缺陷：value目标所有步骤共享同一个终端奖励信号，和单步决策关联弱；observation预测目标是长且噪的网页、终端日志等，仅覆盖单步，训练效率极低。

### 方法关键点
- 单LLM骨干同时承担决策与多步动作预测两个任务，推理时仅用决策分支，完全无额外开销
- 仅在成功的on-policy轨迹上构造监督：从当前历史直接预测后续K步动作，跳过中间观测，目标直接从成功轨迹读取，无需建模环境动态
- 总损失为GRPO损失加λ加权的动作预测损失，预测损失按每组内成功轨迹数归一化，避免训练过程中梯度权重失衡
- 多步预测让每个动作被K个前置历史监督，形成隐式时序集成，强化策略的多步规划能力

### 关键结果
在ALFWorld、ScienceWorld、WebShop、τ2-bench、AppWorld5个基准测试，对比GRPO、ECHO、RWML等基线：1. 整体性能超过所有RL基线，WebShop成功率从64.5%提升到77%，ScienceWorld成功率从64.5%提升到72.5%，AppWorld正常难度成功率从41.7%提升到55.4%；2. 样本效率最高比GRPO高2倍、比ECHO高1.9倍；3. 训练仅增加11%单步计算时间，总端到端时间反而因轨迹变短减少9%，推理零开销。

最值得记住的一句话：对于长 Horizon 语言Agent训练，利用成功轨迹的多步动作做辅助监督，比预测噪声大的观测信号性价比高得多，且完全不增加推理成本。
