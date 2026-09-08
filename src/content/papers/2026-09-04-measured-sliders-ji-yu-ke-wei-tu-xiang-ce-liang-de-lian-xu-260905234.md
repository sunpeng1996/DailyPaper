---
title: 'Measured Sliders: Learning Continuous Controls from Differentiable Image Measurements'
title_zh: Measured Sliders：基于可微图像测量的连续生成控制学习框架
authors:
- Yijia Chen
- Boyu Wei
- Xuanhua Yin
affiliations:
- School of Computer Science, The University of Sydney
arxiv_id: '2609.05234'
url: https://arxiv.org/abs/2609.05234
pdf_url: https://arxiv.org/pdf/2609.05234
published: '2026-09-04'
collected: '2026-09-08'
category: Multimodal
direction: 多模态生成 · 扩散模型可控属性编辑
tags:
- Diffusion Model
- Controllable Generation
- LoRA
- Image Editing
- Attribute Control
one_liner: 提出基于可微图像测量的扩散连续控制框架，实现可预判、可比较、可组合的属性滑杆控制
practical_value: '- 电商商品图生成场景可复用该框架实现亮度、色温、光影等属性的精准连续调优，无需反复调试prompt，大幅提升素材生产效率

  - 多LoRA分支无训练组合方案可直接复用，无需额外训练联合控制模型，降低多维度风格/属性定制的训练成本

  - 训练前可观测性测试流程可迁移到其他生成控制任务，提前筛选可学习的属性目标，避免无效训练投入'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型连续控制滑杆多基于文本或隐层表示，刻度与实际图像属性变化脱节，无法预判可学习属性、对比控制强度，多控制组合时易出现属性干扰。
### 方法关键点
1. 全流程统一基于可微图像测量空间构建，训练前通过可观测性测试筛选可用监督信号；
2. 训练时采用测量引导的损失函数，学习目标属性变化的同时抑制非目标属性偏移；
3. 训练后通过解码校准将控制量化为可比较的实际图像变化单位，多LoRA分支可存入单checkpoint，无需联合训练即可直接组合。
### 关键结果
在SDXL和FLUX.1-dev上验证，553个prompt测试中光照方向控制rho达0.995，单调调节率98.9%；五属性checkpoint平均选择性2.59，较最优基线高72.7%，双属性组合保留率96.7%，三属性组合保留率86.1%；可观测性测试可100%区分训练成功/失败的测量项。
