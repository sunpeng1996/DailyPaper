---
title: 'O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking
  and Reasoning'
title_zh: O-VAD：基于对象中心跟踪与推理的工业视频异常检测框架
authors:
- Mei Yuan
- Qi Long
- Qifeng Wu
- Zhenyang Li
- Yizhou Zhao
- Lei Wang
- Yang Liu
- Min Xu
affiliations:
- Carnegie Mellon University
- University of Alabama at Birmingham
- Griffith University
arxiv_id: '2607.18142'
url: https://arxiv.org/abs/2607.18142
pdf_url: https://arxiv.org/pdf/2607.18142
published: '2026-07-19'
collected: '2026-07-28'
category: Agent
direction: Agent 工业视频异常检测推理优化
tags:
- Video Anomaly Detection
- Object-Centric Tracking
- Agentic Framework
- Zero Training
- Industrial AI
one_liner: 提出免训练的对象中心Agent框架，用于工业视频异常检测，效果超SOTA且可输出可解释报告
practical_value: '- 免训练Agent框架的设计思路可复用在多模态内容审核、工业电商品控视频异常识别场景，无需领域预训练数据就能快速冷启动

  - 对象级时空状态轨迹跟踪+推理的架构，可迁移到直播内容合规审核、电商商品外观瑕疵检测等需时序判断的多模态任务

  - 可解释异常报告的生成逻辑，可复用在需溯源的推荐负反馈归因、广告素材违规原因标注等场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM基异常推理方法在工业场景效果显著下滑，该场景存在复杂物体变换、严格物理与流程约束，传统方法需域内重训练或注入领域知识才能完成推理，落地门槛高。

### 方法关键点
提出免训练的Agent框架O-VAD，模拟人类巡检逻辑聚焦对象状态演化：先跟踪检测对象的时空动态与底层变换，再基于对象级时序状态轨迹推理，定位锚定帧中的异常对象，全程无需域内重训练或预设领域知识。

### 关键结果
在3个工业视频异常检测数据集上，性能超越经对应数据集微调的前沿VLM、Agent框架与传统VAD方法，同时可输出包含异常过程、异常类型的结构化可解释报告
