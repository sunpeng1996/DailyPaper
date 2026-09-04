---
title: 'AffectDelta: Beyond Emotion Labels for Image Editing'
title_zh: AffectDelta：超越情绪标签的图像编辑方法
authors:
- Xingzu Zhan
- Lin Gu
- Ruogu Fang
affiliations:
- Department of Biomedical Engineering, Vanderbilt University
- Research Institute of Electrical Communication, Tohoku University
arxiv_id: '2609.02616'
url: https://arxiv.org/abs/2609.02616
pdf_url: https://arxiv.org/pdf/2609.02616
published: '2026-09-02'
collected: '2026-09-04'
category: Multimodal
direction: 多模态情绪驱动的图像编辑
tags:
- Emotion-driven Editing
- Diffusion Model
- Image Editing
- Multimodal Generation
- Dataset Construction
one_liner: 提出基于8维情绪分布差值的源感知图像编辑框架，配套249K情绪图像对数据集，效果优于6类基线
practical_value: '- 电商商品图氛围优化可复用「源-目标情绪分布差值」思路，替代单一情绪标签调整商品图情绪，避免破坏原图构图

  - 多模态内容生成的细粒度控制场景，可迁移「直接用属性分布差值作为条件信号」的方法，省略文本指令中间对齐环节

  - 生成式内容任务的训练数据构建，可参考AffectPair-249K的跨类/同类属性转移配对逻辑，降低标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有情绪驱动图像编辑依赖单一情绪标签+文本操作指令，无法量化共存情绪的增减幅度，易丢失原图结构语义，情绪对齐精度不足。
### 方法关键点
1. 将编辑任务建模为8维情绪分布的过渡过程，用冻结的情绪分布预测器输出源图情绪状态，计算源到目标的带符号差值作为编辑信号，无需文本指令做中间对齐；
2. 内置过渡编码器+源感知扩散主干，将差值信号转化为上下文相关的语义和外观修改，保留原图整体构图与结构一致性；
3. 构建AffectPair-249K数据集，包含248841对源-目标图像对，覆盖跨类别和类内情绪过渡场景。
### 关键结果
对比6个基线模型，在情绪对齐度、原图内容保留度上均取得最优表现，消融实验验证了所有模块设计的有效性。
