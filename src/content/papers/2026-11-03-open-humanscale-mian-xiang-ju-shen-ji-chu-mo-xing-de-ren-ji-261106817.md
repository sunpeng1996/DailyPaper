---
title: 'Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for
  Embodied Foundation Models'
title_zh: Open-HumanScale：面向具身基础模型的人机经验规模化开源方案
authors:
- Juncheng Ma
- Jiaxin Li
- Jiankai Tu
- Bo Liang
- Guodong Lv
- Yufan Deng
- Junzhe Tang
- Liangzhu Yang
- Chen Bian
- Zicong Cao
affiliations:
- PKU
- NUS
- MIT
- UCSB
- NVIDIA
arxiv_id: '2611.06817'
url: https://arxiv.org/abs/2611.06817
pdf_url: https://arxiv.org/pdf/2611.06817
published: '2026-11-03'
collected: '2026-11-08'
category: Agent
direction: 具身Agent · 预训练数据规模化
tags:
- Embodied AI
- Scaling Law
- Pre-training
- World Model
- Dataset
- Zero-shot
one_liner: 开源5万小时标注第一人称视频与训练管线，验证具身模型预训练scaling定律，刷新具身任务SOTA
practical_value: '- 可复用对数线性scaling定律结论，规划多模态Agent、生成式推荐模型的预训练数据量级，减少试错成本

  - 人机混合预训练思路可迁移到仓储拣货机器人、AR导购具身Agent场景，混合人类行为+机器实测数据提升泛化性

  - 第一人称视频标注pipeline可复用在用户手势理解、AR试穿/试玩场景的动作识别数据生产环节'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
第一人称人类视频是机器人学习操作先验的高性价比规模化数据源，但原始数据向可泛化机器人策略的转化缺乏标准化数据治理与训练方案。
### 方法关键点
1. 开源5万小时密集标注手部动作、自然语言的第一人称视频语料库Open-HumanScale-50K，配套全链路数据治理、预训练、评测管线
2. 实证得到预训练数据时长与下游机器人任务成功率的对数线性scaling定律
3. 分别推出仅人类数据预训练的HumanWAM-Vanilla、人机混合数据预训练的视觉目标条件世界动作模型HumanWAM-Goal
### 关键结果数字
- HumanWAM-Goal刷新RoboTwin 2.0 SOTA：Clean2Clean准确率92.70%、Clean2Random准确率84.60%
- 具备具身上下文学习能力，无需参数更新即可适配未见过的视觉目标，零样本泛化能力显著提升
