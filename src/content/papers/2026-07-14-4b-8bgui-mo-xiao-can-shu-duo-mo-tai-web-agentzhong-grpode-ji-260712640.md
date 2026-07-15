---
title: 'A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language
  Model Web Agent: A Controlled Null and Its Mechanism'
title_zh: 4B-8B规模小参数多模态Web Agent中GRPO的失效机制研究
authors:
- Chengguang Gan
- Zhixi Cai
- Yunhao Liang
- Hanjun Wei
- Shiwen Ni
- Qinghao Zhang
arxiv_id: '2607.12640'
url: https://arxiv.org/abs/2607.12640
pdf_url: https://arxiv.org/pdf/2607.12640
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 强化学习GRPO优化机制
tags:
- Agent
- GRPO
- Small LLM
- Vision-Language Model
- Reinforcement Learning
one_liner: 揭示4B-8B小参数Web Agent中GRPO的学习率门控失效机制与生效前提
practical_value: '- 小参数Agent做RL优化前，先验证采样策略是否优于基线贪心策略，无优化空间时GRPO不会带来增益，可直接节省算力投入

  - 4B-8B规模Agent做GRPO训练时避免使用中高学习率，文本交互场景下会显著降低任务成功率

  - 设计Agent RL消融实验时可复用论文的控制变量网格（学习率、KL权重、种子、裁剪参数），快速排除pipeline故障导致的阴性结果'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前业界普遍基于监督checkpoint用GRPO等带可验证奖励的RL优化Agent效果，但小参数（4B-8B）多模态Web Agent场景下GRPO的实际增益与失效机制尚不明确。
### 方法关键点
设计18组控制变量消融实验，变量覆盖学习率、KL权重、随机种子、初始化方式、裁剪阈值，覆盖文本、Set-of-Marks截图两种观测输入，对比4B、8B两种规模backbone的效果。
### 关键结果数字
1. 在Agent已基本掌握的任务上，所有配置均无法超过监督基线，中高学习率在文本场景下会显著降低任务成功率；
2. 仅当采样策略成功率高于贪心策略（存在明确优化空间）时，GRPO可带来22个百分点的成功率提升；
3. 中学习率的性能退化可归因于注意力与MLP层，高学习率的性能崩溃无单一可归因模块，4B模型后层有效秩与能力强相关，8B模型无该关联。
