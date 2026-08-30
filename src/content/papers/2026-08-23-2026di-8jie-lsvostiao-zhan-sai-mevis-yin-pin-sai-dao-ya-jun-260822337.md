---
title: 'Motion-Aware Reasoning from Speech to Mask Tracks: Runner-up Solution for
  the MeViS-Audio Track of the 8th LSVOS Challenge 2026'
title_zh: 2026第8届LSVOS挑战赛MeViS-音频赛道亚军方案：语音到掩模轨迹的运动感知推理
authors:
- Jinxing Zhou
- Suiyi Zhao
- Yanghao Zhou
- Ruohao Guo
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Anhui University of Science and Technology
- National University of Singapore
- China Agricultural University
arxiv_id: '2608.22337'
url: https://arxiv.org/abs/2608.22337
pdf_url: https://arxiv.org/pdf/2608.22337
published: '2026-08-23'
collected: '2026-08-30'
category: Multimodal
direction: 跨模态语音引导视频对象分割
tags:
- Speech-Guided Segmentation
- Video Object Segmentation
- Motion Reasoning
- SAM
- Challenge Solution
one_liner: 提出语音引导视频对象分割框架Speech2MaskTrack，获LSVOS 2026 MeViS音频赛道亚军
practical_value: '- 语音指令转结构化约束的思路可复用在电商语音搜索的query解析，提取品类、属性、动作需求等结构化字段

  - 多阶段候选生成→排序→结果校验的pipeline设计，可迁移到多模态召回排序场景，提升边缘case召回率

  - 大模型辅助兜底修复的策略，可借鉴到推荐/搜索bad case事后修复链路，降低人工干预成本'
score: 5
source: arxiv-cs.MM
depth: abstract
---

### 动机
语音引导的参考视频对象分割需串联语音识别、运动时序定位、掩模跟踪、无目标处理多模块，现有方案缺乏跨模态运动感知推理能力，需适配LSVOS 2026挑战赛MeViS-Audio赛道的复杂真实场景要求。
### 方法关键点
1. 先将语音查询转录为包含类别、数量、方向、交互角色、时序阶段的结构化约束；
2. 采用SAM3.1生成多实例轨迹，TRACE模块基于全轨迹运动与关系证据完成排序；
3. 用词汇存在门控抑制错误的基础预测，判定目标存在时用SaSaSa2VA轨迹替换SAM3.1生成的掩模；
4. 空输出结果进入GPT辅助修复链路，经查询与掩模级别校验后二次调用SaSaSa2VA生成结果。
### 关键结果
在LSVOS 2026 MeViS-Audio赛道官方排名中获得亚军
