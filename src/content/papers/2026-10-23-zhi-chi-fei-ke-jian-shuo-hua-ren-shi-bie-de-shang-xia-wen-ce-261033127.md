---
title: 'Beyond Visible Speakers: Context-Aware Active Speaker Detection with Speaker
  Registration'
title_zh: 支持非可见说话人识别的上下文感知主动说话人检测
authors:
- Pu Wang
- Hugo Van hamme
affiliations:
- KU Leuven, Department of Electrical Engineering, Leuven, Belgium
arxiv_id: '2610.33127'
url: https://arxiv.org/abs/2610.33127
pdf_url: https://arxiv.org/pdf/2610.33127
published: '2026-10-23'
collected: '2026-11-01'
category: Multimodal
direction: 多模态音视频融合 · 主动说话人检测
tags:
- Active Speaker Detection
- Audio-Visual Fusion
- Multimodal Learning
- Context Reasoning
- Speaker Registration
one_liner: 提出两款带上下文与身份感知推理的ASD模型，支持检测视觉不可见活跃说话人，多基准达SOTA
practical_value: '- 直播/短视频场景的语音字幕匹配、互动发言归因可复用跨候选人脸的上下文补全推理逻辑，解决人脸遮挡、角度偏斜下的说话人识别问题

  - 虚拟主播、多Agent语音交互场景可借鉴说话人注册表征方案，实现无视觉输入时的发言人身份判定

  - 多模态融合任务中可参考目标信息缺失时引入互补模态/候选特征补全的思路，提升极端场景下的模型鲁棒性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有主动说话人检测（ASD）依赖语音与可见人脸的音视对应，在拥挤场景、人脸视觉证据缺失（遮挡/出框）时准确率大幅下降，真实落地场景鲁棒性不足。

### 方法关键点
基于ROAM-ASD扩展出两个优化版本：
1. ROAM-ASD-C：对同一场景下所有可见候选人脸做联合推理，目标观测模糊/不完整时调用其他人脸特征提供互补证据
2. ROAM-ASD-CR：引入从注册语音提取的说话人表征，支持检测视觉不可见的活跃说话人

### 关键结果
ROAM-ASD-C在5个ASD基准上达SOTA：AVA数据集mAP 96.8%，WASD 98.9%，UniTalk 88.8%，Talkies 98.7%，ASW 99.5%；在75%目标轨迹视觉信息被移除的极端场景下，比原ROAM-ASD的mAP最高提升13.3
