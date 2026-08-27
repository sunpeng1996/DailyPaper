---
title: 'GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities
  with a Three-System Architecture'
title_zh: GigaBrain-0.7：基于三系统架构的具身基础模型缩放实现涌现能力
authors:
- GigaBrain Team
- Angen Ye
- Axiang Sun
- Can Jin
- Chenxi Cheng
- Chong Shi
- Dengke Shang
- Dingqian Zhang
- Guan Huang
- Guangqiang Wang
affiliations:
- GigaBrain Team
- GigaAI
arxiv_id: '2608.15875'
url: https://arxiv.org/abs/2608.15875
pdf_url: https://arxiv.org/pdf/2608.15875
published: '2026-08-15'
collected: '2026-08-27'
category: Agent
direction: 具身Agent · 三系统架构优化
tags:
- Embodied Agent
- VLA Model
- Foundation Model
- System Architecture
- Zero-shot Generalization
one_liner: 提出三系统架构具身基础模型，跨多机器人形态零样本任务泛化能力大幅提升
practical_value: '- 三系统分层架构可迁移至多模态电商导购Agent，分别对应意图理解规划、用户需求预判、落地执行动作生成，提升多场景泛化能力

  - 异构多源数据预训练+单阶段联合对齐范式可复用至LLM4Rec系统，同时优化语义理解与推荐结果生成效果

  - 零样本泛化优化思路可参考用于冷启动场景推荐/导购Agent适配，大幅降低新场景微调数据量需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA具身Agent存在架构设计效率偏低、异构数据适配性差、跨任务跨形态泛化能力不足的行业痛点。

### 方法关键点
1. 采用三系统协同架构：拆分理解规划（VLM/VLA模块）、动作控制（经验驱动RL，输入实机/仿真/世界模型生成多源数据）、预测评估（世界模型+人在回路数据）三个模块解耦优化
2. 预训练使用超37000小时异构具身数据
3. 采用单阶段对齐训练，联合优化视觉语言理解与多形态动作生成

### 关键结果
相比前代GigaBrain-0系列与SOTA模型π₀.₅，零样本基础能力、语言指令遵循能力、训练后任务成功率均实现大幅提升，在自研Maker H01平台与主流机器人形态的家庭、工业场景均展现强任务适配与完成能力，训练代码与预训练权重将全部开源。
