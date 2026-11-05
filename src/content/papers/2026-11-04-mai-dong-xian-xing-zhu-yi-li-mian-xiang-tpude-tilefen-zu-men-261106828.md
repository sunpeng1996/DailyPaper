---
title: 'Systolic Linear Attention: Co-Designing Tile-Grouped Gated Delta Attention
  for TPUs'
title_zh: 脉动线性注意力：面向TPU的Tile分组门控Delta注意力协同设计
authors:
- Gagik Amirkhanyan
- Nuojin Cheng
affiliations:
- Google
arxiv_id: '2611.06828'
url: https://arxiv.org/abs/2611.06828
pdf_url: https://arxiv.org/pdf/2611.06828
published: '2026-11-04'
collected: '2026-11-05'
category: Training
direction: 大模型训练·TPU专属注意力优化
tags:
- Linear Attention
- TPU
- MoE
- Kernel Optimization
- Training Efficiency
one_liner: 面向TPU硬件特性重构门控delta线性注意力，训练提速最高24%，推理延迟最高降60%
practical_value: '- 硬件协同设计思路可复用：做LLM4Rec、Agent大模型离线训练时，可针对自有GPU/ASIC硬件的计算单元尺寸，调整attention头分组、维度对齐策略，避免算力浪费

  - 长用户行为序列建模可借鉴：做长周期用户行为序列召回/排序时，可复用tile分组门控+块倍增逆矩阵的思路，降低线性attention的计算瓶颈，支持更长行为序列建模

  - 大模型预训练优化：如果用TPU训练MoE结构的电商/广告大模型，可直接替换SLA注意力，获得11%-24%的训练提速，基本不损失精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有GDN、KDA等门控delta线性注意力均为GPU定制，直接迁移到TPU时，因TPU的256×256脉动矩阵单元(MXU)与向量单元(VPU)吞吐量比达128:1，会出现MXU tile利用率不足50%、VPU运算成为瓶颈、中间数据HBM读写开销大的问题，最终仅能发挥不到一半的算力，训练和推理效率极低。
### 方法关键点
- 宽键分组值头：将键维度扩至256，每个键头共享给2/4个值头，刚好填满MXU的256×256 tile，QKV投影、chunk求解次数降低2-4倍
- Tile分组遗忘门：把256个键通道拆为4组64通道的tile，每组共享1个标量衰减率，避免VPU逐通道缩放开销，所有运算均跑在MXU上
- MXU端chunk求逆：采用递归块倍增算法，仅用矩阵乘法即可完成chunk逆矩阵求解，完全替代原VPU端顺序三角求解，无额外VPU开销
- 单内核全链路融合：将所有运算阶段融合到64MiB片上SRAM中执行，反向传播时在片上重计算中间矩阵，消除HBM中间读写开销
### 关键结果
在TPU v7x上测试：单SLA层比开源Tokamax KDA快1.6×-2.5×；在2048芯片规模的MoE预训练任务（6.5B-63.1B参数）上，SLA比KDA训练快11%-24%，困惑度略低于KDA；32层长序列推理场景下，131K上下文TTFT仅1.67s，比GQA快4.28倍，HBM占用降低93.4%。
### 核心结论
硬件与算法的协同设计，比单纯调优kernel能获得数量级的效率提升。
