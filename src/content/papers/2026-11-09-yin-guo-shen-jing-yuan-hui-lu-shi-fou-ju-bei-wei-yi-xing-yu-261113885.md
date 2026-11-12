---
title: Are Causal Neuron Circuits Unique and Transferable?
title_zh: 因果神经元回路是否具备唯一性与可迁移性
authors:
- Ömer Tekin Yavuz
affiliations:
- İletişim Yazılım, Bursa, Turkey
arxiv_id: '2611.13885'
url: https://arxiv.org/abs/2611.13885
pdf_url: https://arxiv.org/pdf/2611.13885
published: '2026-11-09'
collected: '2026-11-12'
category: LLM
direction: 大模型可解释性 · 神经元回路干预
tags:
- Mechanistic Interpretability
- Neuron Circuit
- Causal Intervention
- LLM
- Ablation Study
one_liner: 通过LLM神经元干预实验验证因果神经元组存在冗余，效果仅在同任务转述下可迁移
practical_value: '- 做LLM4Rec、Agent的推理优化时，可通过干预少量核心因果神经元替代全参数调整，大幅降低计算成本

  - 垂直领域LoRA微调时，可先定位领域任务对应的核心因果神经元组，仅微调对应神经元子集，兼顾微调效率与通用能力保留

  - 跨场景迁移LLM能力时，先验证目标因果神经元组的跨场景适配性，避免盲目复用全量权重导致的效果退化'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM可解释性研究仅验证了神经元组干预可改变模型输出，未明确这类神经元组的必要性、可替代性与跨输入迁移性。
### 方法关键点
针对Qwen、Llama、Gemma系列模型的12个MLP神经元组，穷举4096种子集开展零消融、激活值替换等因果干预实验，覆盖双选首都判别、多跳关系推理两类任务。
### 关键结果数字
1. 首都任务中消融12个目标神经元使答案置信度边际下降27%，随机神经元无明显影响，且目标神经元激活值跨问题几乎恒定，不携带问题特定信息
2. 多跳推理任务中替换12个神经元的首跳激活值，Qwen3-1.7B、Llama-3.2-1B、Gemma-3-1B分别在9/11、9/11、8/10的链上输出首跳桥接实体，随机神经元无该效果
3. 完整神经元组非必需，少量不相交子集即可独立实现输出翻转，干预效果仅在同问题转述场景下迁移，跨其他任务链效果极弱
