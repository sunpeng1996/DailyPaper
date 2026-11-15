---
title: 'EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming'
title_zh: EgoX：支持具身梦境的第一视角跨具身操控框架
authors:
- Yaru Niu
- Binghong Chen
- Changwei Yao
- Shangtao Li
- Zhenlong Fang
- Revanth Krishna Senthilkumaran
- Shuai Zhou
- Yuemin Mao
- Kalie Ching
- Po-Ju Chao
affiliations:
- Carnegie Mellon University
- Bosch Center for Artificial Intelligence
- The University of Texas at Arlington
- University of California, Berkeley
- NVIDIA
arxiv_id: '2611.16728'
url: https://arxiv.org/abs/2611.16728
pdf_url: https://arxiv.org/pdf/2611.16728
published: '2026-11-11'
collected: '2026-11-15'
category: Agent
direction: 具身Agent 跨形态操控策略学习
tags:
- Agent
- Cross-Embodiment
- Transformer
- Pre-training
- Self-supervised
one_liner: 提出跨具身学习框架EgoX，通过模块化Transformer+具身梦境实现异构演示数据高效利用
practical_value: '- 多源异构数据预训练的模块化架构可迁移至多场景推荐模型，不同业务域对应独立tokenizer/专家头、共享主干，大幅降低多场景建模成本

  - 训练阶段新增的自监督「梦境」目标（预测未来隐状态）可借鉴到序列推荐中，提升模型对用户行为动态的建模能力，增强OOD场景泛化效果

  - 跨域预训练+小样本目标域微调的范式可复用在冷启动业务的推荐/Agent策略落地，减少新场景标注数据需求'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
通用具身操控策略可融合人类、真实机器人、仿真Agent的互补经验，但不同形态的感知、控制接口差异导致异构演示数据难以联合训练。

### 方法关键点
1. 提出EgoX跨具身学习框架，通过语义对齐的观测-动作模态组织异构演示数据
2. 核心模型MXT+为每个观测模态配置专属tokenizer、每个动作模态配置专属专家，共享Transformer主干降低训练成本
3. 新增训练阶段专属的具身梦境目标，预测未来视觉、本体感知状态的隐表示，引导主干建模不同具身的动态特性，采用「跨域预训练+目标域微调」的落地范式

### 关键结果
13组任务-具身对测试下，跨具身预训练相比从零训练平均归一化任务进度从0.63提升到0.80；OOD场景下从0.53提升到0.77；消融实验验证模块化接口、具身梦境、广覆盖预训练数据集均对效果提升有显著贡献
