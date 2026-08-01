---
title: 'ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics
  Representations from a Video and Its Shadow'
title_zh: ShadowDancer：基于视频阴影对学习统一动力学表征的世界模型控制
authors:
- Jin Cao
- Zian Meng
- Kaipeng Zhang
affiliations:
- Alaya Lab
- Shanghai Innovation Institute
arxiv_id: '2607.28362'
url: https://arxiv.org/abs/2607.28362
pdf_url: https://arxiv.org/pdf/2607.28362
published: '2026-07-29'
collected: '2026-08-01'
category: Other
direction: 视频世界模型 · 统一动力学表征学习
tags:
- World Model
- Dynamics Representation
- Video Generation
- Action Transfer
- Unsupervised Learning
one_liner: 构建同动力学不同外观的阴影对，通过跨阴影预测学习统一表征，实现视频世界模型无标注跨场景动作迁移
practical_value: '- 配对去冗余特征思路可复用在电商多模态商品表征学习：构造同商品不同背景/拍摄角度的样本对，提取不变商品语义，提升跨场景召回准确率

  - 无标注迁移框架可适配生成式推荐风格迁移任务：支持同款商品在不同营销场景的图生图、文案生成，无需额外标注

  - 动作迁移方案可直接落地虚拟电商直播场景：将演示视频的动作迁移到不同数字人/直播间背景，无需动作捕捉标注，降低内容制作成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型动作控制存在两类缺陷：一是动作编码松散，控制精度低；二是依赖难获取的结构化标注，仅适配单一动力学域。从演示视频学习的动作受场景外观干扰，跨场景迁移效果极差。
### 方法关键点
1. 构建大规模Shadow Library，批量生成「动作动力学完全一致、外观独立重采样」的阴影对，剥离外观与动力学的绑定关联；
2. 设计跨阴影预测预训练任务，自动过滤配对中被重采样的外观特征，保留统一动力学表征，驱动块因果世界模型，无需标注、微调即可复用演示动作。
### 关键结果
在人体运动、机器人操作、开放世界游戏等多动力学域测试，相较SOTA隐式动作、交互式世界模型基线，动作迁移、长序列生成效果显著提升，盲测平均胜率达86%
