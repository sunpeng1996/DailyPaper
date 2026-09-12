---
title: 'Logit Refiner: Improving Visual Autoregressive Models via Intra-Scale Dependency
  Modeling'
title_zh: Logit Refiner：基于尺度内依赖建模优化视觉自回归模型
authors:
- Meimingwei Li
- Stefan Andreas Baumann
- Felix Krause
- Björn Ommer
affiliations:
- CompVis @ LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2609.11804'
url: https://arxiv.org/abs/2609.11804
pdf_url: https://arxiv.org/pdf/2609.11804
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态生成 · 自回归解码优化
tags:
- Autoregressive Modeling
- Visual Generation
- Decoding Optimization
- Parameter Efficient
- Plug-and-Play
one_liner: 为预训练视觉自回归模型加轻量无需重训的优化模块，补全同尺度token依赖提升生成质量
practical_value: '- 生成式推荐/商品图文生成场景可借鉴插件式模块设计：针对并行解码导致的局部内容不一致问题，无需重训大模型主干，仅新增少量参数的轻量模块即可修复，大幅降低迭代成本

  - 大模型落地优化优先级参考：优先定位解码规则层面的瓶颈而非盲目扩参，本方案验证1.1B参模型加轻量模块即可超过原生2B参模型效果，大幅降低推理部署成本

  - 多token并行生成类任务（如推荐理由批量生成、多商品海报生成）可复用尺度内依赖补全思路：对同层级并行生成的token增加顺序依赖校验，提升输出一致性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有Visual Autoregressive Models（VAR）采用尺度内并行解码策略，本质为均值场近似，会丢失同尺度token间的空间依赖，导致生成样本局部不一致，该缺陷无法通过扩大主干模型参数量解决。
### 方法关键点
1. 提出轻量Logit Refiner模块，基于冻结的主干模型特征，对同尺度token进行顺序采样，补全尺度内依赖关系
2. 仅新增约10%参数量、消耗不到基础模型5%的训练算力，可直接插入任意预训练VAR checkpoint，无需重训主干
### 关键结果数字
在ImageNet 256×256分类条件生成任务上，310M~2B全量级主干模型加模块后效果均稳定提升；1.1B参数模型加模块后效果超过原生2B参数模型；方案可泛化到文生图任务，通用解决VAR的均值场瓶颈。
