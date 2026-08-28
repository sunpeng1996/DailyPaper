---
title: 'Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual
  Information'
title_zh: 检索头结合视觉：揭示多模态大模型定位提取视觉信息的机制
authors:
- Chanho Park
- Daehyeon Choi
- Jihyun Lee
- Minhyuk Sung
affiliations:
- KAIST
- Independent Researcher
arxiv_id: '2608.27417'
url: https://arxiv.org/abs/2608.27417
pdf_url: https://arxiv.org/pdf/2608.27417
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态大模型 · 视觉检索头机制研究
tags:
- VLM
- Attention Head
- Visual Grounding
- Retrieval Head
- Multimodal Reasoning
one_liner: 发现VLM中占比1.7-2.6%的视觉检索头是文本到图像区域因果对齐的核心组件
practical_value: '- 多模态商品检索场景：可通过定位VRHs优化VLM的图文匹配精度，减少无关商品召回，同时降低推理计算开销

  - 多模态Agent任务（如商品问答、搭配引导）：可优先微调VRHs模块，用少量数据快速提升视觉定位准确性，成本远低于全量微调

  - 多模态生成式推荐场景：屏蔽非VRH的冗余注意力头，可在不影响图文对齐效果的前提下压缩KV cache占用，提升推理吞吐量'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLMs可根据文本提示定位对应图像区域并输出关联视觉信息，但其内部作用机制尚不清晰，参考LLM的检索头相关研究，探索VLM中是否存在类似的视觉检索机制。

### 方法关键点
将现有注意力头打分方法统一到包含查询token、key聚合、跨样本聚合三个维度的设计空间下，通过计算输出预测token的注意力在真实指代区域的求和值，识别出因果相关的注意力头，定义为Visual Retrieval Heads (VRHs)。

### 关键结果数字
VRHs仅占总注意力头的1.7-2.6%；在11款VLM、5个指代表达基准测试中，仅屏蔽Top20 VRHs可使定位准确率最高下降80个百分点，屏蔽相同数量随机头几乎无影响；VRHs可跨视觉参考任务泛化、功能特定，且在共享LLM backbone的不同VLM间可迁移。
