---
title: 'Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for
  Omni LLMs'
title_zh: Omni-Woodpecker：基于证据-先验重平衡的全模态大模型幻觉校正
authors:
- Zijian Liu
- Chaoyou Fu
- Yan Yang
- Caifeng Shan
- Ran He
affiliations:
- 南京大学
- 中国科学院大学
arxiv_id: '2610.27103'
url: https://arxiv.org/abs/2610.27103
pdf_url: https://arxiv.org/pdf/2610.27103
published: '2026-10-19'
collected: '2026-10-22'
category: LLM
direction: 多模态大模型 · 幻觉校正
tags:
- Hallucination Correction
- Omni-LLM
- Representation Editing
- Training-free
- Multimodal Reasoning
one_liner: 训练免微调的全模态大模型幻觉校正框架，将干预从输出层转向表征层重平衡
practical_value: '- 多模态电商导购/内容推荐场景下，可直接复用该框架免微调降低跨模态幻觉，比如避免商品视频中「无介绍语音」的视觉先验压制实际音频证据，提升回答准确率

  - 表征层重平衡思路可迁移到排序模型优化：当用户个性化行为证据和全局热门先验冲突时，可在排序模型隐层做正交分解和加权调整，无需全量重训即可缓解热门马太效应

  - 冲突触发的调度机制可直接复用：仅检测到模态/证据冲突时执行额外计算，普通请求走原链路，兼顾效果优化和推理成本控制'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
全模态大模型（OLLM）已具备极强的跨模态联合推理能力，但跨模态幻觉问题严重制约落地：当多模态输入存在冲突时，模型往往会用强先验压制实际接地证据（如看到狗的视觉就默认狗在叫，忽略音频实际为静音）。现有幻觉缓解方法均在输出层做干预，无法解决多模态融合阶段就已出现的证据与先验纠缠、失衡的本质问题。

### 方法关键点
- 完全训练免微调，无需修改模型参数或语言头，适配任意开源OLLM
- 三阶段干预流程：
  1. 冲突诊断：用4种输入视图（全模态/仅音频/仅视频/仅文本）识别跨模态冲突，定位目标证据模态和竞争先验来源
  2. 正交分解：将融合隐层表征拆分为正交的接地证据子空间和竞争先验子空间，避免修正先验时损伤有效证据
  3. 自适应重平衡：根据冲突程度，在注意力路径和残差状态两个层面分别增强被压制的证据、抑制误导性先验，修正后写回原层不破坏上下文

### 关键结果
- 基于Qwen2.5-Omni-7B backbone，CMM幻觉基准准确率提升12.9个点，AVHBench提升8.6个点， hallucination resistance从57.0%提升到85.5%，与感知准确率的差距从32.5个点缩小到1.2个点
- 跨架构泛化性强：迁移到VideoLLaMA2-AV，两个基准分别提升4.6、3.9个点；4个通用OLLM推理基准一致获得0.67~2.25个点的提升
- 推理成本低：冲突触发调度下平均 latency仅为原模型的1.71~1.77倍，远低于其他对比校正方法

### 核心结论
幻觉校正应该在其产生的融合表征层执行，而非仅在输出层做事后修正。
