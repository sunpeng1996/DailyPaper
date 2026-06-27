---
title: 'LISA: Likelihood Score Alignment for Visual-condition Controllable Generation'
title_zh: LISA：面向视觉条件可控生成的似然分数对齐方法
authors:
- Yanghao Wang
- Hongxu Chen
- Jiazhen Liu
- Zhenqi He
- Rui Liu
- Zhen Wang
- Long Chen
affiliations:
- The Hong Kong University of Science and Technology
- Huawei Research
arxiv_id: '2606.27192'
url: https://arxiv.org/abs/2606.27192
pdf_url: https://arxiv.org/pdf/2606.27192
published: '2026-06-24'
collected: '2026-06-27'
category: Training
direction: 视觉可控生成 · 似然分数对齐
tags:
- Controllable Generation
- Diffusion Model
- Score-based Generative Model
- Training Regularization
- Zero Inference Cost
one_liner: 提出似然分数对齐正则化方法LISA，加速视觉条件可控生成训练并提升合成质量
practical_value: '- 电商/广告多条件生成任务（如商品图生成、营销素材定制）常用「冻结预训练主模型+训练侧分支注入条件」的双分支范式，可直接复用LISA的正则化思路：给侧分支加轻量解码器，将中间特征对齐近似似然分数目标，仅增加极微训练成本即可加速收敛、提升生成质量，且无推理开销。

  - 生成式推荐中若需对多维度条件（用户兴趣、商品属性、场景约束）做解耦控制，可借鉴LISA的显式似然对齐逻辑，引导侧分支学习更解耦的条件表征，降低多条件叠加时的生成偏移风险。

  - 迭代快、推理资源紧张的业务场景（如节日营销素材快速上线），可优先尝试这类「仅加训练正则、不改推理链路」的优化方案，无需调整线上部署即可拿到效果收益。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
视觉条件可控生成的主流双分支范式（冻结预训练主网络+训练侧分支注入视觉条件）应用广泛，但侧分支的作用机理未被充分阐释，训练效率与条件控制效果仍有提升空间。

**方法关键点**
从分数生成模型视角重新解读双分支范式：主网络提供无条件先验分数保障视觉感知质量，侧分支隐式贡献似然分数实现条件控制。LISA正则化方法核心流程：
1. 取出侧分支指定层的中间特征，通过轻量解码器投影到分数隐空间；
2. 构造近似似然分数作为对齐目标，将解码器输出与目标的距离作为额外正则损失；
3. 用标准扩散损失与正则损失联合优化侧分支和解码器，推理阶段完全复用原双分支链路。

**关键结果**
在图像/视频多任务、UNet/DiT等多种骨干架构、扩散/流模型上均一致生效：训练收敛速度显著加快，最终合成质量稳定提升，侧分支的条件表征更解耦；额外训练成本可忽略，推理零额外开销。
