---
title: What Helps Language-Model Agents Review Violent Video? A Controlled Comparison
  with a Human Evidence Reference
title_zh: 暴力视频审核场景下LLM Agent决策架构对照实验与人类参考基准
authors:
- Mohammed El Amine Mokhtari
- Matei Mancas
- Virginie Vandenbulcke
affiliations:
- University of Mons
arxiv_id: '2611.26776'
url: https://arxiv.org/abs/2611.26776
pdf_url: https://arxiv.org/pdf/2611.26776
published: '2026-11-19'
collected: '2026-11-23'
category: Agent
direction: Agent 多模态信息传递架构优化
tags:
- LLM Agent
- Multimodal
- Controlled Experiment
- Video Moderation
- Human Evaluation
one_liner: 固定感知推理模块的对照实验证明暴力视频审核中平文本推理比肩端到端多模态模型，结构化架构准确率更低
practical_value: '- 做多模态Agent落地时优先验证平文本拼接所有感知结果的baseline，不要上来投入资源做复杂的证据图、多轮工具调用，本实验证明平文本性能最高、推理成本最低，适合快速上线

  - 短视频内容审核、商品短视频标签生成等多模态场景可加入音频事件、ASR转写特征，本场景下加入音频信息可稳定提升F1 0.012，符合人类决策的模态依赖习惯

  - 若业务需要可解释、可审计的能力，可将结构化证据图作为存储层，推理层仍采用平文本拼接所有证据的方案，兼顾可解释性和推理准确率

  - 设计Agent工具调用时避免返回孤立的检测结果，要附带上下文信息，防止模型因信息碎片化做出错误决策'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前基于LLM的多模态Agent系统普遍采用复杂的消息传递、证据图、多轮工具调用架构，但极少有研究控制变量对比不同信息传递架构本身的性能增益；同时暴力视频审核等多模态任务常忽略音频模态的价值，也缺乏人类决策时的证据依赖基准作为参考。
### 方法关键点
- 固定同一套感知模块（视频描述、目标检测、声音标签、ASR、语音语义标签）和推理模块，仅变更信息传递方式：多Agent消息传递、工具调用探索证据图、平文本一次性输入，同时对比端到端多模态模型baseline
- 构建XD-Violence数据集的人类参考基准，标注审核决策、事件时间片段、决策依赖的模态（视觉/非语音声音/语音）
- 控制变量验证音频模态、图结构边、推理模型大小、prompt改写对结果的影响
### 关键结果
- 实验在XD-Violence的799条测试clip上开展：端到端多模态模型F1=0.968，平文本输入F1=0.967，二者性能无显著差异；证据图Agent F1=0.935，消息传递F1=0.930，均显著低于平文本方案
- 加入音频事件可提升F1 0.012，和人类标注结果一致：85%以上的暴力视频人类决策时会依赖声音/语音信息
- 平文本方案的GPU推理成本约为结构化Agent的1/3，且引用证据的忠实度和结构化Agent相当
### 核心结论
对于无强多源信息冲突的多模态决策类Agent任务，将所有感知结果按时间排序为平文本输入推理模型的简单方案，性能和成本都优于复杂的结构化Agent架构
