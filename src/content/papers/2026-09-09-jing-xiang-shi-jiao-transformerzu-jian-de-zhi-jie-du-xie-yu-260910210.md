---
title: 'Through the Looking Glass: Directly Reading and Writing Transformers'
title_zh: 镜像视角：Transformer组件的直接读写与可解释性方法
authors:
- Mark Oskin
affiliations:
- University of Washington
arxiv_id: '2609.10210'
url: https://arxiv.org/abs/2609.10210
pdf_url: https://arxiv.org/pdf/2609.10210
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: 大语言模型 · Transformer可解释性与编辑
tags:
- Transformer Interpretability
- Model Editing
- Attribution
- LLM Mechanism
- Neuron Analysis
one_liner: 提出无额外训练的Transformer归因方法，定位单token预测的极小关键组件集，支持低成本编辑
practical_value: '- 做LLM驱动的推荐/Agent定制化时，可借鉴本文的极小关键组件定位方法，替代全模型微调/LoRA，实现特定关联（比如商品-关键词绑定）的低成本注入，编辑损失仅为传统秩一更新的1/40

  - 搭建大模型推理故障排查工具时，可复用本文的带符号归因方法，定位bad case对应的极小组件集，不用分析全链路数千个组件，排查效率提升2个数量级

  - 垂直场景（如电商query理解、广告文案生成）小模型训练时，可参考“单预测仅依赖1%-3%组件”的结论，仅微调关键组件，降低训练和部署成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Transformer归因方法用绝对值计算贡献，单token预测需关联数千到数十万个组件，结果无解释性也无法支持精准编辑，且依赖额外训练的解释器，引入额外理解成本。

### 方法关键点
- 采用带符号的贡献归因逻辑，用净贡献而非绝对值总和统计组件对预测的作用，抵消大量反向抵消的无效贡献
- 无需额外训练/拟合，仅基于模型原生参数和激活值定位关键组件，设计层原生token表作为中间层特征的解释基准，避免外部解释器偏差
- 设计关键组件的必要性（删除是否改变预测）、充分性（仅保留是否复现预测）验证流程，支持组件功能的精准校验
- 提出单组件注入编辑方法，直接向空闲组件写入目标关联，无需全局参数更新

### 关键结果数字
- 覆盖124M到7B参数的12款主流Transformer模型中，单个预测的充分组件集仅2-16个，仅占模型总组件的0.017%，90%净贡献由最多53个组件提供
- 单组件注入编辑可将目标token排名从578提升到第1，仅带来0.25%的外样本损失，成本仅为传统秩一更新的1/40
- 模型每层74%-79%的残差更新是固定线性映射的架构开销，不参与具体预测计算

### 核心结论
Transformer的单个预测仅依赖极小的关键组件集合，大部分计算都是维持残差流组织的架构开销，带符号的净贡献归因是穿透抵消噪声的核心。
