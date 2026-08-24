---
title: 'Anchoring Instruction Outside Mask: Exact Reference Caching for Efficient
  In-Context Diffusion Transformers'
title_zh: 掩码外锚定指令：面向高效上下文扩散Transformer的精确引用缓存
authors:
- Yangshuai Liu
- Zheming Li
- Jiaao Li
- Kang He
- Ziliang Lai
- Zhitai Liu
- Chengru Song
affiliations:
- Harbin Institute of Technology
- KlingAI Research
arxiv_id: '2608.21229'
url: https://arxiv.org/abs/2608.21229
pdf_url: https://arxiv.org/pdf/2608.21229
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态扩散模型 · 推理效率优化
tags:
- Diffusion Transformer
- KV Cache
- Attention Mask
- Knowledge Distillation
- In-Context Generation
one_liner: 通过掩码外文本锚定+蒸馏策略，在不损失生成质量的前提下大幅提升多参考扩散Transformer推理速度
practical_value: '- 电商商品图多参考编辑、营销素材生成等多模态生成场景，可复用「静态锚点+注意力掩码拆分」方案，在保留KV cache复用能力的同时解决跨模态交互缺失问题，大幅降低推理成本

  - 模型架构改动导致效果下降时，可参考「teacher-forced蒸馏+短周期on-policy监督」的修复策略，无需新增参数即可对齐原模型效果

  - 多参考输入的生成类业务（如AI设计、素材合成）可直接复用该架构的线性加速特性，参考越多提速收益越高，10个参考时可获5倍以上推理加速'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有上下文扩散Transformer的稀疏注意力方案虽支持参考KV cache跨步复用、降低推理计算量，但会阻断视觉参考与文本指令的注意力交互，导致多参考编辑场景下指令遵循度、参考保真度大幅下降。
### 方法关键点
1. 联合重构token序列与注意力掩码，通过掩码外静态文本锚点连接指令与参考分支，无需新增参数即可保留KV cache全步复用能力；
2. 采用teacher-forced速度蒸馏+短周期on-policy蒸馏策略，修复架构改动带来的生成质量损失，是首次将on-policy蒸馏用于扩散模型架构效果恢复。
### 关键结果
在3个图像编辑基准上效果完全对齐全注意力方案；5张参考图时40步去噪全流程加速3.92倍，静态锚点引入的运行时开销可忽略；10张参考图时提速达5.47倍。
