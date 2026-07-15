---
title: 'Motion4Motion: Motion Transfer Across Subjects at Inference'
title_zh: 《Motion4Motion：推理阶段跨主体的动作迁移框架》
authors:
- Ling-Hao Chen
- Zixin Yin
- Duomin Wang
- Xianfang Zeng
- Gang Yu
affiliations:
- Tsinghua University
- The Hong Kong University of Science and Technology
- Stepfun
arxiv_id: '2607.11644'
url: https://arxiv.org/abs/2607.11644
pdf_url: https://arxiv.org/pdf/2607.11644
published: '2026-07-13'
collected: '2026-07-15'
category: Other
direction: 跨主体动作迁移 · 免训练推理方案
tags:
- MotionTransfer
- Training-free
- Cross-domain
- VideoGeneration
- ComputerVision
one_liner: 提出免训练跨主体动作迁移框架，以运动流建模替代骨架依赖，实现跨物种迁移效果优于现有基线
practical_value: '- 可复用免训练迁移思路，用于电商虚拟主播/数字人跨形象动作复刻，无需为每个虚拟形象单独做骨架标注与模型训练

  - 运动流替代骨架建模的思路，可迁移至多品类虚拟商品（宠物用品/潮玩/IP形象）的动作化展示内容生产场景

  - 跨物种动作迁移能力可用于创意电商短视频生成，大幅降低虚拟内容制作的素材采集与标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统视频动作迁移方法依赖预定义人体骨架与骨架条件训练，无法泛化到动物、异质卡通形象等非人类主体，且多类主体的骨架标注数据稀缺，限制规模化应用。
### 方法关键点
跳出骨架依赖的传统框架，提出免训练的Motion4Motion方案，通过建模视频中主体的运动流而非预设骨架，无需针对目标主体做额外标注或训练，即可在推理阶段实现跨物种、跨不同形态主体的动作迁移。
### 关键结果
实验验证效果大幅优于现有基线方法，可稳定支持人类到熊猫、鹅等不同物种的动作迁移，适配多类数字内容创作场景。
