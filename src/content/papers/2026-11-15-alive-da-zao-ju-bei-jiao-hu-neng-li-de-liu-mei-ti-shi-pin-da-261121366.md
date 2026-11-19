---
title: 'ALIVE: Making Streaming Video Models Interactive'
title_zh: ALIVE：打造具备交互能力的流媒体视频大模型
authors:
- Jinzhao Li
- Yuan Xu
- Jinxuan Wu
- Yukun Wang
- Yijia Lei
- Hanyu Ji
- Yinuo Chen
- Zining Huang
- Chi Zhang
- Hang Ye
affiliations:
- Tsinghua University
- Peking University
- ByteDance
- Beihang University
- University of Wisconsin–Madison
arxiv_id: '2611.21366'
url: https://arxiv.org/abs/2611.21366
pdf_url: https://arxiv.org/pdf/2611.21366
published: '2026-11-15'
collected: '2026-11-19'
category: Agent
direction: 多模态Agent · 流媒体视频交互
tags:
- Multimodal Agent
- Streaming Video
- Contrastive SFT
- Reinforcement Learning
- Interactive LLM
one_liner: 通过对比SFT和BACA强化学习两阶段训练，赋予流媒体视频大模型主动交互全能力
practical_value: '- 两阶段训练范式可迁移到主动交互类Agent场景：先做对比SFT对齐行为逻辑，再用RL结合全局+局部信用分配优化实际交互效果，适合电商直播实时导购、内容平台主动提醒类Agent开发

  - 对比SFT的设计思路可复用：通过构造相同输入不同交互条件的正负样本，教模型判断响应时机、选择交互策略，可直接用于推荐系统的主动触达时机优化

  - BACA信用分配方法可借鉴：将多轮交互的轨迹奖励拆解到不同行为单元（策略选择、响应、静默），解决多轮RL中信用分配模糊的问题，适合多轮交互类任务的RL优化

  - 交互数据集构造流程可复用：先做证据时序对齐，再合成对话，最后校验因果合理性，可用于构建电商场景下的实时交互训练数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流媒体视频大模型多为被动响应，无法处理动态变化的用户任务、主动索取缺失信息，限制了其作为多模态交互助手的落地潜力，难以适配直播导购、实时内容推荐等需要动态交互的场景。

### 方法关键点
- 数据侧：构造ALIVE-SFT-288K、ALIVE-RL-3K两份数据集，覆盖主动监控、流任务协调、反馈索取三类核心交互能力，同步推出FSI-Bench专门评测反馈索取交互效果
- 第一阶段对比SFT：构造响应门控对比、交互策略对比两类样本，教模型在相似视觉输入下根据交互状态判断是否响应、选择合适策略，同时平衡静默和响应的损失权重避免偏向单一行为
- 第二阶段RL优化：提出Behavior-Aligned Credit Assignment (BACA)，结合轨迹级全局奖励和行为单元级局部奖励，解决多轮交互中信用分配模糊的问题，同时加入冗余响应惩罚提升交互效率

### 关键结果
在OVO-Bench、StreamingBench、IPIBench、ProactiveVideoQA四个公开基准上均达到SOTA，其中IPIBench得分40.3，超过次优基线AURA 18.7个点；自研FSI-Bench上EDP协议准确率52.8%，超过GPT-6 Astra 10.6个点，FDP协议准确率54.0%，超过GPT-6 Astra 23.9个点。

### 核心结论
被动感知模型转化为主动交互助手，仅靠通用SFT远不够，必须针对交互逻辑做对比训练，再结合细粒度信用分配的RL优化才能达到可用水平。
