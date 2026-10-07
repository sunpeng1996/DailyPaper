---
title: 'Denoising Hierarchical Representations: Joint Continuous Diffusion for Language
  Modeling'
title_zh: 层次去噪表征：面向语言建模的联合连续扩散框架
authors:
- Mathias Ollu
- Nikos Komodakis
affiliations:
- Ecole Polytechnique
- Archimedes Athena RC
- University of Crete
- IACM-Forth
arxiv_id: '2610.08738'
url: https://arxiv.org/abs/2610.08738
pdf_url: https://arxiv.org/pdf/2610.08738
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: 扩散语言建模 · 多粒度语义联合扩散
tags:
- DiffusionLM
- HierarchicalRepresentation
- ContinuousDiffusion
- FlowMatching
- TextGeneration
one_liner: 以极低开销通过粗细粒度语义联合扩散大幅提升连续扩散语言模型性能
practical_value: '- 多粒度联合生成思路可迁移到生成式推荐：对候选item语义做不同粒度聚类，将粗粒度聚类ID和细粒度item ID联合做扩散生成，提升准确率的同时仅增加极少参数开销

  - 分模态独立调优采样策略可复用：对推荐场景多模态特征（用户/物品/上下文）分别设置噪声调度、采样率，用粗粒度特征作为语义锚降低高噪声阶段生成误差

  - 语义聚类低成本优化方法可直接落地：对预训练token/embedding做k-means聚类获得粗粒度语义单元，无需额外训练，选择合适聚类规模（如n=16）即可控制开销达到最优效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
连续Diffusion Language Models (DLM)支持并行文本生成，推理效率显著优于自回归LM，但现有连续DLM在高噪声阶段难以精准还原token语义，生成质量、下游任务表现长期落后于离散DLM与自回归模型，亟需低overhead的优化方案拉平性能差距。

### 方法关键点
- 对预训练token embedding做k-means聚类得到粗粒度语义簇ID，构建「细粒度token + 粗粒度簇ID」双层语义表征，二者共享序列长度，拼接后输入模型仅新增约1%参数开销
- 采用联合扩散范式，为两种模态分别设置独立噪声调度、采样器与损失权重：粗粒度簇信息作为语义锚在高噪声阶段引导token恢复，细粒度token预测结果同时反哺优化簇识别精度
- 推理最后阶段仅保留token模态输出，无需额外后处理，可直接兼容CoBit、FLM流匹配等现有连续DLM架构

### 关键结果
在LM1B、OpenWebText（OWT）、GSM8K基准上对比SOTA连续DLM：
- 数据熵匹配条件下，LM1B的GenPPL从73.6降至49.4（降幅24.2），OWT的GenPPL从71.1降至50.4（降幅20.7），性能超过同参数量离散DLM
- GSM8K准确率达27.4%，优于所有现有连续扩散/流匹配模型
- 仅需基线60%的训练步数即可达到同等性能，推理开销最大仅增加4.2%

无需新增复杂结构，仅通过引入无训练成本的语义聚类作为辅助模态做联合扩散，就能以可忽略的开销大幅提升连续生成模型性能，语义锚的价值远大于新增参数的作用。
