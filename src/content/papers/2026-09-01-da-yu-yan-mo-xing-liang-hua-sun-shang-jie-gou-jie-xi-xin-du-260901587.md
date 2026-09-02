---
title: 'The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent
  Globally'
title_zh: 大语言模型量化损伤结构解析：新增精度比特应优先全局分配
authors:
- Jundong Hu
- Shekar Ramachandran
affiliations:
- PayPal AI
arxiv_id: '2609.01587'
url: https://arxiv.org/abs/2609.01587
pdf_url: https://arxiv.org/pdf/2609.01587
published: '2026-09-01'
collected: '2026-09-02'
category: LLM
direction: LLM推理优化 · PTQ量化
tags:
- PTQ
- Quantization
- LLM Serving
- Mixed Precision
- Model Compression
one_liner: 验证3种常用LLM量化损伤定位假设不成立，等精度预算下全局提升量化粒度优于局部层修复
practical_value: '- 部署LLM做RAG/Agent/生成式推荐时，有限精度预算优先选全局更细量化粒度（如group-128），比修复个别关键层效果好21-52个百分点，成本收益比更高

  - 8-bit PTQ已经接近无损，不需要追求更高精度的权重表示，可直接用8-bit量化降低推理成本，适合电商大流量LLM服务场景

  - 不要依赖任务电路、计算位点、权重统计这三类廉价信号定位量化损伤层，三类信号均无法有效预测精度恢复效果，避免做无用的局部层精度优化

  - 同架构族的LLM量化损伤峰值层位置相关，如LLaMA-3.x都在L1，同架构大规模部署时可小参数量化测试后复用结论，降低调优成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
PTQ是LLM推理降本的核心手段，但量化精度损失分布不均，业界普遍认为可通过定位损伤层、局部提升精度修复效果，却缺乏对量化损伤真实分布的系统性验证，也无明确的有限精度预算分配规则。

### 方法关键点
- 以因果混合精度干预为金标准：逐次将单个层从4-bit提升到8-bit，其余层保持4-bit，测量精度恢复率作为该层精度的边际价值
- 测试3个业界普遍认可的量化损伤定位假设：损伤存在于任务电路（H1）、模型计算位点（H2）、权重统计特征（H3），对比三类定位信号与金标准的匹配度
- 等预算对比：将+0.146有效比特/权重的增量分别投入全局（全模型量化粒度从per-row升级到group-128）和局部（优先将边际价值最高的层升级到8-bit），对比两者精度恢复效果

### 关键实验
覆盖4个架构族共9个开源LLM，在22个任务（阅读理解、常识推理、事实检索等）上测试：
- 3个假设全部不成立，控制模型和任务类别后，电路漂移与损伤的相关系数降至0.05，边界计算层对6/9模型的精度恢复率≤13%，权重统计仅在LLaMA族内有效
- 量化损伤整体呈弥散分布，恢复75%的精度损失平均需要修复49%的层，仅Qwen3-8B存在集中损伤
- 8个支持group-128的模型中，全局粒度优化的精度恢复率比局部层高21-52个百分点，即使是损伤集中的Qwen3-8B也符合该结论；8-bit PTQ精度与fp16几乎无差异

### 核心结论
有限精度预算下，全局优化量化粒度的默认优先级远高于局部修复关键层，廉价的量化损伤定位信号无法替代因果干预测试
