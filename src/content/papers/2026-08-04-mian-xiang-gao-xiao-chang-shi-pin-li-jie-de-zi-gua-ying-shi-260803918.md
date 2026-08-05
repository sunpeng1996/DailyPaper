---
title: 'When and Where to Look: Adaptive Visual Evidence Scheduling for Efficient
  Long Video Understanding'
title_zh: 面向高效长视频理解的自适应视觉证据调度方法EcoFrame
authors:
- Ke Li
- Jiayu Chen
- Maoliang Li
- Zihao Zheng
- Hailong Zou
- Hengyi Zhang
- Xuanzhe Liu
- Xiang Chen
affiliations:
- Peking University School of Electronics Engineering and Computer Science
- Peking University School of Computer Science
arxiv_id: '2608.03918'
url: https://arxiv.org/abs/2608.03918
pdf_url: https://arxiv.org/pdf/2608.03918
published: '2026-08-04'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 长视频理解效率优化
tags:
- VLM
- Long-Video-Understanding
- Adaptive-Scheduling
- Efficiency-Optimization
- Training-Free
one_liner: 提出无训练的自适应视觉证据调度框架EcoFrame，大幅优化长视频理解的精度-效率权衡
practical_value: '- 长视频/长序列理解场景可复用熵门控早停策略，用输出不确定性动态调整采样预算，平衡精度与推理成本

  - 可借鉴注意力引导的候选采样思路，在序列召回、多模态内容理解任务中优先采样高注意力区域，兼顾全局覆盖

  - 无训练的调度框架设计思路可直接复用，无需额外微调预训练模型，降低业务落地成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
长视频理解需VLM基于稀疏采样帧推理，现有两类方案存在明显缺陷：静态一次性采样方法使用固定帧预算与候选池，精度上限低；Agent类调度方案依赖多轮推理，推理开销极高，亟需低 overhead 的自适应采样方案。
### 方法关键点
提出训练免的EcoFrame框架，核心包含两个模块：
1. 熵门控预算调度：基于VLM输出的不确定性判断当前证据是否足够，满足需求则早停，否则逐步扩容帧采样预算；
2. 注意力引导候选生成：将帧级注意力转化为时序先验，在高信息密度区域做密集局部搜索，注意力分散时保留全局覆盖采样。
### 关键结果
在Video-MME、LongVideoBench、MLVU等基准上实现更优的精度-效率权衡；基于Qwen2.5-VL测试，平均精度达64.4，超过BOLT的63.5，推理速度较AKS、BOLT提升1.85×；相比Agent类方案A.I.R.精度相当，推理速度最高提升13.5×
