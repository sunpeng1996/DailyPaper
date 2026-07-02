---
title: 'QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling'
title_zh: QuasiMoTTo：基于拟蒙特卡洛的大模型测试时计算缩放方法
authors:
- Michael Y. Li
- Anthony Zhan
- Kanishk Gandhi
- Noah D. Goodman
- Emily B. Fox
affiliations:
- Stanford University
arxiv_id: '2607.01179'
url: https://arxiv.org/abs/2607.01179
pdf_url: https://arxiv.org/pdf/2607.01179
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 大模型采样优化 · 测试时计算缩放
tags:
- QMC
- LLM Sampling
- Test-Time Scaling
- GRPO
- Sample Efficiency
one_liner: 用拟蒙特卡洛生成无偏相关LLM采样，推理和RL训练样本效率提升25%到50%
practical_value: '- 推理侧多候选生成场景（如Agent多路径规划、生成式推荐多Item候选、Query改写多候选）可直接替换i.i.d采样为QuasiMoTTo的lattice采样，零额外成本减少25%-47%的采样量，相同候选数下覆盖更多解空间，提升召回率

  - 做LLM/GenRec的RLHF/GRPO训练时，替换原有i.i.d采样为QuasiMoTTo采样，可减少50%左右的训练步数，同时降低零方差组比例，提升每批次有效学习信号，降低训练成本

  - 业务中需要评估pass@k指标的场景（如生成结果正确性校验、多候选选优），可复用论文提出的dyadic bootstrap无偏评估器，解决相关采样下传统pass@k指标失效问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型通过并行生成多份独立样本提升推理效果（如pass@k）、为RL训练提供梯度信号的方案，存在严重的计算冗余：独立采样容易重复生成高概率区域的相似结果，推理侧浪费算力，RL训练侧易出现同批次所有样本奖励相同的零方差组，无有效梯度信号。现有提升采样多样性的方法要么破坏模型输出的边缘分布无偏性，无法兼容RL等需要无偏估计的场景，要么无法完全并行，损失吞吐量。

### 方法关键点
- 基于算术采样将自回归生成重参数化为逆CDF采样流程，用拟蒙特卡洛（QMC）生成低差异均匀输入替代i.i.d均匀输入，生成的样本相关性更高、输出空间覆盖更均匀，且每个样本的边缘分布完全符合原LM输出分布，可作为i.i.d采样的drop-in替换，无适配成本。
- 提供三种QMC实现：lattice（网格随机偏移）、stratified（分层采样）、token-level Sobol（序列维度Sobol序列），全部支持完全并行生成，单样本额外开销可忽略。
- 针对相关采样下传统pass@k评估失效问题，提出dyadic bootstrap无偏评估器，兼容三种QMC采样方案。

### 关键结果
在Countdown、Maze、Sudoku、1D-ARC四个符号推理基准上测试，对比i.i.d采样，lattice版本QuasiMoTTo达到相同pass@k可减少25%-47%的样本量，效果接近边际保留采样的理论上限；在GRPO RL训练场景，达到相同pass@1指标可减少50%的训练步数，零方差组占比显著降低。

最值得记住的一句话：不需要修改模型结构、训练目标或推理逻辑，仅通过优化采样的联合分布，就能在保证输出无偏的前提下，获得最高近50%的推理/训练样本效率提升，是几乎零成本的性能增益
