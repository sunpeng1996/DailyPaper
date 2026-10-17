---
title: 'Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding'
title_zh: 面向长视频理解的恒定内存帧打包框架FramePack-U
authors:
- Shuo Gao
- Chenhao Zheng
- Zhongzheng Ren
affiliations:
- Renmin University of China
- University of Washington
- UNC-Chapel Hill
arxiv_id: '2610.16118'
url: https://arxiv.org/abs/2610.16118
pdf_url: https://arxiv.org/pdf/2610.16118
published: '2026-10-12'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型 · 长视频理解效率优化
tags:
- VLM
- Long Video Understanding
- Frame Packing
- Inference Optimization
- Memory Efficiency
one_liner: 提出免训练免微调、无架构修改的恒定内存帧打包框架，在各类VLM上实现长视频理解精度显著提升
practical_value: '- 可直接复用「语义相关性排序+多样性约束+可变分辨率打包」策略，用于电商直播/长短视频的内容理解特征压缩，在固定KV cache预算下提升语义识别精度

  - 免训练、无需修改模型架构的设计，可快速集成到现有多模态内容理解链路，大幅降低长视频推理的内存开销与延迟

  - 优先级驱动的资源分配思路可迁移到多模态推荐的用户行为序列压缩，将内存预算优先向高价值（点击/转化相关）的行为特征倾斜'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
小时级长视频、直播流等内容将VLM推理性能推至瓶颈，逐帧编码生成的视觉token序列随视频长度线性增长，带来极高内存开销与推理延迟；现有token裁剪、关键帧选择方案未解决O(n)扩展的本质问题，无法适配长视频处理需求。
### 方法关键点
提出免训练、免微调、无需修改模型架构的FramePack-U帧打包框架，两步实现恒定内存开销：1）按帧与文本prompt的语义相似度打分，结合多样性规则排序筛选帧；2）为选中帧按优先级分配不同分辨率，统一压缩到固定长度上下文窗口，将内存预算向指令相关、视觉多样性高的帧倾斜。
### 关键结果数字
在LongVideoBench、MLVU、Video-MME三个基准上，跨模型家族、参数规模、帧预算场景下均优于全分辨率基线及现有剪枝/选帧方法；在Qwen3.5-35B-A3B 128帧预算下，三个基准精度分别提升12.9%、10.6%、9.7%
