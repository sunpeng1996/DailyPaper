---
title: 'Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring'
title_zh: Chronos：基于时间锚定的保身份序列视频生成框架
authors:
- Mengqi Huang
- Wenchuan Wang
- Zhendong Mao
- Yijing Tu
- Zhike Liu
- Luoni Wang
- Ning Tong
- Xiaoxiao Sheng
- Tianyu Huang
- Xuecheng Qi
affiliations:
- University of Science and Technology of China
- South China University of Technology
- Huawei Inc.
- Independent Researcher
arxiv_id: '2611.05893'
url: https://arxiv.org/abs/2611.05893
pdf_url: https://arxiv.org/pdf/2611.05893
published: '2026-11-04'
collected: '2026-11-07'
category: Multimodal
direction: 多模态生成 · 保身份视频生成
tags:
- Video Generation
- Identity Preservation
- Temporal Anchoring
- Semantic Prompt
- Candidate Routing
one_liner: 提出融合多锚定与候选路由机制的保身份视频生成框架，获ACM MM 2026挑战赛双赛道第一
practical_value: '- 电商商品短视频生成场景可复用Semantic Prompt Anchoring机制，自适应优化用户输入的商品展示Prompt，提升生成内容与业务需求的匹配度

  - 多模态内容生成后处理环节可借鉴Metric-Guided Candidate Routing思路，基于多维度业务指标从多生成器输出中筛选最优结果，降低badcase出现率

  - 序列内容生成任务可引入Visual Frame Anchoring方法，插入业务相关的接地关键帧作为引导，平衡生成内容的一致性与可控性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有保身份视频生成方法仅优化静态身份对齐，导致身份保真度与时序可控性存在固有冲突，大姿态变化、多段连续动作场景下易出现身份漂移、动作抑制问题。

### 方法关键点
Chronos框架统一单段人脸身份保留与多段序列动作生成的时序建模，核心包含三大模块：
1. Semantic Prompt Anchoring：自适应优化用户原始Prompt，提升指令对齐性
2. Visual Frame Anchoring：将条件转化为具备视觉接地能力的关键帧锚点，提供可视化引导
3. Metric-Guided Candidate Routing：基于多维度评估从异构生成器输出中筛选最高质量视频

### 关键结果
在ACM MM 2026保身份视频生成挑战赛双赛道均获得第一名，人脸身份保留、序列动作生成两类场景效果均显著优于现有方案
