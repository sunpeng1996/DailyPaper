---
title: 'PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling'
title_zh: PreSTO：基于预测子树预取的LLM Power采样加速方法
authors:
- Nan Jiang
- Panagiotis Theodoropoulos
- Wei Deng
affiliations:
- University of Texas at El Paso
- Georgia Institute of Technology
- Morgan Stanley
arxiv_id: '2610.13171'
url: https://arxiv.org/abs/2610.13171
pdf_url: https://arxiv.org/pdf/2610.13171
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM推理加速 · Power采样优化
tags:
- Power Sampling
- MCMC
- Inference Acceleration
- Prefetching
- KV Cache
one_liner: 通过预测子树预取加速LLM Power采样，不改变MH采样逻辑且实现最高2.33倍推理速度提升
practical_value: '- 业务中若使用Power采样提升LLM推理/生成效果（如电商商品文案生成、Agent多步推理），可直接接入PreSTO开源框架，无需修改原有MH采样逻辑即可获得1.7x~2.3x的延迟降低，且输出分布完全一致

  - 子树预取+KV cache前缀复用的批处理优化思路，可迁移到生成式推荐的候选序列采样、多步推理Agent的 speculative 执行阶段，降低串行采样的开销

  - 基于轻量分类器预测访问概率、优先分配预算给高概率路径的优化思路，可复用在推荐系统的缓存预取、召回候选集排序阶段，提升资源利用率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Power采样无需额外训练即可让LLM推理效果媲美RL精调，可大幅降低业务侧LLM优化成本，但其核心采样器PowerMH基于Metropolis–Hastings (MH)算法，存在天然串行依赖：每步必须等上一步的accept/reject结果才能生成下一个候选，推理延迟可达普通低温采样的6.5~18.4倍，现有优化方案要么改采样器要么改模型，会破坏原有采样分布一致性，最终影响推理效果。

### 方法关键点
- 将未来MH的accept/reject决策建模为决策树，每次批处理生成预取子树内的所有候选proposal，再按原始MH规则执行路径选择，理论证明不改变原有MH转移核，输出分布完全与基线一致
- 观察到Power采样下MH仅会访问预取子树中稀疏的近一元路径，设计Condition 1筛选可共享前缀的可行预取请求，通过KV cache前缀复用降低批处理额外开销
- 提出预测遍历规则，通过三分类逻辑回归预判断每个节点的𝜖-确定性（大概率接受/拒绝/不确定），用动态规划分配预取预算，最大化每批完成的MH步数

### 关键实验
在7个数据集（MATH500、LCB V6、MBPP、GPQA等）、5个基座LLM上测试，对比PowerMH、EntropyCut、MultiTryMH三个基线，PreSTO实现中位数加速比分别为1.71×、1.91×、2.33×，其中前两个基线的模型调用次数中位数减少3.9×，单调用耗时仅增加2.1×；预测遍历规则相比默认BFS遍历额外带来1.25×~1.37×的加速。

值得记住的一句话：对于串行依赖的采样类算法，无需修改核心逻辑，仅通过预取高概率执行路径+批处理资源复用，即可在不损失效果的前提下实现显著的延迟优化。
