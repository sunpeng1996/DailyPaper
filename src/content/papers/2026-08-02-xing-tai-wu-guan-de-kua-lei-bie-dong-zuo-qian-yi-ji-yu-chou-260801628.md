---
title: 'Motion Beyond Morphology: Bootstrapping Cross-Category Motion Transfer from
  Abstract Motion Representations'
title_zh: 形态无关的跨类别动作迁移：基于抽象动作表征的自举方法
authors:
- Zhixue Fang
- Zhimin Zhang
- Bi'an Du
- Zijie Meng
- Yan Zhou
- Wei Hu
- Guoxin Zhang
- Pengfei Wan
- Kun Gai
affiliations:
- Kuaishou Technology
- Peking University
arxiv_id: '2608.01628'
url: https://arxiv.org/abs/2608.01628
pdf_url: https://arxiv.org/pdf/2608.01628
published: '2026-08-02'
collected: '2026-08-05'
category: Multimodal
direction: 多模态视频生成 · 跨类别动作迁移
tags:
- Video Generation
- Motion Transfer
- Cross-Category Learning
- Representation Learning
- Benchmark
one_liner: 提出两阶段跨类别动作迁移框架，配套开源数据集与评测基准，实现跨形态高保真动作迁移
practical_value: '- 跨品类抽象表征学习思路可复用至电商跨品类推荐、跨品类广告语义对齐任务：无需依赖固定属性对应关系，先学习高维抽象语义表征实现跨域迁移，降低跨品类任务的适配成本

  - 两阶段自举构造训练对的方法可解决跨域/跨类别任务标注不足的问题：比如广告跨品类创意生成、跨类目搜索语义匹配的弱监督训练，可自动构造配对训练样本，减少人工标注成本

  - 推理阶段去掉显式特征提取的工程优化思路可迁移至生成式推荐/广告生成场景：将前置的特征抽取逻辑内化到生成模型中，降低推理延迟，提升线上服务吞吐量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频动作迁移方法依赖参考与目标对象的固定结构对应，当二者形态、关节、形变机制差异较大时，对应关系不成立，无法实现跨类别的有效动作迁移。
### 方法关键点
1. 两阶段学习框架：阶段I学习多粒度互补的抽象动作视图，自举构造跨形态、保留可迁移动态的跨类别视频配对训练数据，无需人工标注跨类配对样本；
2. 阶段II将自举得到的监督信号内化到参考视频条件生成模型中，推理阶段无需显式执行动作特征提取步骤，降低推理开销；
3. 开源OpenVMT数据集与评测基准，覆盖同类别、近类别、远类别三种跨品类差距的图像/文本条件动作迁移任务。
### 关键结果
实验验证方法在动作保真度、目标外观保留两项核心指标上达到SOTA水平
