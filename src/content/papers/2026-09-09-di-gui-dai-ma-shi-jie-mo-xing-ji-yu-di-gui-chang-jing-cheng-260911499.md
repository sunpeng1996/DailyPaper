---
title: 'Recursive Code World Models: Building Complex Worlds through Recursive Scene
  Programs'
title_zh: 递归代码世界模型：基于递归场景程序构建复杂三维世界
authors:
- Zhiqi Li
- Yuxuan Liao
- Bo Zhu
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.11499'
url: https://arxiv.org/abs/2609.11499
pdf_url: https://arxiv.org/pdf/2609.11499
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: Agent 3D场景可执行代码构建
tags:
- Code World Model
- Vision-Language Agent
- Recursive Construction
- 3D Reconstruction
- Program Synthesis
one_liner: 提出递归代码世界模型RCWM，通过全局-局部-全局递归实现单图生成高一致性可执行3D场景代码
practical_value: '- 全局-局部-全局的递归任务拆解思路可直接迁移至电商3D商品建模、虚拟卖场场景搭建任务，降低复杂生成场景的全局一致性误差

  - 局部优化后父节点回溯修正边界、空间关系误差的机制，可复用在多步Agent生成类任务中，避免局部最优破坏整体输出逻辑

  - 视觉-语言Agent直接对比参考与生成结果驱动迭代的范式，可迁移至商品素材自动化修图、合规校验、多模态内容生成流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有代码世界模型仅提供可执行程序形式的世界表示，缺乏复杂3D场景的系统性构建逻辑，单图生成场景代码时普遍存在局部结构精度低、全局几何与空间关系一致性差的问题。
### 方法关键点
1. RCWM框架耦合Recursive Scene Program（RSP）组合式场景代码表示与可递归自调用的构造求解器；
2. 每轮求解器调用遵循「全局整体建模→递归重构未解析局部→回溯全局优化组件组合」的流程，跨层级共享相机投影参数，父节点回溯修正局部优化后产生的边界误差、空间关系错位与共性错误；
3. 视觉-语言编码Agent直接对比参考图像与场景渲染结果，引导迭代优化、递归下沉与返回逻辑。
### 关键结果
复杂场景下性能全面优于此前所有基于代码的图转3D重建方法；消融实验证明递归深度越深，细粒度结构的重建效果越好
