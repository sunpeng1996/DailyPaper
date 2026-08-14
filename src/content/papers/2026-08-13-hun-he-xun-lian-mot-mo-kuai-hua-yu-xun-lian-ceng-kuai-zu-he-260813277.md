---
title: 'Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into
  a Larger Language Model'
title_zh: 混合训练（MoT）：模块化预训练层块组合生成大语言模型
authors:
- Mohammed Sabry
- Sean Augenstein
- Keith Rush
- Lucio Dery
affiliations:
- Google
- Dublin City University
arxiv_id: '2608.13277'
url: https://arxiv.org/abs/2608.13277
pdf_url: https://arxiv.org/pdf/2608.13277
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 大语言模型 · 模块化预训练优化
tags:
- MoT
- Modular Pretraining
- Transformer Training
- LLM Efficiency
- Scaffold Training
one_liner: 混合训练框架MoT通过冻结对齐器脚手架独立训练Transformer层块，可拼接为完整大语言模型
practical_value: '- 训练电商/推荐域专属中/小LLM（比如文案生成、语义匹配、query改写模型）时，可复用开源小模型作为对齐器脚手架，分块并行训练目标模型，降低单任务故障影响，加快迭代速度

  - 若团队需迭代多版结构一致的垂直域LLM，可复用同一个对齐器，当复用次数≥3时，MoT总计算成本低于端到端单块训练，性价比更高

  - 对模型效果要求不极致的场景（比如推荐push文案生成、搜索suggestion补全），可采用低计算量schedule：K=2分块+15k步适配，仅用70%左右的端到端训练EFLOPs就能达到接近基线的效果

  - 模型迭代时若仅需更新部分层（比如适配新电商品类语义），可仅重训对应层块，拼接后做短适配即可，无需全量重训，大幅节省算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统LLM预训练采用端到端单块式流程，存在明显扩容瓶颈：单节点故障会影响全量训练进度，每次模型迭代都需要重启全流程，小样本训练研究成本高、可复现性差，亟需探索可拆分、可复用的模块化预训练范式。

### 方法关键点
- 将目标Transformer拆分为K个连续层块，引入与目标模型形状完全兼容的预训练对齐器（宽度、注意力头维度、词表、输出头完全一致），同样拆分为K个对应块
- 为每个目标层块搭建脚手架网络：冻结所有对齐器块，仅训练目标层块，采用标准next-token损失优化，各块训练过程无梯度交互
- 训练完成后丢弃对齐器，直接拼接所有目标层块，可选择短时间端到端适配消除层块接口不匹配问题

### 关键实验结果
实验基于C4英文语料，目标模型为12层1.3B参数的Gemma风格Decoder模型，基线为端到端预训练同结构模型，PPL=15.0，消耗268.4 EFLOPs：
- 冷组合（无适配）：PPL=19.3，消耗157.9 EFLOPs，理想关键路径速度为基线的4.2倍
- 加15k步端到端适配：PPL=15.9，消耗189.4 EFLOPs（比基线低29%），关键路径速度为基线的2.8倍
- 质量等价配置：PPL与基线持平为15.0，总消耗285 EFLOPs，关键路径速度为基线的1.7倍；当对齐器复用次数≥3时，单轮训练成本低于端到端基线

### 核心结论
模块化预训练的核心价值不是无条件的效率提升，而是通过对齐器摊销实现多轮复用的成本优势，以及拆分训练带来的故障容错、迭代灵活度提升。
