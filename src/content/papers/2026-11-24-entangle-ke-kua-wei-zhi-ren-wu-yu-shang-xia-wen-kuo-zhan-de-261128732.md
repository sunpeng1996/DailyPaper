---
title: 'Entangle: Scaling Human-Video In-Context World-Action Models across Unseen
  Tasks and Contexts'
title_zh: Entangle：可跨未知任务与上下文扩展的人类视频上下文世界动作模型
authors:
- Chendong Xiang
- Chengwen Zhang
- Ruowen Zhao
- Zeyuan Wang
- Shuhe Huang
- Rongxu Cui
- Min Zhao
- Fan Bao
- Hengkai Tan
- Jun Zhu
affiliations:
- Tsinghua University
- GensPI Technology
- Motubrain
arxiv_id: '2611.28732'
url: https://arxiv.org/abs/2611.28732
pdf_url: https://arxiv.org/pdf/2611.28732
published: '2026-11-24'
collected: '2026-11-28'
category: Agent
direction: 具身Agent · 上下文动作泛化
tags:
- In-Context Learning
- World-Action Model
- Video Generation
- Contrastive Learning
- Embodied Agent
one_liner: 提出用视频生成扩增对齐数据+任务内对比损失的ICL世界动作模型，实现机器人跨未知任务操作泛化
practical_value: '- 训练数据不足场景可借鉴「用生成模型转异构数据为对齐训练对」的思路，比如跨模态用户行为数据对齐时用生成补全缺失配对

  - 模型防捷径学习可复用「同任务内对比区分正确轨迹/其他执行轨迹」的损失设计，减少推荐/Agent决策依赖浅层特征的问题

  - 多场景泛化场景可参考「可变长度输入窗口+无任务微调的ICL范式」，降低跨业务场景的微调成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
人类视频作为上下文的具身ICL世界动作模型存在两大痛点：人机任务对无时间对齐，标准损失易让策略依赖初始场景/任务ID捷径，无法跟踪上下文。
### 方法关键点
1. 用视频生成将录制的机器人视频转换为匹配的人类上下文，补充真实配对数据，规模化时间对齐的训练数据；
2. 训练结合可变长度视频窗口+任务内对比目标，区分配对动作轨迹与同任务其他执行轨迹，避免捷径学习。
### 关键结果
无任务特定微调下，Astribot S1机器人6个未知任务平均得分83.5/100；7个未知RoboTwin任务平均成功率69.5%，比Zero-WAM高22.6个百分点；Context-OOD场景下可跨重排布局、替换工具迁移行为。
