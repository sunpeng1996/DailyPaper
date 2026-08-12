---
title: 'Putting Registers to Work: Task Registers for Token Pruning in Vision Transformers'
title_zh: 基于任务寄存器的视觉Transformer Token剪枝方法
authors:
- Hongsen Cao
- Mona Jaber
- Shanxin Yuan
- Ahmed Sayed
affiliations:
- Queen Mary University of London
arxiv_id: '2608.10989'
url: https://arxiv.org/abs/2608.10989
pdf_url: https://arxiv.org/pdf/2608.10989
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: ViT 多任务Token剪枝与推理优化
tags:
- Vision Transformer
- Token Pruning
- Task Adaptation
- Multi-Task
- Inference Acceleration
one_liner: 引入任务寄存器实现多任务自适应Token剪枝，兼顾CV多任务精度与推理吞吐量
practical_value: '- 多任务搜/推/广场景可借鉴任务专属寄存器设计，为不同业务线存储专属特征选择/Token剪枝策略，避免统一策略的性能损失

  - 大模型推理优化可参考动态剪枝预算分配思路，根据任务优先级动态调整KV cache保留量，平衡推理延时与业务效果

  - 多任务大模型微调时可复用「仅激活当前任务对应寄存器」的设计，降低跨任务干扰，减少LoRA微调的参数量与成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有ViT Token剪枝策略多为单任务设计，预训练ViT跨分类、分割、检测等任务复用时，统一剪枝策略无法适配不同任务的空间特征需求，易造成精度损失。

### 方法关键点
1. 通过无参探针实验验证：不同任务对剪枝层位置、剪枝准则、特征恢复端点的偏好存在显著差异；
2. 提出任务自适应剪枝框架TAP，为每个任务设置专属任务寄存器，仅激活当前任务对应的寄存器，基于寄存器状态完成Token重要度排序、逐层剪枝预算分配、稠密特征恢复尺度设置。

### 关键结果
Token保留率ρ=0.5时，联合适配的TAP-J模型：
- ADE20K语义分割：47.0 mIoU，encoder吞吐量提升1.30倍
- COCO目标检测：53.7 box AP，encoder吞吐量提升1.32倍
- ImageNet-1K分类任务保持竞争力
