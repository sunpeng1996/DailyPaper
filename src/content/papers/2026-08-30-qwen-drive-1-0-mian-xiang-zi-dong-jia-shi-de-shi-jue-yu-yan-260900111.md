---
title: 'Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model
  for Autonomous Driving'
title_zh: Qwen-Drive-1.0：面向自动驾驶的视觉语言基础模型初探
authors:
- Xin Zhou
- Zongchuang Zhao
- Zhibo Yang
- Mingsheng Li
- Humen Zhong
- Shuai Bai
- Du Chu
- Ruizhe Chen
- Zhaohai Li
- Jun Tang
affiliations:
- Qwen Team
- Huazhong University of Science and Technology
arxiv_id: '2609.00111'
url: https://arxiv.org/abs/2609.00111
pdf_url: https://arxiv.org/pdf/2609.00111
published: '2026-08-30'
collected: '2026-09-03'
category: Multimodal
direction: 多模态大模型 · 自动驾驶统一多任务框架
tags:
- VLM
- Autonomous Driving
- BEV Perception
- Motion Planning
- Multimodal Foundation Model
one_liner: 基于预训练VLM架构，统一集成3D感知、VQA和运动规划的自动驾驶多任务基础模型
practical_value: '- 统一多任务架构可复用：基于通用大模型底座加领域专属任务头的设计，可迁移到推荐系统多任务预估（CTR/CVR/收藏率）场景，共享底层表征提升整体效果

  - 分阶段训练策略可借鉴：微调时混合通用预训练数据与领域监督数据，能在提升领域任务效果的同时避免大模型原有通用能力的灾难性遗忘，适合LLM4Rec微调

  - 可解释探测头设计思路可复用：在共享表征层外挂独立可解释的探测模块，可用于LLM4Rec场景下黑盒大模型表征的可解释性分析与效果验证'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有自动驾驶方案多为单任务定制架构，难以同时兼顾感知、推理、规划全链路能力，且通用VLM迁移到垂直领域时易丢失原有通用视觉理解、指令跟随能力。

### 方法关键点
1. 沿用预训练VLM底座架构，统一整合3D感知、VQA、运动规划三大核心任务，底层表征全局共享
2. 外挂独立BEV感知头，同时实现3D目标检测、语义占用预测、BEV地图分割，提供可解释的3D场景结构交互接口
3. 基于共享VLM表征的规划专家模块生成自车未来行驶轨迹
4. 采用分阶段训练范式，混合通用VLM数据与自动驾驶领域监督数据训练，平衡通用能力保留与领域性能提升

### 关键结果
3D感知与驾驶场景理解效果优异，保留大部分通用VLM能力，开环、伪闭环、闭环全场景评测下运动规划性能达到极具竞争力的主流SOTA水平。
