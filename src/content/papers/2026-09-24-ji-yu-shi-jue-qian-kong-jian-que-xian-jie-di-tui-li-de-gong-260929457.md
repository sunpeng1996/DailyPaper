---
title: Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent
  Space
title_zh: 基于视觉潜空间缺陷接地推理的工业异常检测
authors:
- Jaron Yeh
- Yen-Wei Chang
- Jiang Liu
- Shao-Yuan Lo
affiliations:
- National Taiwan University
- AMD GenAI
arxiv_id: '2609.29457'
url: https://arxiv.org/abs/2609.29457
pdf_url: https://arxiv.org/pdf/2609.29457
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态大模型 · 潜空间推理
tags:
- MLLM
- Latent Reasoning
- Industrial Anomaly Detection
- Instruction Dataset
- Visual Understanding
one_liner: 推出视觉潜空间缺陷推理框架Anomaly-LR及22K指令数据集，实现同规模工业异常检测SOTA
practical_value: '- 电商商品质检、虚假宣传图识别场景可复用潜空间直接迭代优化异常表征的思路，无需反复切分图像区域调用工具，降低推理延迟

  - 构建垂类多模态业务指令数据集时，可参考「全局推理轨迹+区域级标注」的标注范式，提升MLLM细粒度理解能力

  - 视觉商品理解、瑕疵品自动分拣Agent可直接适配该框架，无需外挂图像分割工具即可实现端到端缺陷识别与解释'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM驱动的工业异常检测方法存在两大痛点：一是视觉精细化检测需反复迭代访问局部图像区域或外挂工具，推理成本高；二是推理过程中局部缺陷证据易丢失，细粒度检测准确率受限。
### 方法关键点
1. Anomaly-LR缺陷接地潜空间推理框架采用先全局理解输入，再直接在视觉潜空间逐步迭代优化异常相关表征的范式，无需外挂工具或重复访问局部区域；
2. 配套推出首个面向潜空间推理的工业异常检测指令数据集IAD-LR-22K，包含22228个图文实例、4523张工业图像，覆盖全局文本推理轨迹与区域级视觉标注。
### 关键结果
在多份工业异常检测基准上，同规模方法中Anomaly-LR取得SOTA性能，无需外部参考或工具支持。
