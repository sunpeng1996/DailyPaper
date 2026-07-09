---
title: Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation
title_zh: 多教师同策略蒸馏中的行为杠杆失衡问题与优化方案
authors:
- Jiabin Shen
- Guang Chen
- Chengjun Mao
affiliations:
- 天津大学
- 蚂蚁集团
arxiv_id: '2607.07050'
url: https://arxiv.org/abs/2607.07050
pdf_url: https://arxiv.org/pdf/2607.07050
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 工具调用蒸馏优化
tags:
- On-policy Distillation
- Knowledge Distillation
- Tool Calling
- Multi-Teacher Distillation
- Soft Clamp
one_liner: 识别多教师同策略蒸馏的行为杠杆失衡问题，提出Soft Clamp校准法降低工具过度调用
practical_value: '- 做多教师蒸馏训练Agent工具调用能力时，不能只看整体loss，要重点监控<tool call>这类高杠杆模式入口token的概率偏移，避免出现工具过度调用/调用不足的行为漂移

  - 蒸馏训练结构化输出（比如工具调用、Semantic ID生成）时，可加入低权重的有监督损失作为格式锚，避免出现输出格式漂移无法解析的问题

  - 多任务/多教师蒸馏出现行为偏移时，可直接复用Soft Clamp方法：按batch内平均JSD的k倍动态钳制极端token的divergence，保留梯度的同时降低高杠杆token的过度影响

  - 部署多轮对话Agent前，要做多轮循环诊断，单轮的过度调用率上升会直接放大为多轮的重复调用、循环调用，大幅降低用户体验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多教师同策略蒸馏（MOPD）是训练Agent工具调用能力的主流方案，可分别用工具调用教师、直接回答教师做定向监督，但 vanilla 方案存在隐性行为偏移：工具调用召回率提升的同时，本该直接回答的场景也会过度调用工具，而整体loss、token曝光量、全序列divergence都无法解释该问题，严重影响Agent部署可用性，会导致延迟上升、多轮调用循环等问题。

### 方法关键点
- 提出**行为杠杆失衡**概念：<tool call>、函数名这类模式入口token的局部学习信号对全局生成模式的影响远大于普通内容token，工具调用教师的信号集中在这类高杠杆位置，即使整体占比低，也会推动模型向过度调用工具偏移
- 提出**Soft Clamp**校准方法：每个batch内计算所有token的JSD均值，以k倍均值作为动态阈值，低于阈值的token损失不变，高于阈值的token将前向值钳制在阈值，梯度按比例缩放不消失，无需额外数据、模型修改，仅修改损失计算逻辑
- 训练时加入权重0.3的有监督损失作为格式锚，避免工具调用的结构化输出格式漂移

### 关键结果
在APIGen-MT工具调用决策基准上，对比vanilla GKD、Hard Clip、Global Reweight基线，Soft Clamp将过度调用率从13.7%降至9.0%，同时保持89.2%的决策精度；BFCL多轮诊断中，每轮工具调用数从1.494降至1.268，3步循环率从14.8%降至10.1%，最终回答率从89.6%升至94.1%。

最值得记住的结论：多教师同策略蒸馏监控指标不能只看各教师的总信号量，更要关注信号作用的位置是否是高杠杆的行为边界token。
