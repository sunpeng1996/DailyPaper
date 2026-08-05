---
title: 'OmniPack: Unified Token Compression for Efficient Omni-modal Large Language
  Models'
title_zh: OmniPack：面向高效全模态大模型的统一Token压缩框架
authors:
- Wanshun Su
- Yang Shi
- Feihu Liu
- Ziwen Yu
- Yan Min
- Zhuoran Zhang
- Qixun Wang
- Haotian Wang
- Shixuan Liu
- Yuanxing Zhang
affiliations:
- Northwestern Polytechnical University
- Peking University
- Alibaba Group
- Tsinghua University
arxiv_id: '2608.03812'
url: https://arxiv.org/abs/2608.03812
pdf_url: https://arxiv.org/pdf/2608.03812
published: '2026-08-03'
collected: '2026-08-05'
category: Multimodal
direction: 全模态大模型 · Token压缩推理优化
tags:
- Token Compression
- Omni-modal LLM
- Inference Acceleration
- Training-free
- Multimodal Understanding
one_liner: 无需训练的两阶段全模态大模型Token压缩框架，极低保留率下实现最优性能效率平衡
practical_value: '- 多模态导购Agent、直播/短视频商品理解场景可直接复用两阶段压缩策略：预LLM阶段先做模态独立的结构冗余压缩，LLM内部完成多模态交互后再做任务相关的语义压缩，无需微调即可降低推理成本，适配H20等推理卡部署

  - 长视频/长音频类内容（如直播回放、商品讲解音视频）的Token压缩可借鉴模态特定打分规则：视觉特征叠加帧间变化、空间区分度，音频特征叠加相邻token变化系数，配合覆盖度选择避免长序列稀疏关键信息丢失

  - 压缩时丢弃的Token不要直接删除，可复用相似度加权合并trick，将丢弃Token信息按自身重要性权重聚合到最近的保留代表Token，压缩率超60%场景可有效降低信息损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态大模型处理音视频输入时生成的Token序列远长于文本，带来极高的推理计算与内存开销，现有压缩方法在极低Token预算下性能退化严重：预LLM压缩易丢失稀疏分布的结构关键信息，LLM内部压缩未充分利用音视频跨模态协同信息，无法满足线上低延迟部署需求。
### 方法关键点
- 训练无关的两阶段渐进压缩框架：第一阶段预LLM模态独立压缩，先按模态特定重要性（编码器注意力+视觉帧间/空间变化、音频相邻变化特征）筛选高显著性Token，再结合特征+位置联合距离做覆盖度选择保证全局信息不丢失，最后将丢弃Token按相似度、位置、保留Token重要性加权合并到对应代表Token，避免不可逆信息损失。
- 第二阶段LLM内部压缩：在多模态充分交互的中间层（如Qwen2.5-Omni-7B选第18层），结合文本Query相关性、跨模态协同度、模态内代表性三个维度打分筛选保留Token，再按语义多样性平衡补充，最终合并丢弃Token信息后输入后续Transformer层。
### 关键实验结果
在Qwen2.5-Omni-3B/7B、MiniCPM-o-2.6三个全模态主干，AVUT、WorldSense等5个音视频理解基准上验证，对比FastV、OmniZip、SEATS等SOTA压缩方法：
- 仅用16.7%的原FLOPs即可保留98.0%的原性能，仅用6.8%的原FLOPs仍保留92.9%的原性能；
- 15%/7.5% Token保留率下FLOPs降低10倍，prefill速度提升4.5倍，仅损失4.4%的原性能。
### 核心结论
全模态Token压缩需分阶段适配语义成熟度，预压缩保结构、后压缩保任务语义，二者协同才能在极低压缩率下实现性能与效率的最优平衡。
