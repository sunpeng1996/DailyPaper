---
title: Tracking Any Point with Agentic Visual Reasoning
title_zh: 基于智能体视觉推理的任意点跟踪方法
authors:
- Xuweiyi Chen
- Jin Yao
- Linzhan Mou
- Lei Gong
- Di Liu
- Cheng Zhang
- Ziqiao Ma
- Sihan Xu
- Adam W. Harley
- Shengyi Qian
affiliations:
- University of Virginia
- Meta
- Princeton University
- University of Michigan
arxiv_id: '2611.34943'
url: https://arxiv.org/abs/2611.34943
pdf_url: https://arxiv.org/pdf/2611.34943
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: 视觉Agent · 时空点跟踪推理
tags:
- VLM
- Visual Agent
- Point Tracking
- Video Understanding
- Dataset
one_liner: 提出基于VLM的AgenTAP视觉智能体，无需专项微调即超过专用点跟踪模型，还构建了EgoTAP-4D数据集
practical_value: '- 可复用「自主迭代验证+预测优化」的Agent推理范式，应用到电商多模态内容理解（如商品视频关键点定位、商品轨迹追踪）场景

  - 无需领域专项微调即可超越专用模型的实现思路，可降低多模态推荐场景下定制微调的人力与数据成本

  - 零散轨迹重连的技术方案，可迁移到用户行为序列补全、跨session行为轨迹拼接等推荐侧任务'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用VLM在物体检测、视频识别等领域已超越专用视觉模型，但点匹配任务要求跨帧像素级定位同一物理点，需应对外观变化、点消失后重现等场景，是VLM的能力短板。
### 方法关键点
1. 提出AgenTAP VLM智能体，可直接预测点坐标与可见性，自主选择检查维度，用证据验证点身份并迭代优化预测结果
2. 基于AgenTAP对消失后重现的物理点重识别、拼接零散轨迹，构建长序列第一人称视角视频3D点轨迹数据集EgoTAP-4D
### 关键结果
1. 基于GPT-6 Astra实现的AgenTAP无需点对应专项微调，在点定位、可见性预测任务上均超过专用视觉模型
2. 重现点预测效果接近人类标注水平，将EgoTAP-4D加入D4RT训练后，3D跟踪平均性能获得提升
