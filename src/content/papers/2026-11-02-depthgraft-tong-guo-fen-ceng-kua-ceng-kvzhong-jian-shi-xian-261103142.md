---
title: 'DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV
  Reconstruction'
title_zh: DepthGraft：通过分层跨层KV重建实现结构正则化
authors:
- Xiaohan Qin
- Xiangdong Zhang
- Yu Wang
- Huaijin Wu
- Zhuo Xia
- Yebin Yang
- Junchi Yan
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Xiaohongshu Inc.
arxiv_id: '2611.03142'
url: https://arxiv.org/abs/2611.03142
pdf_url: https://arxiv.org/pdf/2611.03142
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: LLM架构优化 · KV缓存与正则化
tags:
- KV cache
- Transformer
- MoE
- Structural Regularization
- Inference Acceleration
one_liner: 提出分层跨层KV重建架构DepthGraft，同时提升LLM下游性能与推理效率
practical_value: '- 生成式推荐、电商Agent场景部署LLM时，可直接复用DepthGraft的三层KV共享设计，降低约1/3的KV缓存占用，128K长上下文下TTFT降低近30%，大幅提升用户交互响应速度

  - 训练电商/广告领域专用LLM时，可借鉴跨层KV梯度正则化思路，无需增加额外计算量即可提升下游任务表现，16B规模下知识类任务最高可获得7%的绝对精度提升

  - 该方法的步长对齐KV映射天然兼容流水线并行，训练大模型时无需大幅改造现有并行训练框架即可落地，降低架构优化的工程成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Pre-LN架构Transformer深度缩放时存在层间信息稀释问题，深层对浅层特征的提取效率低，现有跨层连接方案会引入额外计算与访存开销；传统跨层KV共享仅被视为缓存压缩手段，其梯度传导带来的正则化价值未被系统挖掘，无法兼顾模型效果与推理效率。
### 方法关键点
- 明确KV共享本质为跨层梯度正则化：远端层复用浅层KV时，梯度直接传导至浅层KV投影层，可让Key检索方向更聚焦、Value内容子空间更丰富，正则化效果由共享拓扑决定
- 三层分层KV重建架构：将Transformer拆分为浅、中、深三个等规模阶段，浅/中层正常计算KV，深层KV通过可学习通道系数，从步长对齐的浅-中层源KV对加权重建得到
- 天然适配PP/VPP流水线并行，保留prefill提前完成特性，工程改造成本低
### 关键结果
在0.5B~16B稠密与MoE模型上验证，对比GQA、MLA基线：16B MoE模型MMLU-Pro绝对提升7.0%，CMMLU提升6.6%，C3提升6.4%；KV缓存降低约1/3，128K上下文下TTFT降低28.8%，解码速度损失<1%；32K长上下文RULER基准平均得分提升6.2分。
**最值得记住的一句话**：KV共享不只是推理优化手段，更是可改善KV表示几何的训练正则化方法，合理的共享拓扑能同时提升模型效果与推理效率。
