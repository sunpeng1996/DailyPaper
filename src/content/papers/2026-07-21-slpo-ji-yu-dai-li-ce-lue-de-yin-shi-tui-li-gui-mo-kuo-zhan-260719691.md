---
title: 'SLPO: Scaling Latent Reasoning via a Surrogate Policy'
title_zh: SLPO：基于代理策略的隐式推理规模扩展方法
authors:
- Runyang You
- Zhiyuan Liu
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Sichuan University
arxiv_id: '2607.19691'
url: https://arxiv.org/abs/2607.19691
pdf_url: https://arxiv.org/pdf/2607.19691
published: '2026-07-21'
collected: '2026-07-23'
category: Reasoning
direction: 大语言模型 · 隐式推理RL优化
tags:
- Latent Reasoning
- Reinforcement Learning
- Policy Optimization
- Test-time Scaling
- SLPO
one_liner: 提出代理隐式策略优化SLPO，将结果奖励RL引入自回归隐式推理，实现隐式测试时规模扩展
practical_value: '- 隐式推理RL优化思路可迁移到生成式推荐的Semantic ID序列推理场景，用代理似然替代离散token概率做credit
  assignment，大幅降低推理token开销

  - 带正确性冷启动的自适应停止头设计可复用到推荐/广告多步推理Agent中，根据请求难度动态分配计算资源，平衡效果和推理耗时

  - 连续向量空间的策略梯度构造方法可借鉴到用户行为序列隐式表征优化任务，无需映射到离散语义空间就能做端到端奖励优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
显式CoT推理的测试时规模扩展依赖结果奖励RL，但每一步都要解码为自然语言token，计算成本极高；隐式推理用连续向量做中间计算，效率远高于显式CoT，但长期受限于模仿学习，无法用结果奖励RL做优化——核心瓶颈是隐式轨迹没有可计算的每一步似然，也没有自适应停止接口，固定推理预算无法适配不同难度任务。

### 方法关键点
- 构造代理隐式策略密度：通过K次带MC dropout的前向传播，拟合隐状态转移的对角高斯分布作为代理似然，替代离散token的词汇分布概率，实现连续隐空间的策略梯度credit assignment
- 设计正确性监督的停止头冷启动：先枚举不同推理长度的结果正确性，监督停止头学习何时终止推理，再通过RL联合优化隐式推理策略和停止决策，实现可变推理长度的自适应计算
- 兼容RLOO、GRPO等多种现有RL优化算法，无需修改隐式推理主干架构，可直接接入现有公开的隐式推理checkpoint

### 关键实验
在GSM8K、GSM-Hard、MultiArith等数学推理数据集上测试，适配COCONUT、CODI等多种隐式推理主干，相比基线，Llama-3.2-1B+CODI+SLPO的Pass@16最高提升2.8个百分点，难度越高的任务收益越显著，同时可根据任务难度动态分配推理长度，难例推理长度平均提升17.8%。

最值得记住的一句话：连续隐空间的推理优化不需要强行映射回离散token空间，通过构造代理似然就能复用成熟的RL优化范式，同时兼顾推理效率和效果。
