---
title: A Visual Dependence-Aware Framework for Multimodal Unsupervised Continual Post-Training
title_zh: 视觉依赖感知的多模态大模型无监督持续后训练框架
authors:
- Kaichen Li
- Zhilin Zhu
- Jianhao Huang
- Zhengqin Lai
- Baochen Xiong
- Zibo Shao
- Yaguang Song
- Linhui Xiao
- Xiaoshan Yang
- Changsheng Xu
affiliations:
- State Key Laboratory of Multimodal Artificial Intelligence Systems, CAS
- Pengcheng Laboratory
- School of Artificial Intelligence, UCAS
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2608.26095'
url: https://arxiv.org/abs/2608.26095
pdf_url: https://arxiv.org/pdf/2608.26095
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 多模态大模型 · 无监督持续训练
tags:
- MLLM
- Continual Learning
- Unsupervised Post-Training
- Visual Dependence
- LoRA
one_liner: 基于token级视觉依赖设计双组件框架，平衡多模态无监督持续学习的稳定性与可塑性
practical_value: '- 做多模态商品/广告理解的增量迭代时，可复用token级视觉依赖（VD）度量方法，区分视觉驱动和语言驱动token，优化微调目标减少语言偏见

  - 多模态大模型无监督增量训练时，可借鉴VC-OT最优传输的防遗忘设计，仅用1000条旧样本回放即可将遗忘率控制在0.6%，无需标注数据

  - VMA加权损失思路可迁移到多模态生成场景，对视觉相关token加权优化，提升商品属性识别、海报文案生成的视觉一致性

  - 实验验证LoRA rank=128、回放buffer=1000时多模态持续训练性价比最高，可直接复用该超参数配置降低调参成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有MLLM无监督后训练基于静态闭合数据集，无法适配真实场景流式无标注多模态数据的持续迭代需求；且优化时对所有token统一加权，忽略token级视觉依赖（VD）异质性，易出现跨模态归因遗忘——视觉依赖从实体token漂移到语言上下文token，导致模型输出幻觉，而已有持续学习方法高度依赖标注数据，落地成本极高。

### 方法关键点
- 定义token级VD度量：通过真实输入和无信息视觉输入下的token预测对数似然差计算，正值表示token由视觉输入驱动，非正值表示由语言上下文驱动
- 提出VC-OT视觉约束最优传输模块：将旧任务VD结构扭曲建模为最优传输问题，通过区域感知运输成本（基于视觉注意力JSD）和依赖分层惩罚（禁止VD从视觉相关token转移到无关token），缓解跨模态遗忘
- 提出VMA视觉调制适配模块：新任务训练时按VD值加权token损失，放大视觉驱动token的学习权重，抑制任务特定语言模板的过拟合，提升新任务可塑性

### 关键实验结果
在TextVQA、SciVQA等6个跨领域多模态VQA数据集上测试，对比10个现有无监督后训练、持续学习基线：VDA平均准确率达62.5%，比最强无监督后训练基线ScPO高3.7个百分点，比最强持续学习基线SEEKR-MLLM高2.4个百分点，相对frozen backbone提升8.6个百分点；平均遗忘率仅0.6%，比基线降低至少79%，同时新任务学习准确率达63%，实现稳定性与可塑性的最优平衡。

**最值得记住的结论**：多模态无监督持续学习中，token级视觉依赖是平衡稳定性和可塑性的天然有效信号，无需额外标注即可同时实现低遗忘和高适配。
