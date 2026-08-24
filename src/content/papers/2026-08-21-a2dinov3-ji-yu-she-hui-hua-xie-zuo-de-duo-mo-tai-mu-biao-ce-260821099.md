---
title: 'A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration'
title_zh: A2DINOv3：基于社会化协作的多模态目标检测优化方案
authors:
- Jiekang Feng
- Zhihe Fan
- Yunqi Zhu
- Xinjie Yao
- Yueying Zhang
- Yike Gao
- Ranxin Li
- Guanzuo Chen
affiliations:
- School of Artificial Intelligence, Tianjin University
- School of Sports Training, Tianjin University of Sport
- School of Computer Science and Engineering, University of New South Wales
- Faculty of Information Engineering and Automation, Kunming University of Science
  and Technology
arxiv_id: '2608.21099'
url: https://arxiv.org/abs/2608.21099
pdf_url: https://arxiv.org/pdf/2608.21099
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态目标检测 · 跨模态融合优化
tags:
- Multimodal Object Detection
- Cross-Modal Fusion
- DINOv3
- Expert Collaboration
- Adapter Tuning
one_liner: 提出带社会化协作协议的多专家融合框架A2DINOv3，适配DINOv3实现多模态目标检测SOTA
practical_value: '- 跨模态融合场景可借鉴「异构专家独立保留预训练先验+选择性约束交互」的思路，避免强制无差别融合破坏单模态预训练效果，可复用在电商多模态推荐的图文/行为/视频模态融合任务中

  - 跨模态适配阶段的零初始化逐步激活协作策略，可迁移到多模态大模型微调场景，降低微调对预训练基础能力的损耗，缓解灾难性遗忘问题

  - 社会化协作协议的设计思路可复用在多Agent系统的跨角色信息交互规则制定，减少无效信息传递与干扰'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态目标检测的密集跨模态融合方案强制异构模态无差别交互，易引入冗余信息、破坏DINOv3等视觉基础模型的预训练表征，无法适配低光、恶劣环境下的鲁棒检测需求。

### 方法关键点
1. 从社会化学习视角设计多专家协作框架A2DINOv3，提出Socialized Collaboration Protocol (SCP)，将RGB、红外分支建模为异构专家，独立保留专属知识，仅通过选择性约束交互传递互补信息，避免跨模态干扰、保护预训练先验
2. 引入零初始化策略逐步激活跨模态协作，实现从单模态学习到协同表征学习的平滑过渡

### 关键结果
在GAIIC（航空检测）、FLIR（自动驾驶）、LLVIP（低光监控）、M3FD（复杂真实场景）4个多模态基准数据集上均取得SOTA性能
