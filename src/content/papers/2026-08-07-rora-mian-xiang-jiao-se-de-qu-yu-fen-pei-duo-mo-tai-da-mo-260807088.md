---
title: 'RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs'
title_zh: RoRA：面向角色的区域分配多模态大模型视觉Token剪枝框架
authors:
- Qiyanhui Lu
- Han Wu
- Rongjian Xu
- Tingzhang Luo
- Cheng Fan
- Xinghao Chen
- Minjing Dong
- Jufeng Yang
- Jianyuan Guo
affiliations:
- City University of Hong Kong
- Peking University
- Huawei Technologies
- Nankai University
arxiv_id: '2608.07088'
url: https://arxiv.org/abs/2608.07088
pdf_url: https://arxiv.org/pdf/2608.07088
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态大模型 · 视觉Token剪枝推理加速
tags:
- MLLM
- Token Pruning
- Training-free
- Inference Acceleration
- KV Cache
one_liner: 训练免优的MLLM视觉Token剪枝框架，按语义角色分配预算实现高压缩比下的精度保留
practical_value: '- 电商多模态商品理解、导购Agent场景可直接复用RoRA框架，无需重训MLLM即可降低视觉推理的KV cache占用与延迟，适配高并发商品审核、实时图文问答需求

  - 分角色分配特征预算的思路可迁移至多模态推荐的特征提取阶段：将商品图特征拆分为主体、上下文、细节三类加权，在减少特征传输与计算开销的同时保留核心排序信号

  - AAR轻量区域代理的设计可替代全局相似度计算，用于端侧多模态推荐/导购Agent的部署，在高压缩比下仍能保留OCR、细粒度商品属性识别的精度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
多模态大模型（MLLM）编码图像时会生成数千长度的视觉Token序列，占据绝大多数prefill计算成本、KV cache存储空间与推理延迟，现有免训练剪枝方法要么仅按注意力、多样性筛选Token，忽略语义角色差异导致核心信息丢失，要么依赖全局相似度矩阵计算开销极高，无法在高压缩比下兼顾精度与效率。
### 方法关键点
- 预算拆分：将保留Token按语义角色划分为**保护语义核心**（查询关联的核心物体）、**互补上下文**（核心外的场景/关联物体）、**细粒度细节**（文字/边缘/小部件）三类，固定总预算下差异化分配配额
- 注意力校准：用离线统计的位置先验+物体提示校准的物体先验修正文本条件注意力的位置偏差，选择Top Kp Token作为不受后续剪枝影响的语义核心
- AAR结构化剪枝：基于核心Token构建Attention-Anchored Regions（AARs）作为已覆盖物体区域的轻量代理，上下文Token优先从AAR外选择，冗余过滤仅对比候选与核心Token的相似度，无需构建全局相似度矩阵
- 细节修复：用小额度预算从AAR内选择高局部对比度、高特征强度的Token，补全OCR、小部件等易被粗粒度筛选丢失的细粒度信息
### 关键结果
在LLaVA-1.5、LLaVA-NeXT、Qwen2.5-VL、Qwen3-VL等主流MLLM上对比10+SOTA免训练剪枝基线：
- LLaVA-1.5在88.9%极高剪枝率下仍保留96.5%的全量模型精度
- Qwen3-VL在75~90%剪枝率下精度领先D2Pruner约5%
- 66.7%剪枝率下单图Token选择仅需0.7ms，端到端推理延迟降低24.6%，NVIDIA H800上推理速度达全量模型的1.33倍
> 最值得记住：多模态信息压缩无需用统一标准筛选Token，按语义角色差异化分配预算，可用极低开销实现精度与效率的最优平衡。
