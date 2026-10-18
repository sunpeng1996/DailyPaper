---
title: 'ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting
  Multiple Models'
title_zh: ARC-SORT：带交互多模型的自适应鲁棒补偿多目标跟踪方法
authors:
- Girish Kumar Adari
affiliations:
- Athlitix Inc.
arxiv_id: '2610.22306'
url: https://arxiv.org/abs/2610.22306
pdf_url: https://arxiv.org/pdf/2610.22306
published: '2026-10-15'
collected: '2026-10-18'
category: Other
direction: 多目标跟踪 · 无训练实时跟踪优化
tags:
- Multi-Object-Tracking
- Kalman-Filter
- Real-Time
- Sports-Analytics
- SORT
one_liner: 提出无需训练的实时多目标跟踪器ARC-SORT，在快动场景跟踪精度领先SOTA
practical_value: '- 不确定性自适应匹配逻辑可迁移到推荐召回/排序：给用户兴趣预测加不确定性度量，动态调整召回候选池范围，提升模糊兴趣下的匹配准确率

  - 冲突决策后置校验思路可用于多Agent任务分配/内容匹配：对低置信度匹配结果暂存冲突，后续引入补充特征修正，降低身份/物品错配概率

  - 无训练轻量化架构设计适合边缘端实时业务：可复用至线下广告屏人流跟踪、快闪店个性化内容推送等低算力场景的实时推理任务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
体育赛事直播场景多目标跟踪存在两大核心痛点：运动员运动速度快、转向突兀，同时摄像头存在平移、缩放操作，现有SORT类跟踪器匹配精度低、身份切换多。
### 方法关键点
1. 基于交互多模型（IMM）Kalman filter输出每一条轨迹的预测协方差，生成不确定性自适应的扩展IoU（EIoU）匹配区域，替代硬阈值马氏距离门限
2. 轨迹交叉时若匹配决策置信度低则留存校验，后续通过外观证据执行最多1次身份修正
3. 长时间出框目标重识别阶段丢弃运动门限，仅用外观特征关联轨迹
### 关键结果
- SportsMOT测试集HOTA达81.82，为2026年8月榜单69个方案中身份切换最少，MOTA 97.09位列第三
- DanceTrack测试集HOTA达62.1；基于Deep-EIoU公开输入时HOTA达80.31，相对基线提升3.1
- RTX3060笔记本GPU上推理速度达50FPS，单帧额外耗时<1ms
