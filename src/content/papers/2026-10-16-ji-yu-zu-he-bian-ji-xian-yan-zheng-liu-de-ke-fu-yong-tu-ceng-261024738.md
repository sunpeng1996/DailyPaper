---
title: Editing Images into Reusable Layers via Compositional Edit-Prior Distillation
title_zh: 基于组合编辑先验蒸馏的可复用图层图像编辑方法
authors:
- Wen Xue
- Yong Liu
- Xueheng Li
- Si Wu
- Yong Xu
- Yipeng Sun
- Yan Li
- Simiu Gu
affiliations:
- South China University of Technology
- Tsinghua University
- University of Science and Technology of China
- Peng Cheng Laboratory
- JD.com
arxiv_id: '2610.24738'
url: https://arxiv.org/abs/2610.24738
pdf_url: https://arxiv.org/pdf/2610.24738
published: '2026-10-16'
collected: '2026-10-24'
category: Multimodal
direction: 多模态图像编辑 · 可复用图层生成
tags:
- Instruction-driven Editing
- Multimodal Generation
- Knowledge Distillation
- RGBA Layer
- E-commerce Material
one_liner: 提出LayerEditor统一框架，同步实现指令引导图像编辑与可复用RGBA图层可控生成
practical_value: '- 电商主图、广告素材设计场景可直接复用LayerEditor能力，编辑后直接输出分层RGBA文件，省去后期抠图拆图层环节，大幅降低素材制作迭代成本

  - 组合编辑先验蒸馏思路可迁移至多输出端生成模型微调场景，既保留预训练大模型原生编辑能力，又可适配业务所需的额外输出（如图层、mask、属性标签等）

  - 带RGBA图层标注的LayerEditor-100K数据集可直接用于电商场景素材编辑模型微调，快速适配服装、3C等品类的主图改款、配色调整需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动图像编辑模型输出扁平融合图，无法支撑细粒度局部调整、图层二次复用，电商/广告素材场景二次修改需反复生成，成本极高；现有图层分解方法与指令编辑流程割裂，无法联动优化效果。
### 方法关键点
1. 提出LayerEditor统一框架，耦合指令引导图像编辑与可复用RGBA图层可控生成
2. 核心采用In-Context RGB-Alpha Token建模，将编辑画布与有序图层序列映射到同一token序列，支持单图层内容精准控制
3. 提出Compositional Edit-Prior Distillation，将预训练模型编辑先验同时迁移到编辑画布、图层合成图两个输出端，避免适配分层输出后编辑能力掉点
4. 构建带有序RGBA图层标注的LayerEditor-100K数据集，配套分层编辑专属评测基准
### 关键结果
实验验证LayerEditor编辑保真度与主流单输出编辑模型持平，同时生成的RGBA图层精度满足业务级图层灵活操作、多层分解需求
