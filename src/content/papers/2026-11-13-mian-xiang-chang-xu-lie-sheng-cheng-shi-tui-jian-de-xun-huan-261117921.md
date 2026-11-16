---
title: 'RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation'
title_zh: 面向长序列生成式推荐的循环记忆压缩框架RecMem
authors:
- Haoyi Hu
- Gaoyang Guo
- Yunjia Xi
- Wen Chen
- Weiwen Liu
- Jian Wu
- Yuning Jiang
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2611.17921'
url: https://arxiv.org/abs/2611.17921
pdf_url: https://arxiv.org/pdf/2611.17921
published: '2026-11-13'
collected: '2026-11-16'
category: GenRec
direction: 生成式推荐 · 长序列记忆压缩
tags:
- GenRec
- LongSequenceRec
- MemoryCompression
- SequentialRec
- InferenceEfficiency
one_liner: 用固定大小记忆槽压缩长用户交互历史，大幅降低上下文开销的同时保留高推荐精度
practical_value: '- 长序列生成式推荐场景可直接复用slot-wise遗忘门+分叉编解码器的记忆压缩方案，仅需16个记忆槽即可保留97%的全1200长度序列Recall@200效果，上下文开销降低5.6倍，大幅降低推理延迟和KV缓存成本

  - 训练时引入流一致性损失对齐分段处理与打包处理的预测分布，搭配逐步增大rollout长度的课程学习，可有效避免长序列更新时的误差累积，保障10000次交互内推荐效果无衰减

  - 工程上可持久化缓存用户记忆状态，新交互攒满一个segment后仅需做一次增量更新，冷启动时按段顺序压缩即可，无需每次重新处理全量历史，适配大规模电商推荐在线服务场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐依赖长用户交互历史捕捉全周期偏好，但Transformer直接处理数千条交互会导致上下文爆炸，计算、显存、推理延迟随序列长度线性增长；现有固定窗口、检索、分段摘要方法要么丢失长期偏好信号，要么上下文长度仍随历史增长，无法满足大规模电商场景的长序列服务需求。
### 方法关键点
- 采用分叉式编解码器架构，底层HSTU层共享，上层分独立的记忆编码、推荐解码分支，将用户历史拆分为归档前缀和最近200条后缀，归档前缀按200条为一段拆分
- 循环压缩阶段每个段输入结合上一轮记忆状态和可学习查询token，经编码器输出候选记忆，用slot-wise遗忘门更新固定大小的16个记忆槽，每个槽单独做范数裁剪避免表征爆炸
- 训练采用双目标：主目标为推荐NCE损失，流一致性损失对齐两段分别更新和合并为一段更新的预测分布，搭配逐步增大rollout长度的课程学习稳定长序列梯度
- 推理时记忆状态可持久化缓存，新交互满段后仅做增量更新，解码器输入固定为16个记忆槽+200条最近交互，上下文长度与历史总长度无关
### 关键实验
在MerRec数据集（500万+用户的C2C交互数据）上，对比HSTU-1200、PHSTU、最近200条基线、检索增强基线：RecMem仅用216个解码器token（比HSTU-1200少5.6倍），保留87.9%的Recall@10和97.0%的Recall@200，效果远超所有压缩类基线；单checkpoint处理10000次交互无效果衰减，单用户记忆仅占8KiB，warm推理延迟7.65ms，比HSTU-1200低一个数量级。
### 核心结论
长序列生成式推荐不需要保留全量历史作为上下文，通过任务驱动的固定容量记忆压缩，可在极小开销下保留绝大多数长期偏好信号。
