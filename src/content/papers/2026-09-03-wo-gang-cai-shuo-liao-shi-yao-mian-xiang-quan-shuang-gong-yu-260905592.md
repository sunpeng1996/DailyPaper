---
title: What Did I Just Say? Self-Listening for Full-Duplex Speech Models
title_zh: 我刚才说了什么？面向全双工语音模型的自监听机制
authors:
- Xuanning Zhou
- Junyi Ao
- Xiaotong Liu
- Tom Ko
- Benyou Wang
- Haizhou Li
affiliations:
- Shenzhen Loop Area Institute, China
- The Chinese University of Hong Kong, Shenzhen, China
arxiv_id: '2609.05592'
url: https://arxiv.org/abs/2609.05592
pdf_url: https://arxiv.org/pdf/2609.05592
published: '2026-09-03'
collected: '2026-09-10'
category: Agent
direction: 全双工语音对话Agent 中断恢复优化
tags:
- Full-Duplex
- Speech Agent
- Interruption Recovery
- Self-Listening
- Conversational AI
one_liner: 自监听机制+AnchorSpeech数据集，解决全双工语音模型的中断锚定问题
practical_value: '- 智能语音导购/客服Agent可直接复用自监听机制，将实际播报的语音回流为输入，避免中断后重复播报或跳项，提升对话体验

  - 结构化多步骤语音引导场景（如售后流程、支付指引）可借鉴AnchorSpeech的标注思路，追踪已完成播报的节点，实现中断后精准续接

  - 异步多模块（生成/合成/播报）的交互系统可引入「实际输出回流校验」逻辑，解决各模块异步导致的状态不一致问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
全双工语音模型可实现边听边说，支持中断、反馈词等丰富交互，但文本生成、语音合成、音频播放三个环节异步，导致模型侧记录的已输出内容与用户实际听到的内容存在偏差，中断后无法准确锚定已播报节点续接，即锚定中断问题。

### 方法关键点
1. Self-Listening机制将用户语音、模型生成文本、模型实际播放语音三路流交错作为输入，把实际播报的语音回流到模型输入层，让中断恢复完全基于用户真实收听到的内容。
2. AnchorSpeech数据集包含同质训练/测试拆分，标注了结构化有序响应中实际已播报的条目，测试集专门评估模型在中断后能否与最后一个完成播报的条目保持响应一致性。

### 关键结果
对比全双工基线模型，搭载自监听机制的模型锚定性能获得显著提升。
