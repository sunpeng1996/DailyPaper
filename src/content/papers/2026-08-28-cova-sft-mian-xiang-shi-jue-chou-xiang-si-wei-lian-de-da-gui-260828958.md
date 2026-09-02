---
title: 'CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions'
title_zh: CoVA-SFT：面向视觉抽象思维链的大规模训练数据集
authors:
- Tsung-Han Wu
- Heekyung Lee
- Anya Ji
- Haoming Chen
- Trevor Darrell
- Joseph E. Gonzalez
- David M. Chan
affiliations:
- University of California, Berkeley
arxiv_id: '2608.28958'
url: https://arxiv.org/abs/2608.28958
pdf_url: https://arxiv.org/pdf/2608.28958
published: '2026-08-28'
collected: '2026-09-02'
category: Reasoning
direction: 多模态推理 · 思维链SFT数据集
tags:
- CoT
- Multimodal Reasoning
- SFT Dataset
- Visual Abstraction
- Evaluation Benchmark
one_liner: 发布51.9K样本的视觉抽象思维链SFT数据集与配套基准，性能超交错CoT基线2倍以上
practical_value: '- 电商多模态商品理解/导购Agent可借鉴「文本+视觉抽象交错推理」范式，替代纯文本序列化推理，提升空间布局、组合类商品的推理准确率

  - 构建多模态任务SFT数据集时，可复用「显式推理逻辑+Agent渲染+验证环」的三层标注框架，提升微调后模型的推理鲁棒性

  - 多模态推荐/搜索系统的推理链路评估，可参考CoVA-Bench的分层任务设计思路，覆盖不同复杂度的多模态场景，评估结果更可控'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
纯文本CoT处理隐含视觉属性的推理任务时，需将天然可视化的问题强制序列化为生硬文字，现有多模态架构缺乏大规模、多步骤、带自校正的训练数据集，无法支撑模型构建内部视觉工作区完成推理。
### 方法关键点
1. 发布CoVA-SFT结构化数据集，共51.9K样本，覆盖5种布局类型、17种复杂任务，包含超222K个多模态推理步骤
2. 配套发布CoVA-Bench评估基准，含1700个留出测试样本，支持可复现评估
3. 数据集自带显式推理公式、Agent渲染、验证环三类监督信号，训练多模态大模型交错使用文本和视觉抽象完成推理
### 关键结果
基于CoVA-SFT微调的模型，在CoVA-Bench上平均性能超过所有交错CoT基线2倍以上，但仍弱于强纯文本CoT基线，多模态视觉抽象推理仍有较大优化空间。
