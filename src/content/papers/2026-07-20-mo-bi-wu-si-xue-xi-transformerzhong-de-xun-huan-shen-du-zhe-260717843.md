---
title: 'Mobius Learning: Cyclic Depth Folding in Transformers'
title_zh: 莫比乌斯学习：Transformer中的循环深度折叠训练机制
authors:
- Tongtian Zhu
affiliations:
- Zhejiang University
arxiv_id: '2607.17843'
url: https://arxiv.org/abs/2607.17843
pdf_url: https://arxiv.org/pdf/2607.17843
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: Transformer分布式训练·循环深度折叠优化
tags:
- Transformer
- Distributed Training
- Cyclic Depth Folding
- Parameter Sharing
- Memory Optimization
one_liner: 提出循环深度折叠的Transformer训练架构，让块组同时适配深浅层角色，降低分布式训练显存开销并提升大循环深度效果
practical_value: '- 训练大尺寸LLM4Rec/推荐Agent底座时，可复用循环深度折叠的分布式策略，每个Worker仅存储部分块组，大幅降低单卡显存需求，解决小集群训练大模型的硬件瓶颈

  - 多步推理的推荐Agent微调场景，可尝试块组多深度角色训练范式，在不增加参数量的前提下提升大循环步数下的推理准确率

  - 跨层参数共享的轻量化LLM端侧部署场景，可借鉴深度角色叠加思路，让有限参数同时适配深浅层语义处理需求，压缩端侧模型体积'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统Transformer的块组与深度角色强绑定，固定顺序的循环训练、跨层参数共享方案无法充分挖掘块组参数潜力；同时分布式训练中数据并行需要全量模型副本、流水线并行固定阶段顺序，普遍存在单卡显存占用高、参数利用率低的问题，亟需更高效的训练架构。

### 方法关键点
- 将Transformer拆分为P个块组，每个Worker仅存储1个块组，不同Worker发起的数据流从本地块组开始，按循环偏移顺序遍历所有块组，实现同一块组在不同数据流中同时承担深浅层角色（深度-角色叠加）
- 采用莫比乌斯并行策略，原始训练数据保留在本地Worker，仅传输隐状态与梯度，无需全量模型副本，大幅降低单卡显存占用
- 训练与推理时每个数据流完成L次完整块组循环（共K=LP次块组调用），最终对不同起始路径的损失做平均得到优化目标

### 关键实验
在124M参数量的modded GPT-2 small上开展四Worker实验，训练数据为2.5B FineWeb tokens，对比同循环深度L的固定顺序循环训练基线：L=6时验证损失低0.0084，L=10时低0.0059，L=15时低0.0083，仅L=1、2时效果略低于基线。

### 核心结论
Transformer块组不需要固定绑定单一深浅层角色，循环深度折叠的训练范式可以在降低分布式训练显存开销的同时，提升大循环深度下的模型效果。
