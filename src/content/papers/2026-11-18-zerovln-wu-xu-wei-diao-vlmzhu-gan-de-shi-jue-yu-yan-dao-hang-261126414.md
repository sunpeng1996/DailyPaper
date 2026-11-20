---
title: 'ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain'
title_zh: ZeroVLN：无需微调VLM主干的视觉语言导航学习框架
authors:
- Zixuan Huang
- Yang Zhou
- Guli Zhang
- Sunzhu Li
- Hongyan Xie
- Zehao Chen
- Fuzhen Zhuang
- Kaixuan Wang
- Xiaozhi Chen
- Yikun Ban
affiliations:
- Beihang University
- Zhuoyu Technology
- Zhejiang University
arxiv_id: '2611.26414'
url: https://arxiv.org/abs/2611.26414
pdf_url: https://arxiv.org/pdf/2611.26414
published: '2026-11-18'
collected: '2026-11-20'
category: Agent
direction: 具身Agent · 视觉语言导航
tags:
- VLN
- EmbodiedAgent
- SlowFastFramework
- RL
- VLM
- ToolCalling
one_liner: 提出零导航域SFT的慢快导航框架，通过语义工具调用和闭环RL实现优于SFT基线的性能同时保留VLM通用能力
practical_value: '- 落地通用Agent时可复用「语义工具调用接口+专用执行模块」架构，不用全量SFT大模型主干，大幅降低灾难性遗忘风险，适合电商导购Agent、虚拟场景导航数字人等多场景复用的业务

  - 两阶段训练策略可迁移到多任务共享大模型的场景：先冻结大模型训下游执行模块对齐语义请求，再用小学习率RL联合优化，兼顾垂直任务性能和大模型通用能力

  - 长序列决策任务的奖励设计可复用四类互补奖励（终端成功+首次到达+距离进度+信息发现），有效解决稀疏奖励问题，可迁移到多轮搜索引导、推荐路径优化等场景

  - 动作生成类任务可复用「执行前缀监督」trick：仅监督实际落地的动作前缀，不用全预测序列，解决训练推理不一致问题，可迁移到广告动态出价序列生成、推荐内容排期等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉语言导航（VLN）方法均需对VLM主干做导航域SFT，会大幅修改VLM原始权重，严重损失通用视觉、空间推理能力，无法支撑通用具身Agent的多场景复用需求。

### 方法关键点
- 慢快分层架构：慢决策层以VLM为大脑，仅做极小幅度更新，通过run_action_head/turn/stop三类语义工具调用输出自然语言移动决策；快执行层用流匹配动作专家，把语义决策转换为连续运动指令
- 两阶段训练：第一阶段冻结VLM，基于VLM在线生成的移动请求，用特权语义规划器生成对齐的参考轨迹，仅监督动作专家实际执行的前缀动作，对齐请求与执行逻辑；第二阶段用闭环Agent RL联合优化VLM决策和动作执行，采用轨迹级RLOO做信用分配，组合四类互补奖励解决稀疏奖励问题
- 全程无导航域全量SFT，仅通过RL对VLM做极小幅度更新

### 关键实验
在SAGE-Bench、R2R-CE、RxR-CE三个主流VLN-CE基准测试，与SFT基线DualVLN、NaVILA使用相同34445条训练episode、相同主干：ZeroVLN的SR在三个基准分别超出DualVLN 30.1pct、37.3pct、33.7pct，超出NaVILA 27.8pct、6.2pct、2.7pct；VLM权重偏移仅0.01497%，远低于DualVLN的3.21%和NaVILA的7.67%，通用视觉能力保留率接近原始VLM。

### 核心洞察
通用大模型适配垂直任务不一定需要全量SFT，通过语义接口连接专用执行模块+小幅度RL微调，既能实现更强的垂直任务性能，还能最大程度保留大模型的通用能力。
