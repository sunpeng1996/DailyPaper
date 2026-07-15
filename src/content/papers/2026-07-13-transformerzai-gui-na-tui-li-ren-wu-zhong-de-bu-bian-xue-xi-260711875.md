---
title: Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks
title_zh: Transformer在归纳推理任务中的不变学习动力学
authors:
- Tiberiu Musat
- Tiago Pimentel
- Nicholas Zucchet
- Thomas Hofmann
affiliations:
- ETH Zurich
- Stanford
arxiv_id: '2607.11875'
url: https://arxiv.org/abs/2607.11875
pdf_url: https://arxiv.org/pdf/2607.11875
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: Transformer 归纳推理学习动力学理论研究
tags:
- Transformer
- Inductive Reasoning
- Learning Dynamics
- Invariant Manifold
- In-Context Learning
one_liner: 提出理论框架证明Transformer归纳推理训练动力学受限于低维可解释不变流形，可支撑训练过程与电路检测分析
practical_value: '- 可基于低维不变流形思路简化LLM4Rec模型训练分析流程，无需遍历全量参数即可定位核心生效的推理电路

  - 微调LLM用于推荐/Agent任务时，可参考数据统计对in-context/in-weights学习的影响规律，定向引导业务所需推理能力涌现

  - 多跳推理类电商导购Agent训练时，可复用流形坐标框架自动检测已习得的推理电路，降低可解释性分析成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Transformer学习动力学研究多绑定特定任务，缺乏通用框架解释归纳推理能力涌现机制，LLM技能习得过程不可预测，阻碍模型优化与安全管控。
### 方法关键点
1. 提出统一的广义归纳任务类别，覆盖上下文n-gram、多跳推理等常见合成任务
2. 理论证明注意力模型训练动力学可被约束在低维可解释不变流形内，仅需少量可解释坐标即可刻画训练过程，无需依赖百万级参数分析
3. 配套流形坐标框架可自动检测训练模型习得的推理电路，可分析数据统计、随机初始化对学习路径的调控规律
### 关键结果
证明Transformer归纳推理训练轨迹始终落在低维不变流形内，可将电路形成过程降维为低维动力学现象，为构建可预测的Transformer训练理论提供核心支撑
