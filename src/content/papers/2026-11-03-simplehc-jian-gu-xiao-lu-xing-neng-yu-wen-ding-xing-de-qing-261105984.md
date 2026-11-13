---
title: 'On the Design of Hyper-Connections: Simplification, Stability, and Scalability'
title_zh: SimpleHC：兼顾效率、性能与稳定性的轻量化超连接架构
authors:
- Xiangdong Zhang
- Xiaohan Qin
- Sunan Zou
- Tuo Dai
- Bizhao Shi
- Zhuo Xia
- Yebin Yang
- Yizhou Chen
- Yuliang Liu
- Yu Cheng
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Dots Studio
- Peking University
- Nanyang Technological University
- Independent Researcher
arxiv_id: '2611.05984'
url: https://arxiv.org/abs/2611.05984
pdf_url: https://arxiv.org/pdf/2611.05984
published: '2026-11-03'
collected: '2026-11-13'
category: Training
direction: 大模型架构优化 · 超连接轻量化设计
tags:
- Hyper-Connection
- SimpleHC
- MoE
- Training Efficiency
- LLM Architecture
one_liner: 移除残差混合+共享内存访问优化，将超连接训练开销降至2.4%且性能持平mHC
practical_value: '- 垂直场景（电商导购Agent、生成式推荐基座）LLM训练可直接替换原有残差为SimpleHC，仅增加2.4%训练开销即可获得与mHC相当的效果，同时降低训练崩溃概率

  - 多流结构（如多兴趣用户建模、多源特征融合模块）可复用分组执行+延迟写回+标量修正的访存优化思路，降低显存占用、提升推理/训练速度

  - MoE大模型训练可直接采用SimpleHC的梯度平稳设计，支持更大batch size，减少电商/推荐大模型训练过程中的调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
前沿大模型广泛采用的Hyper-Connection（HC）架构尤其是mHC变体，虽能提升模型深度利用率，但残差混合操作、频繁的多流状态读写带来了7%-27%的额外训练开销，Sinkhorn约束还引入了训练不稳定风险，亟需更轻量化的设计在不损失性能与稳定性的前提下降低训练成本。
## 方法关键点
- 架构简化：移除残差混合模块，仅保留可学习读写门控+恒等映射的最小有效结构，既消除Sinkhorn计算开销，也避免无约束混合带来的信号累计放大/衰减风险
- 执行优化：提出共享内存访问机制，以4个连续子层为一组，统一从组入口状态计算所有层的独立读写门控，批处理读操作、延迟到组边界再统一写回，通过标量修正保留前序子层输出贡献，无需频繁读写中间高维残差状态
- 配套设计了前后向专用融合内核，进一步降低访存与计算开销
## 关键结果
在15B、30B参数量的MoE模型上验证，对比mHC、identityHC基线：
1. 最大隐藏层尺寸下，端到端训练额外开销从7%降至2.4%，激活存储降低31%
2. 14个下游基准平均得分63.1，与mHC的62.9持平，MATH、中文C3等任务表现更优
3. 10倍学习率压力测试下，mHC出现梯度爆炸，SimpleHC梯度保持平稳无尖峰

**最值得记住的一句话**：基础架构优化优先做组件减法找到最小有效结构，再针对性优化访存瓶颈，往往能同时拿到性能、效率、稳定性的多重收益。
