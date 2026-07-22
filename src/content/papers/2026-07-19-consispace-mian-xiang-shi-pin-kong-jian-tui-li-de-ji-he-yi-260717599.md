---
title: 'ConsiSpace: Learning Geometric Consistency Matters for Video Spatial Reasoning'
title_zh: ConsiSpace：面向视频空间推理的几何一致性学习方法
authors:
- Ting Huang
- Zhenyu Zhang
- Wenyuan Huang
- Jian Yang
- Hao Tang
affiliations:
- Nanjing University
- Peking University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2607.17599'
url: https://arxiv.org/abs/2607.17599
pdf_url: https://arxiv.org/pdf/2607.17599
published: '2026-07-19'
collected: '2026-07-22'
category: Reasoning
direction: 多模态大模型 · 视频空间推理
tags:
- MLLM
- Spatial Reasoning
- Video Understanding
- Self-supervised RL
- Memory Mechanism
one_liner: 提出融合几何一致性记忆与自监督RL的视频空间推理框架，跨基准较最强基线平均提分12.6点
practical_value: '- 多模态商品/场景理解任务可复用几何一致性记忆（GCM）的门控融合机制，减少冗余视频帧特征的存储与计算开销，提升推理效率

  - AR导购、多视角商品属性识别场景可引入统一一致性自监督RL信号，优化跨视角预测稳定性，降低不一致输出带来的用户体验损失

  - 视觉导航类Agent、室内场景交互任务可将空间拓扑/几何一致性作为SFT后辅助优化目标，无需额外标注即可提升推理精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM以语义为核心，无法可靠聚合冗余视频观测中的一致性空间证据，在视角变化的长时序空间推理任务中效率低、稳定性差，难以支撑导航类感知、长视频QA等场景落地。
### 方法关键点
1. 提出几何一致性感知的ConsiSpace框架，将空间一致性同时作为证据组织原则与SFT后显式学习信号
2. 构建几何一致性记忆（GCM），融合隐式证据token与显式几何线索，通过门控写入、融合策略压缩存储任务相关空间证据，降低冗余
3. 监督微调后引入统一一致性自监督强化学习（UC-SSRL），结合答案、度量、拓扑三类一致性奖励优化跨视角推理稳定性
### 关键结果
在VSI-Bench、OSI-Bench、MMSI-Video-Bench三个空间推理基准上取得一致提升，较最强基线平均得分提升12.6点
