---
title: 'BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning'
title_zh: BUS：类脑无监督自反思框架赋能高阶多模态推理
authors:
- Jiacheng Yang
- Tongying Xiao
- Yunkai Dang
- Cong Wang
- Yuekun Yang
- Qi Fan
- Wenbin Li
- Feng Miao
- Yang Gao
affiliations:
- State Key Laboratory of Novel Software Technology, Nanjing University
- Institute of Brain-inspired Intelligence, Nanjing University
- Shenzhen Research Institute of Nanjing University
arxiv_id: '2607.07361'
url: https://arxiv.org/abs/2607.07361
pdf_url: https://arxiv.org/pdf/2607.07361
published: '2026-07-08'
collected: '2026-07-09'
category: Reasoning
direction: 多模态推理 · 无监督自反射训练
tags:
- VLM
- Multimodal Reasoning
- Self-Reflection
- Unsupervised Training
- Brain-Inspired
one_liner: 提出无标注类脑自反射训练框架BUS，显著提升VLM多模态推理性能
practical_value: '- 电商多模态商品理解、以图搜货场景可复用BUS无标注训练逻辑，无需大量人工标注即可提升VLM推理精度，大幅降低数据成本

  - 多模态Agent执行复杂视觉任务（如商品瑕疵检测、图文合规校验、营销素材审核）时，可引入反向预测自反思机制，减少推理错误

  - BUS兼容SFT、RL等主流微调范式，现有VLM微调流程可直接集成该框架，无需重构训练链路，落地成本低'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前Vision-Language Models (VLMs)在处理需要一致性、细粒度推理的复杂视觉任务时表现不佳，现有自反思推理方法依赖大规模标注数据，且测试阶段无显式反思行为，标注成本高、泛化性有限。
### 方法关键点
受神经科学人脑反向预测（基于未来状态反推前置状态）机制启发，首先验证主流VLM天然具备反向预测能力，进而提出无标注训练框架BUS：通过引导VLM执行反向预测任务，在无真值标注数据上生成显式学习信号，强化模型自反思推理能力，且框架完全兼容Supervised Fine-Tuning (SFT)、Reinforcement Learning (RL)等主流微调方法。
### 关键结果数字
在8个多模态推理基准数据集上完成验证，仅使用无标注数据训练的BUS框架，即可较基线VLM取得显著性能提升，实验验证反向预测能力是VLM推理效果的核心影响因子。
