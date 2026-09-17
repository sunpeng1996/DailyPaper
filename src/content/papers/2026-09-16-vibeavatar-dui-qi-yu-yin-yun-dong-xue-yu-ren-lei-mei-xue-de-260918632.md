---
title: 'VibeAvatar: Aligning Phonetic Kinematics and Human Aesthetics for High-Fidelity
  Talking Avatar Synthesis'
title_zh: VibeAvatar：对齐语音运动学与人类美学的高保真说话人头像合成
authors:
- Qilin Wang
- Mingyu Li
- Hao Tang
affiliations:
- Peking University School of Computer Science
- Peking University School of Electronics Engineering and Computer Science
arxiv_id: '2609.18632'
url: https://arxiv.org/abs/2609.18632
pdf_url: https://arxiv.org/pdf/2609.18632
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 多模态说话人数字人合成
tags:
- Talking-Avatar
- Multimodal-Generation
- Flow-Model
- GRPO
- Aesthetic-Optimization
one_liner: 拆分语音精度与动作美学优化阶段，实现低显存高保真的说话人数字人生成
practical_value: '- 电商直播数字人场景可直接复用「语音精度+动作美学分阶段优化」框架，避免单模型多目标学习冲突，同时提升唇形准确率和整体观感

  - 轻量1D warp隐空间flow运动生成器可直接落地，10秒512P视频仅需<10s推理、3GB显存，适配普通GPU/边缘端部署需求

  - 后训练阶段用GRPO优化美学采样策略的思路可迁移到生成式推荐的人偏好对齐场景，无需全量重训即可提升用户主观满意度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散式说话人生成方案无法同时兼顾唇形准确率、动作美学观感与推理效率，单隐式生成器同时学习语音对齐和美学目标会出现冲突，效果不达业务落地要求。

### 方法关键点
1. 解耦两个优化目标，在条件输入阶段引入Phonetic Kinematics Adapter（PKA）将语音识别特征转换为语音运动学控制条件，保证唇形对齐精度；
2. 后训练阶段引入Aesthetic Motion Policy（AMP），通过GRPO优化流一致性随机采样策略，对齐人类动作美学偏好；
3. 基于1D warp隐运动空间的轻量流生成器，大幅压缩推理开销。

### 关键结果
客观指标、用户研究均达SOTA，生成10秒512px视频耗时<10s，仅需约3GB显存
