---
title: Training Parallel Speculative Draft Models by Directly Minimizing Expected
  Decoding Rounds
title_zh: 直接最小化预期解码轮次的并行投机草稿模型训练方法
authors:
- Yunxiao Zhao
- Changxiao Cai
affiliations:
- University of Michigan, Ann Arbor
arxiv_id: '2610.10411'
url: https://arxiv.org/abs/2610.10411
pdf_url: https://arxiv.org/pdf/2610.10411
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM投机解码 · 草稿模型训练优化
tags:
- Speculative Decoding
- Draft Model
- LLM Inference Acceleration
- Training Objective
- Markov Reward Process
one_liner: 提出无超参数EDR全局训练目标，优化并行投机解码草稿模型，提升LLM推理效率
practical_value: '- 电商场景下用LLM生成商品文案、推荐理由、智能客服回复时，可复用EDR目标训练轻量草稿模型，在完全保留生成质量的前提下降低推理延迟，提升高并发流量下的系统响应速度

  - 可直接复用论文提出的离线评估方法，无需在线运行投机解码流程即可对比不同草稿模型的解码效率，大幅降低多模型选型的评估资源消耗

  - 做LLM序列生成类任务的效率优化时，可参考将全局效率目标建模为Markov Reward Process、用TD梯度做无偏优化的思路，替代局部 surrogate
  目标获得更优的全局性能'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM自回归推理延迟随序列长度线性增长，是高并发场景下的核心瓶颈。投机解码通过轻量草稿模型生成多token候选、大模型单次并行验证的方式实现无损提速，但现有并行/半自回归草稿模型的训练目标均为块级局部替代指标，忽略解码轮次间的依赖关系，无法直接优化全局解码效率，导致实际提速效果无法达到最优。
### 方法关键点
- 将投机解码过程建模为以目标模型输出为条件的Markov Reward Process，推导得出与预期解码轮次完全等价的EDR（Expected Decoding Rounds）目标，无额外超参数
- 推导时序差分（TD）形式的无偏梯度，仅需通过目标模型rollout生成的样本即可完成训练，无需反向传播通过状态递推过程，计算开销可控
- 提出基于目标模型rollout的离线评估器，可在相同样本集上对多个草稿模型做无偏对比，无需在线运行投机解码流程
### 关键实验
在9个覆盖数学推理、代码生成、对话的基准数据集上测试，基于Qwen3-4B+DSpark、Qwen3-8B+DFly两个SOTA投机解码组合做1轮微调，对比块级E2E baseline，EDR在所有数据集上的MAL（平均接受长度）均更高或持平，对话类任务MAL提升幅度最高达2.2%，全程无需修改模型架构与推理逻辑。
### 核心结论
优化序列生成类任务的效率时，局部块级最优往往不等于全局效率最优，通过MRP建模跨步依赖、直接优化最终业务目标（如延迟、解码轮次）可获得更优的实际收益。
