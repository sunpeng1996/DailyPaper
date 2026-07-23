---
title: 'Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning'
title_zh: Audio-Zero：面向细粒度音频推理的无标注自进化框架
authors:
- Siqian Tong
- Xuan Li
- Chaozhuo Li
- Baolong Bi
- Yiwei Wang
- Yujun Cai
- Shenghua Liu
- Chengpeng Hao
affiliations:
- Institute of Acoustics, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Beijing Academy of Artificial Intelligence
- Institute of Computing Technology, Chinese Academy of Sciences
- University of California, Merced
arxiv_id: '2607.20166'
url: https://arxiv.org/abs/2607.20166
pdf_url: https://arxiv.org/pdf/2607.20166
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态大模型 · 无标注自进化训练
tags:
- LALM
- Self-Evolution
- Label-Free Training
- Audio Reasoning
- Multimodal LLM
one_liner: 首个面向大音频语言模型的无标注自进化框架，无需人工标注即可提升细粒度音频推理能力
practical_value: '- 无标注自博弈训练范式可迁移至多模态推荐场景，用于短视频/直播音频的细粒度标签生成，大幅降低标注成本

  - 构造对比样本+自验证奖励的方法可优化电商语音搜索、智能客服的语义理解精度，减少人工标注依赖

  - 自进化自然涌现细粒度描述的结论可复用在多模态内容理解弱监督训练流程，提升细粒度特征抽取效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有大音频语言模型（LALM）在事件顺序、重复次数、时长等细粒度音频推理任务上表现较差，传统后训练方法依赖昂贵的人工标注，仅能获取粗粒度语义信号，标注成本高且难以覆盖时序类细粒度特征。
### 方法关键点
提出Audio-Zero无标注自进化框架，构造听觉自博弈游戏：基于无标注音频生成对比对，多数虚拟玩家接收参考音频，1个特殊玩家接收微调变体；模型先为每个玩家生成听觉描述线索，再通过线索不一致性识别特殊玩家，基于构造已知的特殊玩家身份生成可验证奖励，全程无需人工标注。
### 关键结果
在Qwen2-Audio-7B-Instruct、Qwen2.5-Omni-7B上实验，TREA、MMAU Test-mini、MMAR基准上细粒度音频推理能力显著提升，同时完全保留通用音频理解效果，自博弈压力下会自然涌现越来越细粒度的听觉描述。
