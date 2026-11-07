---
title: Failure Prediction and Classification in Vision-Language-Action Models Via
  Calibrated Latent Probing
title_zh: 基于校准隐层探测的视觉-语言-动作模型故障预测与分类
authors:
- Michal P. Podolinsky
- Yunhao Yang
- Daniel Little
- Hong Lu
- Rohan Siva
- Olin Goudey
- Neel P. Bhatt
- Matthias Scheutz
- Ufuk Topcu
arxiv_id: '2611.08425'
url: https://arxiv.org/abs/2611.08425
pdf_url: https://arxiv.org/pdf/2611.08425
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: 具身Agent VLA模型故障检测优化
tags:
- VLA
- Failure Detection
- Latent Probing
- Calibrated Probe
- Embodied Agent
one_liner: 提出轻量隐层探针VLA-Tug，实现VLA高效校准的实时故障检测与分类
practical_value: '- 大模型在线服务故障检测可复用轻量隐层探针思路，仅增加极小推理 overhead 即可实现实时异常预警，适配边缘/低延时业务场景

  - 故障检测的校准策略可迁移到搜索推荐bad case预判场景，约束漏检/误检率的方法可直接复用在高可用服务保障模块

  - 基于轨迹前置片段监督的提前故障检测思路，可用于推荐会话负向体验预判，提前拦截bad case提升用户体验'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
Vision-Language-Action (VLA) 是具身智能核心底座，但分布偏移下性能脆弱，无预警故障易造成设备损坏、人员伤害，现有运行时监测方案无法同时满足实时性、校准性、信息完备性及边缘运行效率要求。
### 方法关键点
提出VLA-Tug轻量探测方案，在VLA backbone隐层部署极小参数量探针，基于轨迹故障前片段做监督训练，可同时输出故障检测结果、漏检/误检率约束边界、故障类型分类，推理额外开销极低。
### 关键结果
相同假阳性率下，早期故障检测能力较最优基线提升30%；unseen任务分布偏移场景下，漏检/误检率边界有效性达86%，基线最高仅21%；unseen任务故障类型top-3分类准确率较多数基线提升44%；开源3180条标注操作轨迹数据集供后续研究使用
