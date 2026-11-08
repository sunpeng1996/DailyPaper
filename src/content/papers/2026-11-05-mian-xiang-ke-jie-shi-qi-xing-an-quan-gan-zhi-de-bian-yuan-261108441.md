---
title: Edge-Assisted Crowdsensing for Explainable Cyclist Safety Perception
title_zh: 面向可解释骑行安全感知的边缘辅助众测系统
authors:
- Hongsen Cao
- Chia-Yen Chiang
- Mona Jaber
- Meihui Wang
- Yasmin Fathy
affiliations:
- Queen Mary University of London
- Imperial College London
- University of Cambridge
arxiv_id: '2611.08441'
url: https://arxiv.org/abs/2611.08441
pdf_url: https://arxiv.org/pdf/2611.08441
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 多模态可解释感知 · 边缘众测系统
tags:
- VLM
- EBM
- Edge Computing
- Crowdsensing
- Explainable AI
one_liner: 提出边缘辅助骑行安全众测系统，用VLM+EBM实现高可解释路线安全评分预测
practical_value: '- 可解释评分类场景可复用VLM提取结构化属性+EBM建模的架构，解释性远优于黑盒模型，精度仅损失1个百分点以内，性价比极高

  - 端边协同多模态业务可参考部署方案：边缘侧完成VLM特征抽取，云端仅需CPU做0.4ms级轻量打分，平衡时延、带宽与计算成本

  - 众包数据采集场景可借鉴采样间隔调优思路：20s采样间隔仅损失1.4个精度点，可大幅降低带宽、存储与计算开销'
score: 5
source: arxiv-cs.CV
depth: abstract
---

### 动机
骑行安全事故率居高不下，自动驾驶进一步提升混合交通复杂度，现有事故统计、多模态检测方案均无法支撑线路级连续骑行安全感知，同时缺少可解释性支撑决策
### 方法关键点
1. 搭建边缘辅助众测架构：车把摄像头采集街景帧，边缘侧用单prompt驱动VLM提取结构化交通属性，融合OpenStreetMap道路基建数据、骑行运动学数据，输入EBM预测1-9分的众包安全评分
2. 基于EBM的逐特征形状函数实现精准特征归因，可直接量化各场景因素对安全评分的影响
### 关键结果
1362条伦敦路段标注帧五折交叉验证下，EBM二分类准确率达72.2%，MAE为1.011，精度仅比黑盒集成模型低不到1个百分点；特征归因量化结果：物理隔离车道+0.97分、标线自行车道+0.70分、施工区域-0.65分；20s采样间隔可支撑1000名骑手同时上传仅需54Mbit/s带宽，仅损失1.4个精度点，可落地连续监测
