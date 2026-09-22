---
title: 'SteerDuplex: Steerable Duplex Speech Dialogue Models'
title_zh: SteerDuplex：可调控的全双工语音对话模型
authors:
- Utkarsh Tyagi
- Ramaneswaran Selvakumar
- Advait Gosai
- Sonal Kumar
- Nikhil Barhate
- Isabell Sagar
- Steven Li
- Miheer Bavare
- Daniel Quigley
- Fabiola Tapia Carrillo
affiliations:
- Scale AI
- University of Maryland
arxiv_id: '2609.12623'
url: https://arxiv.org/abs/2609.12623
pdf_url: https://arxiv.org/pdf/2609.12623
published: '2026-09-10'
collected: '2026-09-22'
category: Agent
direction: 语音对话Agent 可调控性优化
tags:
- Spoken Dialogue
- Full Duplex
- Reinforcement Learning
- Steerability
- Benchmark
one_liner: 提出可调控全双工语音模型SteerDuplex与配套评测基准，结合混合奖励RL优化交互表现
practical_value: '- 搭建电商语音导购/客服类Agent时，可复用双阶段混合奖励RL方案，同时优化中断响应、插话抑制等时序指标和内容合规性

  - 评估语音类交互Agent能力时，可参考SteerBench的多维度人工rubric设计思路，兼顾行为属性（语速、语气）和任务完成度

  - 微调语音交互模型时，可采用自然对话+合成对话混合的训练数据构造方式，同时覆盖指令遵循、交互逻辑等多维度训练目标'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有全双工语音对话模型支持低延迟轮次、中断处理等能力，但缺失可调控性，无法根据用户指令可靠调整语气、人设、语速等对话属性，存在明显能力缺口。
### 方法关键点
1. 构建文本+音频维度的可调控性分类体系，明确现有模型短板；
2. 基于Moshi底座微调得到SteerDuplex，采用自然对话+合成对话混合训练数据，覆盖指令遵循、发声表达、推理、双工交互目标；
3. 引入双阶段RL，混合可验证交互检查、裁判语义反馈两类reward，优化时序表现与响应连续性；
4. 发布SteerBench评测基准，包含390条语音prompt、1067条人工标注二元评估规则，覆盖多维度调控属性。
### 关键结果
SteerBench上音频调控平均通过率较最优开源基线高44.5pp；Audio MultiChallenge任务平均通过率高7pp；RL优化后无噪场景中断响应率从72.5%升至82.5%，合成停顿插话率从26.5%降至9%。
