---
title: 'Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation
  Foundation Models'
title_zh: Qwen-RobotManip技术报告：对齐解锁机器人操作基础模型缩放
authors:
- Haoqi Yuan
- Zhixuan Liang
- Anzhe Chen
- Ye Wang
- Haoyang Li
- Pei Lin
- Yiyang Huang
- Zixing Lei
- Tong Zhang
- Jiazhao Zhang
affiliations:
- Qwen Team
arxiv_id: '2606.17846'
url: https://arxiv.org/abs/2606.17846
pdf_url: https://arxiv.org/pdf/2606.17846
published: '2026-06-16'
collected: '2026-06-30'
category: Other
direction: 多模态基础模型 · 机器人操作对齐
tags:
- Alignment
- Foundation Model
- Scaling
- Multimodal
- Generalization
one_liner: 提出机器人操作多维度统一对齐框架，仅用开源数据训出泛化超SOTA的基础模型
practical_value: '- 多源异质数据做规模化大模型训练时，可从表示、任务、行为多维度做对齐避免训练冲突，该思路可迁移到推荐/Agent领域多源数据融合训练

  - 业务测评模型时，不能仅依赖封闭集标准基准，需要补充分布外（OOD）场景测评才能反映真实泛化能力

  - 可借鉴「人类行为数据合成转换为任务数据」的思路，转换公开人类交互数据扩充推荐/Agent场景训练语料，降低采集成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
语言与多模态基础模型依靠统一对齐下的规模化训练获得强泛化能力，但机器人操作数据天然异质、采集成本高、多样性狭窄，难以同时实现对齐与规模化，无法套用该成功范式。

### 方法关键点
基于Qwen-VL构建通用视觉-语言-动作基础模型，提出横跨表示、运动、行为三个维度的统一对齐框架，解决大规模多源训练的冲突问题，支撑更大规模数据训练；搭建人转机器人的合成管线，将15个平台的第一视角人手演示转换为机器人轨迹，搭配严格的数据清洗管线整合异质数据集，仅用开源数据就构建了约3.81万小时的预训练语料。

### 关键结果
发现标准基准无法有效衡量预训练质量，在多个OOD测评设置上验证，性能全面超越包括π0.5在内的先前SOTA，在RoboChallenge排名第一，相对提升20%，在多个真实机器人平台验证有效，涌现出零样本指令跟随、扰动鲁棒性、错误恢复、跨形态迁移等泛化能力
