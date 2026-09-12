---
title: 'GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game
  to Static Dataflow and CUDA Graph Replay'
title_zh: GPU-CFR：通过静态数据流编译与CUDA Graph重放实现80倍速CFR
authors:
- Boning Li
- Longbo Huang
affiliations:
- Institute for Interdisciplinary Information Sciences, Tsinghua University
arxiv_id: '2609.11923'
url: https://arxiv.org/abs/2609.11923
pdf_url: https://arxiv.org/pdf/2609.11923
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 大规模博弈训练 · GPU加速优化
tags:
- CFR
- GPU Acceleration
- CUDA Graph
- Static Dataflow
- Game Theory
one_liner: 提出静态数据流编译+CUDA Graph重放的GPU-CFR框架，将CFR运算速度最高提升80倍
practical_value: '- 对固定逻辑的迭代类任务（如推荐反事实归因、多智能体竞价策略训练），可复用「一次预编译静态数据流+运行时重放」架构，大幅降低kernel
  launch开销

  - GPU上存在大量小核调用的场景，优先用CUDA Graph Replay合并单次迭代的所有内核调用，仅一次启动即可完成整轮迭代，显著降低调度开销

  - 多步依赖的树状运算可提前做静态展开、层级批处理，裁剪框架调度操作数，即使无GPU在CPU端也能获得数倍性能收益'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统CFR算法存在大量小颗粒度、相互依赖的gather/scatter操作，GPU实现的核函数启动与框架调度开销占比极高，性能反而低于优化后的CPU版本。
### 方法关键点
1. 利用固定游戏的CFR迭代除数值外运算逻辑完全固定的特性，一次性将游戏编译为静态数据流，预计算索引、层级批处理执行序列，仅迭代间更新求解器状态
2. 采用静态机会折叠、层级执行块、双路可达缓冲区裁剪18.1倍框架操作数
3. 用CUDA Graph Replay一次性记录迭代逻辑，单次图启动即可重放整轮迭代
### 关键结果
单A100上相比最优GPU CFR实现提速29.8~80.4倍，相比最优CPU实现LiteEFG在4个最大游戏上提速14~258倍；仅编译后的CPU版本也比原有GPU基线快2.2~51.1倍，首次求解即可覆盖编译与图捕获开销。
