---
title: 'AI-Guided Learning: Research on Knowledge and Skill Acquisition Support Methods
  Using Deep Learning Audio-Video Processing Techniques'
title_zh: AI引导学习：基于深度学习音视频处理的知识技能获取支持方法研究
authors:
- Kazuki Kawamura
affiliations:
- Graduate School of Interdisciplinary Information Studies, The University of Tokyo
arxiv_id: '2608.08990'
url: https://arxiv.org/abs/2608.08990
pdf_url: https://arxiv.org/pdf/2608.08990
published: '2026-08-10'
collected: '2026-08-16'
category: Other
direction: 教育AI · 音视频内容理解与技能辅助
tags:
- AudioVideoProcessing
- DeepLearning
- MultimodalSummary
- LearningEfficiency
- SkillAssessment
one_liner: 提出覆盖音视频学习全流程的AI引导框架，落地3套提升学习效率与技能获取的系统
practical_value: '- 音素级自适应倍速的思路可迁移到电商短视频/直播场景，基于内容语义难度动态调整播放速度，提升用户内容消费效率

  - 保留核心音视觉信息的多模态摘要方法，可复用在电商商品短视频、直播回放的自动摘要生成，缩短用户种草决策路径

  - 弱标注下的用户熟练度建模方法，可迁移到电商客服、主播的话术能力自动评估与反馈系统，降低人工标注成本'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
音视频已成为主流学习介质，存在两大核心痛点：长内容顺序消费时间成本高、模仿类技能获取缺乏规模化反馈机制。
### 方法关键点
提出覆盖Consume（高效消费）、Understand（深度理解）、Imitate（技能获取）三阶段的AI引导学习框架，落地3套系统：
1. AIxSpeed：基于语音识别置信度表征听力难度，实现音素级动态调节播放速度
2. FastPerson：生成保留音视觉核心信息的多模态视频摘要，支持按章节在摘要/完整版切换
3. Profy：基于少量标注语音数据建模用户熟练度，可视化关键区域与声学距离辅助发音练习
### 关键结果
- AIxSpeed平均播放倍率达1.29x~1.30x，主观评分优于固定倍速播放
- FastPerson减少53%观看时长，知识测试得分与正常观看无统计显著差异
- Profy可显著提升用户发音清晰度，训练前后置信区间无重叠
