---
title: 'PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models'
title_zh: PhysBrain 1.5：从视觉语言模型到物理基础模型
authors:
- DeepCybo Team
- Yu Bin
- Haipeng Cao
- Zheng Chang
- Kai Chen
- Youning Chen
- Kailin Deng
- Yichao Du
- Xiaotong Fu
- Haoyang Ge
affiliations:
- DeepCybo Team
arxiv_id: '2609.14973'
url: https://arxiv.org/abs/2609.14973
pdf_url: https://arxiv.org/pdf/2609.14973
published: '2026-09-13'
collected: '2026-09-15'
category: Multimodal
direction: 多模态具身·物理基础模型构建
tags:
- Vision-Language Model
- Embodied AI
- Foundation Model
- Autoregressive Learning
- Open Source
one_liner: 基于VLM构建统一感知交互预测的8B开源物理基础模型，性能对齐顶尖闭源大模型
practical_value: '- 多模态输入（语言/视觉）、决策指令、后续状态统一编码为离散序列做自回归联合训练的框架，可直接复用到电商多模态导购Agent的交互决策建模

  - 基于人类交互视频对齐语义、空间、动作、后续观察的预训练范式，可迁移到电商用户多模态行为（浏览/点击/咨询/下单）序列的预训练任务设计

  - 混合真实轨迹、模拟数据、人类标注做SFT的策略，可用于小样本场景下推荐系统、交互Agent的快速效果迭代'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉语言模型仅支持基础多模态理解，缺乏对物理世界交互逻辑、环境变化的统一建模，无法覆盖具身场景感知、决策、预测的闭环需求。

### 方法关键点
1. 基于通用VLM搭建统一框架，将语言响应、末端执行器运动参数、密集视觉目标统一编码为离散序列，采用自回归下一词预测目标做联合优化；
2. 预训练阶段无需人工标注，完全基于人类交互视频，以任务片段为单位对齐语义空间上下文、恢复的运动序列、后续观察数据；
3. 微调阶段混合人类示范、真实机器人轨迹、模拟环境经验做监督微调，适配下游任务。

### 关键结果
8B参数版本在28个具身理解基准上平均得分72.5，达到开源SOTA，性能与GPT-6-Astra（73.3）、Gemini 3.6 Flash（73.0）等顶尖闭源模型相当；在14个基准上取得开源最优结果，同时保留通用多模态能力，可生成末端执行器轨迹、输出空间对齐的RGB/深度/机器人掩码预测未来场景。
