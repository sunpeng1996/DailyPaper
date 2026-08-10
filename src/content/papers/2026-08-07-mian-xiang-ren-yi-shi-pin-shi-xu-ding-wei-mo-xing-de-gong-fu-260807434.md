---
title: Conformal Coverage Guarantees for Any Video Temporal Grounder
title_zh: 面向任意视频时序定位模型的共形覆盖率保证
authors:
- Aseel Mohamed
- Rasul Khanbayov
- Erchin Serpedin
- Hasan Kurban
affiliations:
- Texas A&M University at Qatar
- Hamad Bin Khalifa University
- Texas A&M University, College Station
arxiv_id: '2608.07434'
url: https://arxiv.org/abs/2608.07434
pdf_url: https://arxiv.org/pdf/2608.07434
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 视频时序定位 · 共形预测校准
tags:
- Conformal Prediction
- Video Temporal Grounding
- Model Agnostic
- Uncertainty Calibration
- Post-hoc Processing
one_liner: 提出模型无关后处理工具COVER，为任意视频时序定位模型提供概率可控的真值区间覆盖保证
practical_value: '- 电商短视频/直播商品高光定位、片段检索场景可直接复用该后处理方案，无需重训已有模型即可获得置信度可控的定位区间，降低badcase率

  - 后处理校准思路可迁移到搜索推荐召回/排序结果置信度预估场景，基于留出集校准非一致分位数，为业务提供可解释的效果保证

  - 黑盒模型适配的框架可复用在多模态LLM推理结果正确性校验环节，无需访问模型权重即可输出可靠性标注'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
视频时序定位的事件边界存在天然歧义，标注真值是区间分布，但现有模型仅输出单一定位区间且无可靠性说明，部署时无法区分结果正误，业务风险不可控。
### 方法关键点
1. 提出模型无关的后处理wrapper COVER，无需重训、无需白盒访问，可适配任意时序定位器或黑盒多模态模型；
2. 基于留出集的时序非一致分位数校准，将基础预测区间拓展为满足1-α概率覆盖真值的置信区间；
3. 提供两类非一致得分族：适配区间输出模型的双边边界拓展得分、适配相关性信号输出模型的超水平集得分，同时给出置信区间大小的理论上界。
### 关键结果数字
在3个基准数据集、5个时序定位模型上测试，实际覆盖率完全贴合预设目标；针对标称0.8覆盖率的专用不确定度时序定位模型，可将其实际覆盖率从0.66修复至达标，同时可定位模型误差集中在偏移边界的结构性问题。
