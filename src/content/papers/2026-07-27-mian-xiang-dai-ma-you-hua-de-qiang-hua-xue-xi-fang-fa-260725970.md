---
title: Reinforcement Learning for Code Optimization
title_zh: 面向代码优化的强化学习方法
authors:
- Pierre Chambon
- Kunhao Zheng
- Juliette Decugis
- Benoit Sagot
- Gabriel Synnaeve
affiliations:
- FAIR at Meta
- Inria
- Université Paris Dauphine
arxiv_id: '2607.25970'
url: https://arxiv.org/abs/2607.25970
pdf_url: https://arxiv.org/pdf/2607.25970
published: '2026-07-27'
collected: '2026-07-30'
category: Other
direction: 代码优化 · 强化学习训练
tags:
- Reinforcement Learning
- Code Optimization
- GRPO
- Reward Design
- Benchmark
one_liner: 通过测试校准、多维度奖励设计、适配GRPO训练三阶段，解决代码优化RL的噪声、稀疏、不稳定问题，提升生成代码运行效率
practical_value: '- 涉及RL优化的业务场景（如广告出价、推荐排序动态调优）可复用多目标奖励校准方法，同时兼顾核心约束目标与优化目标，避免有效信号被噪声淹没

  - 当RL训练出现奖励稀疏、信号不稳定问题时，可借鉴离线预筛高潜力配置的思路，降低在线训练开销，提升训练收敛稳定性

  - 面向低延迟需求的大模型推理优化场景，可参考其校准测试沙箱的思路，构建一致的性能评估环境，减少测量噪声对优化效果的干扰'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有面向代码正确性的RL训练方案已成熟，但直接将执行时间加入奖励做代码优化时，测量噪声、奖励稀疏、GRPO训练不稳定问题会导致有效信号被淹没，生成代码速度提升有限且准确率下降。
### 方法关键点
提出三阶段优化框架：1. 构建DMC-Optim大规模优化测试集与校准沙箱，统一测试环境减少测量噪声；2. 融合正确性与速度指标构建奖励函数，搭配离线模拟器预筛高潜力训练配置，缓解奖励稀疏问题；3. 适配GRPO训练与评估流程，适配稀疏、带噪声的计时执行场景。
### 关键结果
在DMC-Optim上，最优配置将Qwen2.5 7B的严格top-50% pass@1从18.0%提升至31.3%，CWM 32B从30.7%提升至50.4%；top-30%场景下CWM 32B相对提升125%且不损失正确性得分；沙箱环境降级时比标准RLVR提升100%-200%；LCB数据集上CWM 32B在中位样本速度对比中83%优于标准RLVR，复杂度优化效率达到人类水平的50%。
