---
title: Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable
  Grasp Synthesis
title_zh: 基于可组合基础模型先验的自适应视觉语言抓取框架
authors:
- Sixu Yan
- Shikang Wang
- Binhua Huang
- Xuanlai Tang
- Guohua Fan
- Fan Huang
- Haoxuan Li
- Yongkang Li
- Yuhan Li
- Bencheng Liao
arxiv_id: '2609.04096'
url: https://arxiv.org/abs/2609.04096
pdf_url: https://arxiv.org/pdf/2609.04096
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 机器人视觉语言抓取架构优化
tags:
- Vision-Language
- Robotic Grasping
- Foundation Model
- Modular Framework
- Generalization
one_liner: 解耦物理抓取合成与任务理解，提出无需重训即可适配多场景的自适应视觉语言抓取框架AdaRoboVLG
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视觉语言抓取（VLG）方法端到端耦合基础模型与抓取策略，依赖大规模多模态训练数据，跨任务上下文适配性差，难以泛化到不同机械臂手型。
### 方法关键点
1. 架构解耦物理抓取合成与任务相关理解：底层训练通用基础抓取策略，通过显式运动学映射、力闭合稳定性估计生成、评估物理可行的抓取候选
2. 任务理解交由专用基础模型模块，输出空间、认知、时序三类可组合先验，通过结构化接口注入抓取流程，无需重训基础策略即可适配不同上下文
### 关键结果
仿真+真实实验验证：
- 基础策略学习效率高、跨手型泛化性强
- 融合三类先验后可解决三类典型抓取挑战，性能比肩SOTA
- 多先验可协同工作，支持杂乱动态场景下的功能性抓取
