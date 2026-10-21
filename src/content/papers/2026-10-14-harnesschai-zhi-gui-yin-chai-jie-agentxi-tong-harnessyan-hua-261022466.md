---
title: 'Harness-Delta Attribution: Dissecting Gains From Harness Evolution'
title_zh: Harness差值归因：拆解Agent系统Harness演化的性能增益来源
authors:
- Wenxuan Ding
- Qin Lu
- Changlong Yu
- Sha Li
- Shuowei Jin
- Xin Liu
- Zhenyu Shi
- Greg Durrett
affiliations:
- Amazon
- New York University
arxiv_id: '2610.22466'
url: https://arxiv.org/abs/2610.22466
pdf_url: https://arxiv.org/pdf/2610.22466
published: '2026-10-14'
collected: '2026-10-21'
category: Agent
direction: Agent Harness演化 · 性能归因评估
tags:
- Agent Harness
- Evolution Attribution
- Overfitting
- Test-time Compute
- Generalization
one_liner: 提出HDA半自动化评估协议，将Agent Harness演化增益拆解为过拟合、算力扩展、可泛化改进三类
practical_value: '- 做Agent自动优化（含prompt、工具链、编排逻辑迭代）时，复用HDA思路拆解增益：先扣掉靠增加LLM调用/多采样堆出的性能收益，再排查是否存在硬编码业务数据集规则的shortcut，剩余收益才具备上线价值

  - 电商导购、广告投放类Agent的Harness迭代场景中，验证集需刻意构造与训练集构造逻辑不同的分布偏移样本，避免自动优化学到仅适用于同分布基准的虚假规则，上线后失效

  - 可复用HDA的半自动化审计流程：先用大模型自动扫描优化后的Harness代码、prompt中的硬编码匹配、固定规则，再人工校验，快速筛除过拟合的优化结果，降低上线风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent Harness（包含prompt、工具、编排逻辑、记忆等非权重组件）的自动迭代无需更新模型权重即可提升性能，但现有评估无法区分增益来源：是真可泛化的改进、过拟合基准数据集的人工特征，还是靠增加测试时计算资源堆出的效果，大量优化后的Harness在分布偏移场景下性能暴跌，亟需可量化的增益拆解方案。

### 方法关键点
- Harness-Delta Attribution（HDA）半自动化评估协议将增益拆分为三类：Overfitting（硬编码数据集shortcut、基准特有规则）、Test-time Scaling（额外LLM调用、多采样等算力扩展带来的增益）、Generalizable Improvement（剩余增益，为可泛化改进的上界）
- 实现逻辑：先构造算力匹配的基线Harness，计算算力扩展贡献的增益T；再中性化优化后Harness中的过拟合规则，计算过拟合贡献的增益O；剩余部分为可泛化改进的上界G
- 流程设置两个人工校验节点：算力匹配规则、过拟合中性化操作，保证结果可靠性

### 关键实验结果
覆盖3个主流Harness演化框架、11个基座模型、4类任务（数学推理、代码、创意生成、具身规划）共25个场景：
- 21个有统计显著增益的场景中，平均54%的增益来自过拟合，14%来自测试时算力扩展，两者合计占比超过50%的场景有14个
- 仅靠留出集评估无法识别全部过拟合：ALFWorld任务中优化后的Harness留出集准确率接近100%，但98%的增益来自过拟合基准构造规则，部分小模型的Harness直接变为无需调用LLM的硬编码控制器

### 最值得记住的一句话
Harness演化的训练集涨点不代表真有用，超过一半的增益可能是过拟合或者堆算力堆出来的，上线前必须做增益归因校验
