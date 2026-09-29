---
title: 'Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents'
title_zh: 长周期多模态Agent的检索后记忆投递机制优化
authors:
- Yuhang Jiang
- Qingwei Liao
- Kaize Yin
- Xingling Liu
- Luca Cuomo
- Silvio Bacci
affiliations:
- Huawei Technologies Ltd.
- Huawei Pisa Research Center
arxiv_id: '2609.32590'
url: https://arxiv.org/abs/2609.32590
pdf_url: https://arxiv.org/pdf/2609.32590
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: 多模态Agent长时记忆机制优化
tags:
- Multimodal Agent
- Long-term Memory
- RAG
- Retrieval
- Prompt Engineering
one_liner: 拆分多模态Agent记忆检索与投递阶段，提出无训练DeliverMem框架大幅提升长周期任务准确率
practical_value: '- 多模态RAG系统不要直接丢弃原始像素存文本摘要，细粒度信息提取场景投递原始模态可带来10%+准确率提升，尤其适配商品详情识图、用户晒单问答类电商业务

  - 检索到的多模态结果可借鉴Set-of-Mark思路给每个条目渲染唯一视觉标签，绑定时序信息，无需训练即可提升LVLM对结果的寻址利用率，适配长会话、多轮交互推荐场景

  - 小区域视觉检索场景可采用整图+2×2切块的多向量MaxSim召回，不增加存储成本的前提下提升细粒度视觉线索的召回准确率，适配电商同款检索、商品属性识别类任务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态Agent记忆研究集中在存储、检索阶段，完全忽略了检索后到模型输入之间的「投递」环节对准确率的影响；现有方案常将图像转成文本摘要存储投递，丢失大量细粒度视觉信息，频繁出现检索到正确记忆但模型仍答错的问题，MemLens基准上这类错误占比高达30%以上。

### 方法关键点
- 拆分记忆pipeline为存储、检索、投递三个独立阶段，固定检索结果时仅改变投递形式即可量化投递环节的独立增益
- 提出无训练的DeliverMem框架，核心包含3个零成本投递策略：保留原始模态（不将图像转文本摘要）、给每个投递条目渲染唯一可读视觉标签、标注记忆的时序/位置信息
- 搭配检索侧轻量适配器，采用整图+2×2切块的SigLIP 2多向量MaxSim召回，优化小区域视觉线索的检索准确率

### 关键实验结果
- MemLens多模态长对话记忆基准上，8B参数量模型下投递原始像素比仅投递文本准确率提升13.87个点，而将检索优化到完美仅提升2.31个点，投递环节增益远高于检索
- DeliverMem在MemLens所有4种上下文长度下均超过现有SOTA记忆Agent，32K上下文下仅用1/10的输入量即可达到前沿闭源LVLM读全量上下文的效果
- DMV-Bench视觉记忆基准上，DeliverMem在所有设置下均超过原SOTA DualMem，J=50长周期场景下最高领先23.5个点

### 最值得记住的一句话
在多模态长时记忆系统中，优化检索到的记忆以何种形式送达模型，投入产出比远高于单独优化检索准确率
