---
title: 'RynnUnify: Towards Unified Embodied Brain'
title_zh: RynnUnify：面向通用具身智能的统一多模态大脑模型
authors:
- Minghao Zhu
- Bohan Hou
- Kun Xiang
- Zixuan Wang
- Yinzhou Tang
- Yifei Yang
- Zhikai Wang
- Tianyi Zhang
- Kehan Li
- Haoyu Zhao
affiliations:
- Alibaba DAMO Academy
- Alibaba Hupan Lab
arxiv_id: '2610.32965'
url: https://arxiv.org/abs/2610.32965
pdf_url: https://arxiv.org/pdf/2610.32965
published: '2026-10-22'
collected: '2026-10-26'
category: Agent
direction: 具身Agent · 统一多模态基座研发
tags:
- Embodied Agent
- Multimodal LLM
- Long-Horizon Planning
- Reinforcement Learning
- Robot Control
one_liner: 16B参数统一具身模型，融合视频语言推理支撑长期视觉规划与机器人控制
practical_value: '- 多模态Agent工具调用路由设计可复用：用RL学习动态选择直接推理还是调用生成工具（如RAG、视频生成），平衡推理效率与准确率，可落地到电商商品咨询、售后Agent等场景

  - 三级跨chunk记忆架构可迁移到长序列多模态推荐：用固定初始锚点+历史关键帧+近期连续前缀的组合记忆方案，解决长序列生成的一致性问题，适配长用户行为序列的内容生成推荐

  - 自强迫（self-forcing）训练方法可复用：训练时对输入条件加噪、替换为模型自生成的历史输出，提升推理时对累积误差的鲁棒性，可用于生成式推荐的多步迭代生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有统一多模态模型难以支撑具身场景的长时序推理，静态视觉预测容易忽略中间动态，误差随序列长度快速累积，无法同时打通理解、规划、动作三个核心链路，制约具身Agent的落地。

### 方法关键点
- 架构基于Cosmos3的MoT架构，总参16B，拆分8B自回归推理器+8B扩散视频生成器，二者通过联合注意力交互，支持I2V、首尾帧约束生成、跨chunk续生成三种模式
- 设计三级跨chunk场景记忆：固定初始帧+2个历史关键帧+最近步参考帧的稀疏锚点，搭配前序片段的连续前缀，解决长时序生成的场景一致性问题
- 训练分三阶段：先微调推理器的理解、规划、视频prompt生成能力，再冻结推理器用自强迫策略微调生成器，最后用BCPO强化学习训练Agent动态选择直接推理/调用视频生成工具
- 扩展世界动作模型（WAM），新增动作头从生成器的视频特征输出机器人控制指令，打通从感知到动作的全链路

### 关键结果
- 具身理解任务平均得分优于所有对比的统一多模态模型，Rynn-VP长时序视觉规划得分54.8，比Cosmos 3 Nano高9.75
- Agent强化学习扩展后Rynn-GEU平均得分50.0，比直接推理高6.0
- WAM在RoboCasa365的20项复合任务成功率51.5%，3项真实机器人任务平均成功率46.7%，优于GR00T等基线

**最值得记住的一句话**：统一多模态模型通过动态调用生成工具作为中间推理证据，可同时提升理解、规划、执行全链路能力，是通用Agent落地的核心可行路径。
