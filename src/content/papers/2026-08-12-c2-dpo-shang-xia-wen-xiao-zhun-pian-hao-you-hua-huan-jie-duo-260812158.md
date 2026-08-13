---
title: 'Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated
  Preference Optimization'
title_zh: C2-DPO：上下文校准偏好优化缓解多模态大模型物体幻觉
authors:
- Byungoh Ko
- Jinyoung Park
- Jongha Kim
- Jeehye Na
- Jaewon Cho
- Hyunwoo J. Kim
affiliations:
- Korea University
- KAIST
arxiv_id: '2608.12158'
url: https://arxiv.org/abs/2608.12158
pdf_url: https://arxiv.org/pdf/2608.12158
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 多模态大模型 · 偏好优化 幻觉缓解
tags:
- DPO
- MLLM
- Hallucination
- Preference Optimization
- LoRA
one_liner: 提出上下文偏好增益（CPG）指标定位DPO上下文盲视问题，设计C2-DPO大幅降低MLLM物体幻觉率
practical_value: '- 多模态商品理解、搜图、短视频带货文案生成场景，可直接复用C2-DPO训练目标，在现有偏好优化数据基础上新增上下文降级分支，无需额外标注即可降低生成幻觉，避免商品属性描述错误

  - 构建多模态偏好数据集时，可引入CPG指标做模型对齐效果的离线评估，CPG越高说明模型越能充分利用上下文（如商品属性标签、图片描述），幻觉率越低

  - 现有DPO、SimPO等偏好优化框架可快速集成上下文校准正则项，适配纯文本场景（如商品文案生成、客服话术对齐），可提升事实一致性同时不损失通用推理能力

  - 依赖多模态输入的电商Agent（如图导购、直播内容审核），用C2-DPO做对齐可提升对输入上下文的利用率，减少错误推荐/回复'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MLLM在视觉问答、内容生成等场景应用广泛，但存在严重的物体幻觉问题，生成内容与输入视觉/文本上下文不符，严重影响业务可靠性。现有DPO类偏好优化方法通过对齐偏好数据缓解幻觉，但从未验证模型是否真正利用了输入的上下文信息，存在天然的上下文盲视缺陷，导致幻觉优化效果天花板低。

### 方法关键点
- 提出Contextual Preference Gain（CPG）指标：量化模型在完整上下文vs降级上下文下，对正确响应的偏好差值，CPG与幻觉率呈强负相关，可直接反映模型利用上下文的能力
- 设计C2-DPO训练目标：在标准DPO损失基础上新增两个正则项，一是上下文校准损失，最大化完整上下文与降级上下文的偏好差值（即CPG）；二是降级上下文DPO损失，确保无额外上下文时模型仍能保持正确的偏好排序
- 适配性极强：可无缝集成到SimPO、RDPO等其他偏好优化框架，同时支持多模态、纯文本两类场景

### 关键实验
测试覆盖Object HalBench、HallusionBench等幻觉评估基准，以及ScienceQA、MM-Vet等通用多模态推理基准，对比推理端、训练端共10余种基线方法。核心结果：Qwen2-VL-Instruct-2B的Object HalBench响应级幻觉率相对降低36%，提及级幻觉率相对降低60%，同时通用推理能力无损失；纯文本场景下在AlpacaEval 2上相较基线DPO胜率提升2.3%。

### 最值得记住的一句话
现有DPO类方法存在天然的上下文盲视问题，显式优化模型对上下文的偏好增益是在不损失通用能力前提下降低幻觉的高效路径。
