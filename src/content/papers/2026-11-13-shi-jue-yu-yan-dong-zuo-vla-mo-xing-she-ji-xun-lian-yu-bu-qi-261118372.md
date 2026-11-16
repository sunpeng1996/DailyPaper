---
title: 'Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and
  Deployment'
title_zh: 视觉-语言-动作（VLA）模型：设计、训练与部署全生命周期综述
authors:
- Suvarna Kadam
- Soran Parsa
affiliations:
- Witsense AI
- University of Huddersfield
arxiv_id: '2611.18372'
url: https://arxiv.org/abs/2611.18372
pdf_url: https://arxiv.org/pdf/2611.18372
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 多模态具身智能 · VLA全生命周期综述
tags:
- VLA
- Vision-Language Model
- Embodied AI
- Survey
- Model Training
- Model Deployment
one_liner: 梳理2022-2026年88篇VLA工作，按7维度拆解全生命周期技术路径与行业趋势
practical_value: '- VLA的多模态输入-记忆-输出管线设计可复用至多模态Agent的感知-决策-行动链路优化

  - 预训练多源数据混合策略（领域+公共+模拟数据）可迁移至多模态推荐/Agent的训练数据配比优化，降低垂直场景标注成本

  - <1B小参数模型适配消费级GPU的微调、部署方案可复用至端侧推荐/Agent的轻量化落地

  - VLA的鲁棒性测试思路可借鉴至推荐/Agent的泛化性评估，规避基准分高但实际业务表现差的问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
具身机器人领域此前缺乏针对VLA模型全生命周期的系统性梳理，技术选型、训练部署路径无统一参考框架。
### 方法关键点
沿7个核心维度覆盖VLA全链路：4个设计维度（输入与记忆、架构、动作输出、中间预测）、2个训练维度（预训练数据、后训练适配）、1个部署维度（实时执行），横向对比22款主流VLA的核心参数。
### 关键结果数字
- 覆盖2022.12-2026.10共88篇VLA相关工作
- 三大行业趋势：训练数据从1万小时遥操作数据拓展至2.3万社区采集片段+2万小时第一人称人类视频；模型规模分层，主流为3-7B，新增<1B小模型可在消费级GPU运行；通用VLA涌现，支持操纵+导航双任务
- 发现部分基准测试满分的VLA在物体/摄像头微小变动下性能骤降的泛化性缺陷
