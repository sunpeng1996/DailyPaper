---
title: Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning
title_zh: 面向参数高效微调的流形约束超连接方法
authors:
- Valentijn Oldenburg
- Floris de Kam
- Bente Zuijdam
- Lieve Eberson
- Nicky van Zutphen
- Stef de Wildt
- Ivo Verhoeven
affiliations:
- University of Amsterdam
arxiv_id: '2607.18130'
url: https://arxiv.org/abs/2607.18130
pdf_url: https://arxiv.org/pdf/2607.18130
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: 参数高效微调 · 残差连接优化
tags:
- PEFT
- LoRA
- residual connection
- mHC
- Transformer
one_liner: 将流形约束超连接引入参数高效微调，搭配LoRA可在同参预算下提升语言建模损失和任务效果
practical_value: '- 做LLM微调适配下游推荐/Agent任务时，可尝试mHC+LoRA的组合，在参数量接近的前提下提升特定任务（比如常识推理、多步决策）的效果

  - 静态mHC参数量极低（n=4时每层仅24个参数），适合端侧或低资源场景下的小参数微调需求，几乎不增加推理 overhead

  - 微调时可将mHC的残差混合矩阵固定为单位阵，既能减少训练参数量，还能避免破坏预训练好的残差通路表征，效果优于可学习混合矩阵

  - 现有LoRA微调效果遇瓶颈时，可优先尝试优化残差连接路由而非单纯提升LoRA秩，获得更高的参数量效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有PEFT方法（LoRA、Adapter等）多聚焦权重适配或插入轻量模块，未对Transformer核心组件残差连接做针对性优化；此前流形约束超连接（mHC）仅应用于预训练场景，其在冻结主干的微调场景下的价值尚未被探索。
### 方法关键点
- 将mHC作为PEFT模块嵌入冻结Transformer主干，通过学习残差流的读入、写出、跨层混合路由适配下游任务，与LoRA等修改局部权重的方法天然互补
- 对比静态/动态mHC、mHC-lite、KromHC三种参数化方式，动态KromHC兼顾参数量效率与效果，为最优实现
- 发现微调场景下mHC的残差混合矩阵会自发趋近单位阵，因此提出将其固定为单位阵的mHCidentity变体，进一步减少参数量且提升效果
### 关键结果
- 基于Tulu-3 SFT数据集微调，在BBH、GSM8K、MMLU等8个下游任务评估，覆盖1B、7B规模OLMo-2模型
- 对比LoRA、VeRA、(IA)3等主流PEFT基线：同参数量下单独使用mHC效果略逊于LoRA，但mHC+LoRA组合在7B规模下比同参数量LoRA降低测试损失0.001，在GSM8K、PIQA等4/8的下游任务上获得提升
- 静态mHC搭配LoRA仅增加1280个参数，就能将测试损失从1.28降到1.21

最值得记住的结论：残差路由是PEFT的独立优化轴，微调时优先保留预训练残差通路、仅优化残差流的读写路由，比学习跨流混合更高效
