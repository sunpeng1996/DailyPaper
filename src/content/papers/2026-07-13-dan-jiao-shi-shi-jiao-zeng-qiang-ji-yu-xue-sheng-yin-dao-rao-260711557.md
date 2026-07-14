---
title: 'Single-Teacher View Augmentation: Enhancing Knowledge Distillation with Student-Guided
  Perturbations'
title_zh: 单教师视角增强：基于学生引导扰动的高效知识蒸馏方法
authors:
- Xuyi Yu
- Yaohua Liu
- Ziming Song
- Yinghai Zhao
- Huipeng Zhang
- Kuizhi Mei
affiliations:
- 西安交通大学
- 广东智能科学与技术研究院
- 澳门大学
- 北京华航无线电测量研究所
arxiv_id: '2607.11557'
url: https://arxiv.org/abs/2607.11557
pdf_url: https://arxiv.org/pdf/2607.11557
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: 知识蒸馏 · 单教师多视角增强
tags:
- Knowledge Distillation
- Model Compression
- Efficient Training
- Single-Teacher Augmentation
- View Generation
one_liner: 提出单阶段SAKD蒸馏框架，用学生引导扰动+无参数循环移位生成多视角，兼顾效率与性能
practical_value: '- 推荐/广告场景大模型蒸馏可复用学生引导扰动思路，用小模型动态特征生成监督视角，避免多教师蒸馏的高存储算力成本，省掉预训练步骤

  - 无参数循环移位生成多视角的方法可直接迁移到召回/排序模型蒸馏等需要扩增监督信号的场景，参数不随视角数增长，算力开销几乎无增加

  - 混合系数α的调参经验（α=0.9最优）可复用，保证教师知识占主导的前提下引入多样性，避免蒸馏过程中学生学偏

  - SAKD可作为插件直接集成到DKD/MLKD等主流蒸馏框架，无需大幅改代码即可获得稳定精度提升，适合业务快速落地'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
单教师知识蒸馏监督视角固定，限制学生泛化性；多教师蒸馏需训练存储多个大模型，成本过高难以落地。现有单教师视角增强方法存在明显 trade-off：随机扰动效率高但无语义指导，结构化增强方法需多阶段训练、参数随视角数线性增长，无法同时满足效率与性能需求。

### 方法关键点
- 用学生动态特征替代静态教师特征作为扰动生成条件，将学生从被动知识接收者转为训练的主动参与者，实现单阶段端到端训练，无需额外预训练
- 单个基础扰动通过无参数循环移位扩增为多个独立视角，参数复杂度不随视角数量上升，大幅降低额外开销
- 引入一致性损失约束扰动与教师知识对齐，多样性损失保证视角间互补性，兼顾扰动的语义正确性与监督多样性
- 总损失融合原始KD损失、多视角虚拟教师蒸馏损失与扰动约束损失，平衡锚点知识与多样性监督

### 关键实验
在CIFAR-100、ImageNet数据集上对比TeKAP（单阶段随机扰动）、Angular-KD（双阶段结构化增强）等SOTA基线：CIFAR-100跨架构W40-2→R8x4蒸馏比TeKAP最高提升1.16% Acc；额外参数仅46K，比Angular-KD少83%，训练时间从3.1小时降到2.4小时，无需预训练；ImageNet上ResNet34→ResNet18蒸馏Top-1 Acc达71.12%，超过Angular-KD 0.05%、超过TeKAP 0.49%。

知识蒸馏的视角增强无需依赖复杂的教师侧预训练改造，利用学生动态特征生成轻量扰动即可同时实现高效训练与性能提升。
