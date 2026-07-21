---
title: 'SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement
  Learning'
title_zh: SVR-R1：基于自验证强化学习的多模态推理增强框架
authors:
- Mingyuan Wu
- Jingcheng Yang
- Shengyi Qian
- Xudong Wang
- Jize Jiang
- Qifan Wang
- Aashu Singh
- Khoi Pham
- Fei Liu
- Zhaolun Su
affiliations:
- University of Illinois Urbana-Champaign
- Meta
arxiv_id: '2607.10966'
url: https://arxiv.org/abs/2607.10966
pdf_url: https://arxiv.org/pdf/2607.10966
published: '2026-07-12'
collected: '2026-07-21'
category: Multimodal
direction: 多模态大模型 · 自验证RL训练
tags:
- VLM
- GRPO
- Self-Verification
- Reinforcement Learning
- Multimodal Reasoning
one_liner: 将多轮自验证嵌入GRPO训练流程，无额外监督即可大幅提升VLM多模态推理性能
practical_value: '- 电商多模态内容理解场景（如商品图问答、直播文案校验、素材合规检测）可复用自验证+GRPO的轻量RL微调范式，无需额外标注监督即可提升VLM推理准确率，成本远低于传统RLHF

  - 大模型推理链路优化可参考训练后自验证内化的特性：训练阶段加自验证迭代，推理阶段可直接输出高置信结果，无需额外推理轮次，兼顾效果和效率

  - 多模态Agent的自我修正模块可复用论文的二元自验证prompt设计，仅要求输出YES/NO规避VLM幻觉，同时用损失掩码屏蔽验证token的梯度，避免训练目标冲突'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM自优化方案分为两类，一类是推理端通过prompt引导自修正，效果增益有限；另一类依赖外部标注数据做RL微调，成本高且未利用VLM本身的自验证能力，多模态场景下模型自修正能力远弱于纯语言模型，亟需无需额外监督的自举训练框架提升推理性能。

### 方法关键点
- 同权重VLM同时作为生成器与二元自验证器：生成回答后先做自校验，输出NO则触发重生成，直到输出YES或达到轮次上限，仅将最终答案送入奖励计算，验证与生成共享权重无额外开销
- 基于GRPO实现训练，损失计算时掩码掉自验证阶段的Yes/No token，避免生成与验证的目标冲突，无需额外奖励模型或评论家模块
- 奖励采用结果导向的二元设计：可校验任务用规则判断，半开放任务用轻量化LLM judge做答案匹配，不设置格式类奖励

### 关键实验
基于Qwen2.5-VL 3B/7B底座，在ChartQA、TableVQA、ThinkLite-VL-70K三个多模态推理数据集上与标准GRPO基线做控制变量对比：3B模型ChartQA准确率从80.9%提升至83.3%，TableVQA准确率从68.7%提升至72.9%；7B模型TableVQA准确率从78.5%提升至80.6%。训练后期模型自验证轮次从预设的3轮收敛到2轮左右，纯推理模式（无自验证步骤）与带自验证推理的准确率几乎持平。

### 核心结论
模型的自验证能力可作为天然训练信号，将自验证迭代嵌入RL训练流程，可在不增加推理成本的前提下缩小生成与验证的能力gap
