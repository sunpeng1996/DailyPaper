---
title: 'Rufus-Air: An Open LLM Post-Training Recipe'
title_zh: Rufus-Air：面向GLM-4.5-Air的开源可复现大模型后训练流程
authors:
- Chia-Yuan Chang
- Renyuan Cheng
- Rui Feng
- Xiaotian Han
- Yuan He
- Hongye Jin
- Linwei Li
- Shiyang Li
- Fenglin Liu
- Xin Liu
affiliations:
- Amazon
arxiv_id: '2609.29421'
url: https://arxiv.org/abs/2609.29421
pdf_url: https://arxiv.org/pdf/2609.29421
published: '2026-09-23'
collected: '2026-09-25'
category: Training
direction: 大模型后训练 · 多阶段RL+Agent训练
tags:
- Post-training
- RLHF
- Agent Training
- MoE
- SFT
one_liner: 公开基于GLM-4.5-Air的8阶段可复现后训练流水线，效果优于官方后训练版本
practical_value: '- 后训练阶段排序遵循「先硬验证奖励、后软Judge奖励」原则，例如训练电商导购Agent时，先训可规则校验的订单/优惠券查询等工具调用能力，再做偏好类RLHF，可大幅降低Reward
  Hacking风险

  - RL训练阶段新增难度过滤逻辑，仅保留模型成功率在0~0.8区间的样本，自动构建学习课程，可显著提升电商垂直Agent的训练效率，避免无效算力消耗

  - SFT阶段不要仅作为热身，需覆盖目标场景全能力域（如电商导购、售后、多轮对话、工具调用等），建立高能力基线，后续RL仅需微调即可，无需从零灌输基础能力

  - 垂直Agent训练可先在通用MCP工具调用任务上做预训练，再迁移到电商搜索、客服等场景，可获得明显的跨场景能力增益'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型后训练配方披露度极低，多为粗略系统说明，缺失可复现的阶段设计、奖励规则、工程实现细节，中小团队很难基于公开底座快速迭代出效果达标的行业定制模型。
### 方法关键点
- 采用8阶段串行后训练流水线，顺序遵循两大原则：能力从基础到高阶、奖励从硬可验证到软Judge评分，依次为SFT→推理RL→编码RL→指令跟随RL→通用Agent→编码Agent→搜索Agent→RLHF，最大限度减少Reward Hacking的暴露时间
- SFT阶段使用9M多域样本（覆盖对话、STEM、编码、Agent轨迹等），目标是建立高能力基线，而非仅做训练热身；所有RL阶段加入难度过滤，丢弃模型全对或全错的样本，聚焦可学习区间自动构建训练课程
- 工程细节作为配方核心组成部分：统一全流程对话模板、采用Rollout Routing Replay稳定MoE模型RL训练、Agent训练配套分布式沙箱支撑高并发多步工具调用
### 关键结果
基于106B总参数/12B激活参数的GLM-4.5-Air-Base MoE底座训练，对比官方后训练版本GLM-4.5-Air：IFBench指令跟随准确率提升43.3pp至76.9，搜索Agent BrowseComp指标提升14.4pp至37.1，SWE-bench Verified编码能力提升15pp至65.6，Arena-Hard v2(HP)胜率提升34.1pp至89.1，整体效果与同规模SOTA开源模型相当。
### 核心结论
基础设施和工程选择是后训练配方的核心组成部分，而非无关紧要的实现细节。
