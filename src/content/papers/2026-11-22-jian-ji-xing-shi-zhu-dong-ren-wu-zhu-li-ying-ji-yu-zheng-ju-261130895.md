---
title: 'Speak When You See It: Proactive Task Assistants Should Wait for Evidence,
  Not the Clock'
title_zh: 见机行事：主动任务助理应基于证据而非计时器决策
authors:
- Bohe Chen
affiliations:
- Beijing University of Posts and Telecommunications
- Queen Mary University of London
arxiv_id: '2611.30895'
url: https://arxiv.org/abs/2611.30895
pdf_url: https://arxiv.org/pdf/2611.30895
published: '2026-11-22'
collected: '2026-11-26'
category: Agent
direction: 主动Agent · 多模态决策优化
tags:
- Proactive Agent
- Multimodal LLM
- Contrastive Training
- Shortcut Mitigation
- Video Understanding
one_liner: 提出证据对比训练ECT，消除时序捷径，让主动任务助理基于实际证据而非计时决策
practical_value: '- 做主动触发类Agent（如电商直播间智能助理、购物流程主动引导）时，可引入同时间戳正负样本对比训练，消除仅靠固定时间延迟触发的捷径，减少无效打扰

  - 多模态任务评估时可参考「视频盲frontier」思路，先测试纯时序/规则baseline的性能上限，避免把学到的数据时序分布误判为模型多模态理解能力

  - 小模型微调可复用ECT低成本方案：仅用LoRA + 少量真实场景样本（无需合成数据），15小时A100训练即可大幅降低误触发率，适合业务快速落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
主动任务助理（如烹饪指导、装配引导、消费场景主动服务）需要实时判断任务步骤完成/出错时机，提前打断或延迟反馈都会大幅降低用户体验。但现有基准存在严重时序捷径：纯计时规则的性能甚至超过已发表的多模态模型结果，模型实际学到的是数据集的时间分布，而非真实场景的视觉证据。

### 方法关键点
- 定义**视频盲frontier**：仅用步骤耗时、指令文本、训练集统计量做决策的最优性能边界，用于衡量模型是否真正用到了多模态感知信息
- 提出**Evidence-Contrastive Training (ECT)**：将相同时间戳、同一场景下的正负样本配对训练，让模型无法通过时间差区分样本，强制学习视觉证据特征
- 训练仅用LoRA微调2B多模态大模型，无需合成数据、额外决策阈值，15小时A100即可完成全流程训练

### 关键结果
- 跨数据集迁移：在QICD训练的ECT模型，在未经过适配的Ego-MC-Bench上达到59%的无错步骤及时确认率，是同骨干已发表模型的2倍
- 时序配对测试准确率：相同时间戳下完成/未完成步骤区分准确率达90%-92%，纯计时规则仅50%，零样本大模型仅66%
- 误触发率下降：单检查点误报警率从18%降至7%，大幅减少用户被无效打扰的概率

### 核心结论
做主动决策类多模态系统时，先验证纯规则基线的性能上限，避免把学到的数据分布捷径当成模型的感知能力。
