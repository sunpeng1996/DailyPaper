---
title: 'Show-Harness: Just a VLM Agent Can Play Robots'
title_zh: Show-Harness：仅单个VLM Agent即可实现机器人操控
authors:
- Yanzhe Chen
- Zechen Bai
- Zhijun Cao
- Wenzheng Zeng
- Kevin Qinghong Lin
- Yiqi Lin
- Guoqiang Liang
- Kevin Yuchen Ma
- Qiming Huang
- Mike Zheng Shou
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2609.10522'
url: https://arxiv.org/abs/2609.10522
pdf_url: https://arxiv.org/pdf/2609.10522
published: '2026-09-08'
collected: '2026-09-10'
category: Agent
direction: VLM Agent 具身控制语义接口设计
tags:
- VLM
- Embodied Agent
- Semantic Interface
- Zero-shot Deployment
- Low-cost Fine-tuning
one_liner: 提出语义中间层Show-Harness，无需定制预训练即可让VLM Agent实现跨场景跨形态机器人控制
practical_value: '- 可复用「大模型语义接口+下游执行器解释器」的分层架构：电商Agent场景可将LLM输出的语义操作单元映射到商品上架/营销投放/客服回复等具体业务动作，大幅降低大模型对接底层系统的适配成本

  - 参考GUMI的GUI演示采集思路：电商场景可基于前端GUI采集一线运营的操作演示数据，低成本fine-tune小尺寸业务Agent，降低部署门槛

  - 复用闭源大模型零样本适配思路：调用GPT-4V等闭源多模态大模型时，可通过统一语义动作单元约定实现零样本对接业务执行链路，无需定制训练'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM具备丰富世界知识，但难以直接转化为机器人控制能力，定制具身预训练成本极高且泛化性差，跨设备适配难度大。
### 方法关键点
1. 设计Show-Harness语义中间层：定义VLM可自然推理的离散语义动作单元，再通过形态专属解释器确定性映射为具体机器人执行动作，VLM直接负责细粒度决策
2. 配套GUMI GUI操作采集工具：无需专业遥操作硬件，即可跨设备采集人机操作演示数据
3. 支持双部署范式：闭源前沿VLM可零样本直接适配，开源小尺寸VLM仅需数GPU小时微调即可落地
### 关键结果
跨任务、跨机器人形态、跨环境泛化性显著优于主流Agent和VLA范式，无需新增模型容量或定制具身预训练即可释放VLM的具身能力。
