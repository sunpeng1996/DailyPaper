---
title: UE5M3 FP4 Block Scaling for Stable Language Model Pretraining
title_zh: 基于UE5M3块缩放的稳定FP4大语言模型预训练方案
authors:
- Robert Hu
- Carlo Luschi
- Paul Balanca
affiliations:
- Graphcore Research
arxiv_id: '2609.02846'
url: https://arxiv.org/abs/2609.02846
pdf_url: https://arxiv.org/pdf/2609.02846
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 大模型低精度预训练 · FP4量化
tags:
- FP4
- Low Precision Training
- UE5M3
- Pretraining
- Transformer Engine
- Quantization
one_liner: 提出UE5M3无符号块缩放的FP4预训练配方，省略RHT无BF16豁免，效果优于Transformer Engine NVFP4
practical_value: '- 垂直领域LLM训练降本：训电商商品理解/用户意图等垂类小模型时，可复用UE5M3块缩放+50步延迟张量缩放的FP4方案，省略RHT和BF16最终层豁免，降低实现复杂度与算力开销

  - 训练吞吐优化：用NVFP4训练推荐/广告排序大模型时，可尝试去掉RHT+全线性层转FP4，实测提升21.2%训练吞吐，加快业务模型迭代速度

  - 量化策略迁移：低精度训练时可参考仅对反向传播上游梯度dY做随机舍入、其余用就近舍入的策略，平衡训练稳定性与量化精度

  - 线上推理优化：部署电商导购Agent等LLM应用时，可借鉴50步延迟刷新激活缩放的方案，减少量化计算量，对精度影响小于9e-5 NLL'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
FP4相比BF16理论吞吐高4倍，是大模型预训练降本的核心方向，但现有NVIDIA Transformer Engine NVFP4方案依赖随机Hadamard变换（RHT）、BF16最终层豁免、逐步张量缩放等额外操作，实现复杂且增加额外开销。UE5M3无符号块缩放具备更宽的动态范围，有望简化FP4预训练流程同时保障训练稳定性。
### 方法关键点
- 块缩放设计：4位E2M1载荷搭配8位UE5M3无符号块缩放，相比NVFP4的E4M3块缩放，最大有限值高137倍，最小非零值小256倍，动态范围显著提升
- 延迟张量缩放：张量最大值每50步采样缓存一次，无需逐步计算张量最大值；仅对反向传播的上游梯度dY做随机舍入，其余操作使用就近舍入
- 省略冗余操作：完全去掉RHT变换，所有112个符合条件的内部线性层全部采用FP4，无需保留BF16最终层豁免
- 构建与原生NVFP4 GEMM输出完全匹配的软件仿真器，可在无原生UE5M3硬件支持的情况下完成实验验证
### 关键结果
- 训练Nemotron-H 8B模型188.7亿token，对比NVFP4 baseline：最终窗口训练loss低0.0384，验证集NLL低0.00362，下游Core9、MMLU、MMLU-Pro分别高0.13、1.01、0.01个百分点
- 原生NVFP4去掉RHT+全线性层转FP4的消融实验实现21.2%的训练吞吐提升
> 最值得记住：UE5M3块缩放的宽动态范围可大幅简化FP4预训练流程，效果优于现有NVFP4方案的同时降低实现复杂度与计算开销
