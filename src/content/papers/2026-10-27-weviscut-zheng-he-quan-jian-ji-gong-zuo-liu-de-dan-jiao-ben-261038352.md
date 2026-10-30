---
title: 'WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form
  Video'
title_zh: WeVisCut：整合全剪辑工作流的单Agent长脚本转视频系统
authors:
- Chenyu Mu
- Wenming Weng
- Qinrui Wang
- Xingsong Ye
- Hao Yu
- Jun He
- Chong Sun
- Chen Li
- Jing Lyu
- Erkun Yang
affiliations:
- Xidian University
- WeChat Vision, Tencent Inc.
arxiv_id: '2610.38352'
url: https://arxiv.org/abs/2610.38352
pdf_url: https://arxiv.org/pdf/2610.38352
published: '2026-10-27'
collected: '2026-10-30'
category: Agent
direction: 工具Agent · 长视频生成全流程编排
tags:
- ToolAgent
- VideoGeneration
- SFT
- RFT
- DAPO
- LoRA
one_liner: 单9B参数Agent实现脚本转长视频，效果追平Claude Opus 5，生成token成本低33倍
practical_value: '- 数据构造可借鉴：将成品内容（如电商爆款短视频、图文素材）通过反向解析+验证回放生成可执行Agent训练样本，大幅降低标注成本，可直接复用在电商AI内容生成类Agent的训练数据构造流程中

  - Agent架构可复用：采用共享状态的单统一政策替代多Agent分工，减少多Agent通信开销和决策对齐问题，适合电商智能剪辑、商品详情页自动生成等多工具调用场景

  - 训练流程可迁移：SFT→RFT→Guided-OPD→RCF-DAPO的四阶段训练流程，可迁移到电商客服Agent、商品推荐Agent等需要工具调用、错误修复的复杂Agent训练，用小参数模型逼近大模型效果，降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长视频脚本转制作多采用多Agent工作流，依赖通用大模型，成本高、跨镜头一致性差；且成品视频无中间操作轨迹，无法直接用于训练任务适配的小参数政策，质量与成本的权衡空间不明确。

### 方法关键点
- 有状态Agent框架：维护统一共享生产状态，打通规划、检索、合成、质检、修复全流程，工具调用和执行反馈直接更新状态，无固定工作流，支持多轮用户修改
- 四阶段数据流水线：对3750条成品视频做编辑反向解析恢复脚本-镜头意图，经验证回放、观察-反思-修复、轨迹具象化四步，生成13万+带工具反馈和修复结果的可执行训练样本
- 三阶段训练流程：基于Qwen3.5-9B加LoRA，先做统一SFT和运行时验证的RFT学习工具调用和基础修复，再用Guided-OPD逐步减少教师干预学习自主故障恢复，最后用RCF-DAPO算法在同角色同上下文下做相对奖励优化决策

### 关键实验
在100个脚本转视频的自建测试集上：对比基线Qwen3.5-9B，总体得分提升16分达90.5，效果追平Claude Opus 5，每成功输出1分钟视频的生成token量仅2377，比Claude Opus 5少33倍；对比竞品Crayotter，人类偏好得分高31%，生产速度快4.1倍，成本低10.8倍，可靠性提升5.1个百分点。

### 核心结论
针对特定复杂工具调用场景，基于成品反向构造可执行训练轨迹，用小参数模型做任务适配，能以远低于通用大模型的成本实现相当的效果。
