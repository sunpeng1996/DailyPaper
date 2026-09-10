---
title: 'Transformers as In-Context Samplers: From Closed-Form Diffusion to Estimation-Free
  Sampling'
title_zh: Transformer作为上下文采样器：从闭式扩散到无估计采样
authors:
- Arman Adibi
- Alireza Jafari
- Mohammad Ghavamzadeh
- Hadi Daneshmand
affiliations:
- Augusta University
- University of Virginia
- Qualcomm AI Research
arxiv_id: '2609.08981'
url: https://arxiv.org/abs/2609.08981
pdf_url: https://arxiv.org/pdf/2609.08981
published: '2026-09-08'
collected: '2026-09-10'
category: LLM
direction: LLM上下文学习 · 生成采样机理
tags:
- Transformer
- In-Context Learning
- Diffusion Sampler
- Energy-Based Model
- Attention Mechanism
one_liner: 证明冻结Transformer可基于上下文样本模拟迭代生成采样器，明确注意力与FFN的生成功能
practical_value: '- 可借鉴Transformer隐层U型能量分布特性，优化生成式推荐的语义Topic采样逻辑，提升同主题商品/推荐文案生成的一致性

  - 复用软注意力加权平均+FFN做欧拉更新的结构，设计轻量化上下文生成采样模块，适配电商个性化推荐理由、商品文案生成场景

  - 基于冻结Transformer的上下文采样能力，可低成本实现小样本冷启动场景下的同类别商品扩展召回，无需额外微调模型'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有上下文学习研究多聚焦监督类任务，其在数据生成场景的可行性尚未得到理论验证，Transformer内部组件的生成作用机理也缺乏明确解释。
### 方法关键点
1. 理论证明冻结Transformer可基于上下文样本模拟迭代生成采样器，其中softmax attention负责计算责任权重与加权经验平均，FFN层实现欧拉更新，可复现闭式及平滑闭式扩散采样器；
2. 针对预训练LLM设计语义主题采样实验，观测隐层归一化状态的几何变化规律，验证理论结论与实际预训练模型的匹配性。
### 关键结果
Transformer归一化隐层状态呈现两阶段几何特性：中间层向均匀球面参考分布收敛，输出层回归主题相关结构化表示，隐层粒子能量也对应呈现一致U型分布。
