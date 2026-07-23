---
title: Keyframe-Anchored Identity Preservation for Sequential-Action Video Generation
title_zh: 基于关键帧锚定的序列动作视频生成身份一致性保持方法
authors:
- Zhenjie Liu
- Binyan Chen
- Hao Chen
- Tong Pan
- Shangfei Wang
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.17985'
url: https://arxiv.org/abs/2607.17985
pdf_url: https://arxiv.org/pdf/2607.17985
published: '2026-07-20'
collected: '2026-07-23'
category: Multimodal
direction: 多模态生成 · 身份保持文本转视频
tags:
- Text-to-Video
- Identity Preservation
- Keyframe Anchoring
- Training-free Pipeline
- Multimodal Generation
one_liner: 提出三阶段免训练框架，解决序列动作文生视频的主体身份漂移问题，获IPVG26赛道第三
practical_value: '- 电商数字人带货、商品展示短视频生成场景可复用该三阶段免训练框架，无需微调基础模型即可保证主体身份一致性，降低落地成本

  - 序列动作驱动的短视频生成可借鉴动作感知Prompt改写策略，先输出各动作终点关键帧再补全中间片段，大幅降低动作/身份漂移概率

  - 多参考引导+身份驱动噪声搜索的采样增强方法可直接迁移至AIGC短视频生成链路，有效提升主体身份保真度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
面向序列动作的身份保持文本转视频生成要求主体按指定时序执行不同动作，端到端生成器易随运动积累、动作切换出现主体外观漂移，现有方案无法适配带时间戳的结构化时序输入要求。
### 方法关键点
采用免训练三阶段pipeline：
1. 动作感知prompt打磨：将输入改写为指定各动作终点状态的图像生成prompt；
2. 身份保持关键帧生成：同时约束参考身份与前序关键帧生成序列，解耦时间不变外观与时变姿态；
3. 身份感知推理增强：通过多参考引导、身份驱动噪声搜索合成中间片段，强化采样阶段身份保真度。
### 关键结果
在IPVG26挑战赛Track 2官方榜单排名第三，性能具备竞争力且通用性强。
