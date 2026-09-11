---
title: 'Echoes in the Algorithm: Analyzing the Fidelity of User Preferences Against
  Realized Platform Reach'
title_zh: 算法中的回音：用户偏好与平台实际内容触达的保真度分析
authors:
- Emelia Hughes
- Tim Weninger
affiliations:
- ND-IBM Technology Ethics Lab, University of Notre Dame
arxiv_id: '2609.09365'
url: https://arxiv.org/abs/2609.09365
pdf_url: https://arxiv.org/pdf/2609.09365
published: '2026-09-08'
collected: '2026-09-11'
category: RecSys
direction: 推荐系统用户行为 · 热度感知机制
tags:
- user behavior
- popularity cue
- content recommendation
- platform reach
- algorithmic literacy
one_liner: 通过TikTok用户实验验证无显性热度提示时用户的内容热度判断仅略高于随机且高度绑定个人偏好
practical_value: '- 设计无销量/点赞等热度提示的内容/商品feed时，不要默认用户能准确判断内容/商品实际流行度，避免误判用户点击动机

  - 可利用用户「个人偏好≈热度判断」的心理，隐藏热度指标时将用户偏好匹配内容标注为热门，提升点击意愿

  - 若平台要做去热度化的公平推荐，需补充中性热度引导，避免用户用个人偏好错误替代公共热度认知'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
内容平台隐藏/延迟展示播放量、点赞等显性热度提示时，用户仍会自发判断内容的平台实际触达度，该判断的准确性及与用户偏好的关联关系尚未被量化验证。
### 方法关键点
设计TokOrNot网页对比实验，招募363名参与者对成对TikTok视频给出两个判断：个人偏好选择、预估更高触达视频，最终和官方真实播放量数据对齐校验。
### 关键结果数字
- 用户识别高触达视频的准确率仅为56.75%（95% CI：56.01-58.55），仅略高于随机水平
- 个人偏好与高触达视频的匹配率与上述准确率接近，83.48%的实验中用户偏好与热度判断完全一致
- 不同内容品类的热度判断准确率存在显著差异
