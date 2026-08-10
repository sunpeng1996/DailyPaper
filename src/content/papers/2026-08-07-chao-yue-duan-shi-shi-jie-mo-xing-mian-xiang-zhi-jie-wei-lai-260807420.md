---
title: 'Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future
  Prediction'
title_zh: 超越短视世界模型：面向直接未来预测的长序列端到端训练
authors:
- Xinyi Li
- Zaishuo Xia
- Chenjie Hao
- Yubei Chen
affiliations:
- University of California, Davis
arxiv_id: '2608.07420'
url: https://arxiv.org/abs/2608.07420
pdf_url: https://arxiv.org/pdf/2608.07420
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 世界模型长时序预测优化
tags:
- World Model
- Long Horizon Prediction
- End-to-End Training
- Reinforcement Learning
- Direct Prediction
one_liner: 提出非递归直接预测世界模型DPWM，通过端到端端点监督大幅提升长时序未来预测精度
practical_value: '- 做长周期用户行为预测/商品生命周期预测时，可参考直接预测端目标的训练范式，替代递归多步预测避免误差累积，比如预测用户30天后消费意愿可直接端到端训练，无需逐天预测递归

  - 序列输入的长时序任务（比如用户连续动作序列到最终转化的预测）可复用Transformer动作序列编码+FiLM条件调制的架构，用固定深度梯度路径解决长序列训练梯度消失问题

  - 训练长时序模型时可测试不同最大训练Kmax的泛化性，需要外推到超出训练长度的场景时，适当放大Kmax能提升分布外泛化能力，无需局限于实际推理的最大长度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有世界模型大多基于短步预测目标训练，推理时递归滚动生成长时序结果，存在训练推理不匹配问题：局部误差会随递归逐步放大，且训练时对所有过渡步骤加权相同，未区分不同步骤对最终结果的影响，导致长时序预测精度极差，无法满足Agent长周期规划、决策需求。

### 方法关键点
- 采用直接预测范式：不预测中间状态，直接根据初始观测和任意长度动作序列，单步前向预测K步后的端点观测，避免递归误差累积
- DPWM非递归架构由四部分组成：观测编解码器、带RoPE+非因果局部注意力的Transformer动作序列编码器（均值池化生成固定维度动作嵌入）、FiLM条件调制的MLP动力学模块，梯度路径长度固定，不受预测horizon影响，适配长序列端到端训练
- 训练目标直接对齐最终端点预测损失，混合采样不同长度K值训练，让模型适配可变长度预测需求

### 关键实验
在DeepMind Control Suite连续控制、Atari Pong像素控制基准上测试，对比MoSim、短步训练ADM等基线：
- 连续控制任务200步预测时，DPWM较短步训练ADM的端点MSE最高降低94%（Cheetah任务policy评估场景下，ADM MSE为34.07，DPWM仅为1.38），预测horizon越长优势越显著
- 长步训练的ADM较短步训练版本性能提升80%以上，验证训练目标比架构选择对长时序精度影响更大
- Pong像素任务400步预测时，DPWM像素MSE较ADM低17%，无递归漂移问题

### 核心结论
长时序预测的核心瓶颈不是模型架构，而是训练目标是否对齐实际使用的时间尺度，直接端到端监督最终目标比优化局部短步精度更有效
