---
title: 'Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied
  Manipulation'
title_zh: Auriga技术报告：面向零样本具身操控的任务无关Agent适配层
authors:
- Chengcheng Wang
- Yuheng Shi
- Siyu Xu
- Yutong Wang
- Jinjing Zhao
- Chenghao Xia
- Jinqi Liao
- Jiankun Peng
- Ligong Bi
- Yuechuan Ma
affiliations:
- StellarEdge AI Technical Team
arxiv_id: '2611.01112'
url: https://arxiv.org/abs/2611.01112
pdf_url: https://arxiv.org/pdf/2611.01112
published: '2026-10-30'
collected: '2026-11-10'
category: Agent
direction: 具身Agent 规划执行gap优化
tags:
- Agent
- Zero-Shot
- Embodied AI
- Task-Agnostic
- Control Harness
one_liner: 提出任务无关Agent适配层Auriga，填补具身操控规划执行gap，零样本下性能翻倍领先基线
practical_value: '- 架构层可借鉴「LLM仅负责决策、底层适配层统一封装感知/控制/校验能力」的解耦设计，降低LLM对接业务执行模块的开发成本，提升Agent鲁棒性

  - 执行链路可复用「执行前预览校验+执行中阶段容错+异常偏差反馈恢复」的机制，适合迁移到电商自动履约、售后处理等落地型Agent场景，减少错误执行损失

  - 任务无关的通用适配层迭代思路，无需针对每个下游任务微调，可复用在电商多品类客服、运营Agent的快速落地中'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Vision-language models (VLMs) 可完成指令理解与操控任务规划，但直接作为机器人执行策略时存在巨大的规划-执行gap：RoboDojo基准下移除机械臂执行环节，GPT-6 Astra的成功率从22.5%升至76.2%。
### 方法关键点
1. 设计任务无关的Agent适配层Auriga，LLM基于显式任务信念做决策，支持工具调用或合成多步Python程序执行，适配层统一提供校准3D测量、手指参考双臂控制、机器人唯一访问网关
2. 执行前暂停仿真提供视觉轨迹预览供模型校验；执行中实时检测阶段容忍度、抓取边界，异常时停止机器人并返回测量偏差支持原位恢复
### 关键结果
填补68.3%的规划执行gap，零样本下无需目标任务试训或重置：
- RoboDojo榜单第一，成功率57.7%（得分64.0），同模型下性能是参考适配层的2倍以上；场景随机化下仍保持第一，而传统学习策略性能最高下降33.9%
- RoboCasa365基准下成功率73.2%，复合任务上比VLA辅助Agent最高领先23.1%
