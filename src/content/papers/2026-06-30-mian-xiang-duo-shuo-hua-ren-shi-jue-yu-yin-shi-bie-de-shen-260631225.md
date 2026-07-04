---
title: A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR
title_zh: 面向多说话人视觉语音识别的神经形态OT-CFM首次探索
authors:
- Lin Chen
- Jingping Fang
- Hairui Liu
- Chenyang Xu
- Junhao Chen
- Xiaorui Li
- Weidong Cai
- Xiaoming Chen
affiliations:
- Beijing Technology and Business University
- Xidian University
- Tsinghua University
- The University of Sydney
arxiv_id: '2606.31225'
url: https://arxiv.org/abs/2606.31225
pdf_url: https://arxiv.org/pdf/2606.31225
published: '2026-06-30'
collected: '2026-07-04'
category: Multimodal
direction: 多模态视觉语音识别 · 神经形态计算
tags:
- VSR
- Event Stream
- OT-CFM
- Flow Matching
- Multimodal
one_liner: 提出融合事件流、OT-CFM与双层语义监督的LipsFlow框架，实现多说话人VSR的SOTA精度与低延迟
practical_value: '- 多目标场景先做跟踪+活跃检测切分单目标片段再单独建模的思路，可迁移到直播/短视频多主播口播识别、多主体商品文案提取任务

  - OT-CFM将流匹配推理压缩至2步ODE的优化方法，可复用在生成式推荐的流匹配模型推理加速，大幅降低延迟

  - token级+句子级双层语义监督消解歧义的思路，可借鉴到Query改写、商品标题生成等任务，减少同/近义表述错误'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多说话人VSR场景受头部快速运动、遮挡、唇动细微特征难捕捉影响，传统RGB方法帧率低、存在运动模糊，同时面临同形音字歧义、推理延迟高的痛点。

### 方法关键点
1. 提出LipsFlow框架，将RGB视频转换为高时间分辨率事件流，采用ByteTrack跟踪+TalkNet活跃说话人检测将多说话人场景切分为单说话人片段，可捕捉微秒级唇动动态，天然抗视觉退化。
2. 引入OT-CFM在语义隐空间强制生成确定性直线轨迹，仅需2步ODE即可完成推理，大幅压缩延迟。
3. 设计双层语义监督机制，结合token级BERT权重绑定与句子级先验，消解同形音字歧义。

### 关键结果
基准测试上取得SOTA WER 22.3%，推理延迟仅240ms。
