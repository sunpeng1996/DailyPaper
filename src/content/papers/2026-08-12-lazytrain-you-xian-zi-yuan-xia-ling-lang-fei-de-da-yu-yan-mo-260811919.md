---
title: 'LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization
  in Large Language Model Training'
title_zh: LazyTrain：有限资源下零浪费的大语言模型训练调度优化
authors:
- Xiaojun Wu
- Cehao Yang
- Honghao Liu
- Xueyuan Lin
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2608.11919'
url: https://arxiv.org/abs/2608.11919
pdf_url: https://arxiv.org/pdf/2608.11919
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 大模型训练优化 · 资源调度
tags:
- LLM-Training
- Resource-Scheduling
- MILP
- Offloading
- Activation-Checkpoint
one_liner: 通过混合整数调度优化LLM层流训练的显存、通信与重计算，单卡训练吞吐量提升24%
practical_value: '- 垂直领域LLM SFT（如电商商品文案生成、推荐Agent工具调用微调）场景下，可复用LazyTrain调度逻辑，在单张消费级/专业GPU上训练更大尺寸模型，降低硬件成本

  - 多模态大推荐模型微调时，可借鉴激活分层放置+通信隐藏的思路，在显存受限场景下提升可行batch size，减少训练迭代周期

  - 小团队LLM基建可直接集成开源LazyTrain到现有训练框架，无需修改模型代码即可获得约20%的单卡训练吞吐量提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有低资源LLM训练系统（如MegaTrain、ZeRO offload）多采用固定启发式的激活检查点、卸载策略，常让CPU-GPU/NVMe通信落在关键路径上，导致显存容量足够但实际训练吞吐量偏低，单卡训练大模型的硬件效率仍有较大提升空间。

### 方法关键点
- 基于层流执行器做调度优化，将激活检查点选择、存储层级（GPU/CPU/NVMe）放置、重计算块划分、跨层级通信重叠建模为混合整数线性规划（MILP）问题，目标是最小化重计算成本+激活带来的额外通信延迟，而非单纯最大化卸载量
- 训练前离线求解一次最优调度策略，运行时直接执行，调度器不在训练关键路径上
- 设计Hybrid 8-bit算子：结合8bit优化器状态压缩（降低CPU内存占用）与快速梯度裁剪（抵消8bit量化带来的CPU额外开销）

### 关键实验结果
单卡H800上从Qwen2.5-3B到Qwen3.6-27B的SFT实验，对比baseline MegaTrain：27B模型场景下持续TFLOPS从176.9提升到219.95，吞吐量提升1.24倍，token/s从1075.8提升到1361，GPU显存峰值仅68.84GB，MetaMathQA数据集上精确匹配准确率达95.42%；RTX 3090消费级卡上，各尺寸模型的最大可行batch size均比baseline大1，小显存场景下训练可行性更高；消融实验显示MILP调度贡献了12.2%的吞吐量提升，是核心增益来源。

### 核心洞察
低资源LLM训练的瓶颈往往不是显存不足，而是通信与计算的重叠效率不够，用全局调度优化比盲目堆卸载策略效果更好。
