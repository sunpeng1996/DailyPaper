---
title: Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning
title_zh: 面向高精度高效长时程规划的并行预测世界模型
authors:
- Wanjin Feng
- Baobin Zhang
- Ao Yu
- Shibo Feng
- Xi Wang
- Xingyu Gao
affiliations:
- Tsinghua University
- Institute of Microelectronics, Chinese Academy of Sciences
- The Hong Kong University of Science and Technology (Guangzhou)
- Nanyang Technological University, Singapore
arxiv_id: '2610.08627'
url: https://arxiv.org/abs/2610.08627
pdf_url: https://arxiv.org/pdf/2610.08627
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent世界模型 · 长时程并行规划
tags:
- WorldModel
- LongHorizonPlanning
- ParallelPrediction
- CausalTransformer
- ModelBasedRL
one_liner: 提出并行预测世界模型PPWM，消除自回归误差累积，长时程规划精度与效率双提升
practical_value: '- 长序列预测场景（如用户长期行为预测、广告投放长期效果预估）可复用PPWM架构替换自回归预测，既消除递归误差累积提升长时程预测精度，又能通过并行计算降低推理延迟

  - 因果前缀编码+未来隐表征交互的结构可迁移到GenRec/序列推荐任务：例如用户未来N步点击序列生成，给每个预测位构造对应历史行为+动作前缀表征，再通过因果Transformer做并行交互，兼顾因果性与推理效率

  - 多锚点自条件滚动（MAR）训练思路可解决长序列预测的训练/推理分布 mismatch 问题：当预测长度超过模型单次并行窗口时，用随机锚点+梯度截断的自监督训练，无需全序列标注即可提升长序列泛化性

  - 轨迹级联合优化方法可复用在多步规划类业务：例如电商多触点投放规划、推荐序列重排，直接对全序列目标做端到端优化，无需逐步传播梯度，提升优化效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统世界模型长时程规划依赖逐状态自回归滚动预测，存在两个核心痛点：一是预测误差随步长递归累积，精度随规划 horizon 提升快速下降；二是串行计算导致规划延迟随步长线性增长，无法满足高实时性要求的Agent决策场景。现有并行预测方案为了消除递归依赖，又放弃了未来表征间的因果交互，长时程预测精度不足。
### 方法关键点
- 核心架构：替换逐状态自回归递归逻辑，单次前向即可并行输出固定窗口K步的未来轨迹，每步预测仅依赖对应的因果动作前缀，彻底消除解码后状态的反馈路径
- 因果轨迹构造：每个预测步的query融合当前上下文、位置编码与动作前缀表征后，通过多层因果Transformer做未来表征的单向交互，在隐空间保留时序依赖关系
- 长序列适配：训练阶段引入多锚点自条件滚动（MAR）损失，随机选择锚点用截断梯度的预测上下文做监督，解决长于K步的序列预测时训练/推理分布不匹配问题
### 关键实验
在OGBench-Cube、Push-T、Two-Room、Reacher四个视觉控制任务上对比LeWM、Fast-LeWM、TD-MPC2等基线：① 所有任务、所有步长的长时程预测MSE均为最低，Reacher任务15步预测MSE相比Fast-LeWM降低98%；② 搭配CEM规划器时4个任务开环成功率均为最高，平均规划延迟相比自回归LeWM降低3.3倍；③ 架构可迁移到DINO-WM backbone，20步预测误差相比原生自回归DINO-WM降低36.45%。
### 核心结论
长时程时序预测无需强制逐状态自回归，通过并行因果轨迹预测即可同时实现精度与效率的双重提升。
