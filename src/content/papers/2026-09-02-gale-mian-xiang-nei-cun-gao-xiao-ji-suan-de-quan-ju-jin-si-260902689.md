---
title: 'GaLe: memory-efficient Global Approximate and Local Exact features'
title_zh: GaLe：面向内存高效计算的全局近似与局部精确特征方法
authors:
- Alberto Ancilotto
- Elisabetta Farella
affiliations:
- Fondazione Bruno Kessler (FBK), Trento, Italy
arxiv_id: '2609.02689'
url: https://arxiv.org/abs/2609.02689
pdf_url: https://arxiv.org/pdf/2609.02689
published: '2026-09-02'
collected: '2026-09-04'
category: Other
direction: 端侧内存高效推理优化
tags:
- TinyML
- Memory-Optimization
- Edge-Deployment
- Attention-Inference
one_liner: 提出无需重训的特征拆分推理策略，在嵌入式设备实现低开销高适配的模型部署
practical_value: '- 端侧推荐/离线个性化推送场景可借鉴特征拆分思路，全局长序列用户特征降采样近似、近实时交互特征精确计算，平衡内存开销与推荐精度

  - 端侧部署轻量LLM/生成式推荐模型时，可复用无需重训的适配方案，仅用小校准集即可完成低算力设备适配，降低落地成本

  - 混合CNN-Transformer结构的召回/排序模型端侧部署时，可参考GaLe的全局注意力适配方法，替代传统分块推理减少精度损失'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
嵌入式端侧设备算力、RAM资源远低于GPU服务器，现有推理方案要么分块（patch-based）计算开销高，要么全局近似精度损失大，预训练混合CNN-Transformer模型端侧部署门槛高。

### 方法关键点
1. 将特征图拆分为双分支：局部精确（Le）分支保留细粒度特征，全局近似（Ga）分支降采样保留长距离依赖，无需模型重训，仅需少量校准集即可完成部署适配
2. 原生支持混合CNN-Transformer的全局操作与注意力机制计算，解决传统分块推理不支持全局算子的缺陷

### 关键结果
ImageNet数据集上精度与全精确推理持平，Cortex-M33微控制器上相比分块推理最高实现65%速度提升、90%RAM占用降低，可适配分类、检测、生成多类任务
