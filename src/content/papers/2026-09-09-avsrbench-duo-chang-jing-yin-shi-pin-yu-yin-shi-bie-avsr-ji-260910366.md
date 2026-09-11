---
title: 'AVSRBench: A Multi-Condition AVSR Benchmark'
title_zh: AVSRBench：多场景音视频语音识别（AVSR）基准测试集
authors:
- Rishabh Jain
- Naomi Harte
affiliations:
- Trinity College Dublin, Ireland
- Sigmedia Group, School of Engineering, Trinity College Dublin
arxiv_id: '2609.10366'
url: https://arxiv.org/abs/2609.10366
pdf_url: https://arxiv.org/pdf/2609.10366
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态语音识别 · 基准评测
tags:
- AVSR
- Benchmark
- Multimodal
- Out-of-Domain
- Evaluation
one_liner: 提出多条件AVSR评测基准，揭示现有模型跨域泛化缺陷，配套发布数据集与预处理管线
practical_value: '- 直播语音转写、虚拟人唇语识别类业务，可引入多场景测试集提前验证模型泛化能力，避免仅在标准基准上过拟合

  - 电商直播、线下导购等高噪语音交互场景，可优先做音频-视觉融合优化，该场景下融合增益最高

  - 非广播类场景的AVSR落地，尽量避免直接使用泛化预训练LLM架构，优先做目标场景小样本微调'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有AVSR模型在标准LRS3基准上WER低于1%，但训练数据多为广播域，无法验证真实复杂场景下的泛化能力，存在评估盲区。
### 方法关键点
覆盖6类真实场景（受控广播语音、固定语法表达、超清晰Lombard speech、专业/非专业唇语者朗读、多人自发对话），测试3类主流AVSR架构的跨场景表现，同步发布RoomReader-AV基准与统一数据预处理管线。
### 关键结果数字
纯视觉识别在非广播域性能骤降，90°侧脸视角下视觉理解能力暴跌，多模态系统优先回退到音频通路；音频-视觉融合仅在Lombard高噪场景增益明显；LLM-based AVSR跨域泛化表现最差，非广播域WER提升幅度超30%。
