---
title: 'OpenCoF: Learning to Reason Through Video Generation'
title_zh: OpenCoF：通过视频生成实现推理能力学习
authors:
- Xinyan Chen
- Ziyu Guo
- Renrui Zhang
- Dongzhi Jiang
- Hongsheng Li
affiliations:
- ByteDance Seed
- CUHK MMLab
- CUHK IMIXR
arxiv_id: '2607.08763'
url: https://arxiv.org/abs/2607.08763
pdf_url: https://arxiv.org/pdf/2607.08763
published: '2026-07-08'
collected: '2026-07-10'
category: Reasoning
direction: 多模态推理 · 链式帧推理范式
tags:
- Chain-of-Frame
- Video Generation
- Reasoning Token
- Multimodal Reasoning
- Fine-tuning
- Dataset
one_liner: 提出含17K推理视频数据集的OpenCoF框架，通过双推理token提升视频链式帧推理效果
practical_value: '- 电商多模态内容生成（如虚拟试穿、商品使用流程演示）场景，可参考引入视觉+文本双推理token设计，分别捕捉低阶视觉细节和高阶语义逻辑，提升生成内容的时序合理性

  - 多模态Agent做复杂场景决策（如用户场景下的商品组合推荐、使用步骤规划）时，可借鉴Chain-of-Frame思路，将抽象推理步骤转化为可视化时序帧输出，提升决策可解释性

  - 垂直场景（如电商短视频生成、虚拟演示）的生成模型微调，可参考先构建垂直场景专属时序监督数据集再定向微调的范式，提升生成效果的任务适配性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型多基于通用语料训练，缺乏针对Chain-of-Frame（CoF，通过时序关联帧展开推理）的专用监督与设计，无法满足需要逻辑时序推导的场景需求。

### 方法关键点
1. 构建OpenCoF-17K数据集，覆盖11类推理任务的时序视频标注，提供多样化时序监督信号；
2. 对Wan2.2-I2V-A14B基线做定向微调得到Wan-CoF推理视频模型；
3. 新增视觉+文本两类推理token，分别捕捉低阶视觉线索和高阶语义先验，显式管理中间推理状态。

### 关键结果
在4个公开视频推理基准上，Wan-CoF相对基线实现显著性能提升；验证了广谱时序监督+显式中间推理状态管理机制对视频推理能力的增益作用。
