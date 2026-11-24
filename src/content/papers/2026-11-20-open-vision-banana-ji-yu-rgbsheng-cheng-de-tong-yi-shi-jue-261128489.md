---
title: 'Open Vision Banana: An Open Framework for Unified Visual Perception through
  Generation in RGB Space'
title_zh: Open Vision Banana：基于RGB生成的统一视觉感知开源框架
authors:
- Xu Lin
- Ruilin Yao
- Haoran Xu
- Zixiang Wang
- Ming Ma
- Yu Zhao
- Pu Miao
- Chonghan Liu
affiliations:
- Renmin University of China
- Zhejiang University
- ByteDance
- Meituan
- University of California, Los Angeles
arxiv_id: '2611.28489'
url: https://arxiv.org/abs/2611.28489
pdf_url: https://arxiv.org/pdf/2611.28489
published: '2026-11-20'
collected: '2026-11-24'
category: Multimodal
direction: 多模态统一感知 · 开源扩散模型适配
tags:
- Diffusion Model
- LoRA
- Unified Perception
- Multimodal
- Open Source
one_liner: 基于Qwen-Image-2.1 7B扩散模型用单共享LoRA构建支持4类视觉任务的统一感知开源框架，配套调优实证
practical_value: '- 电商多模态推荐的商品图像属性抽取场景可复用单共享LoRA适配多任务的方案，大幅降低多模态大模型的部署与微调成本

  - 构建多模态Agent的视觉感知模块时可直接复用OVB的task contract规范，快速适配深度、分割等不同视觉任务需求

  - 多任务微调时不要仅依赖验证损失选最优checkpoint，需结合下游任务实际指标筛选，避免损失与指标负相关导致的效果下降'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
此前闭源Vision Banana验证了将图像生成器指令微调为通用视觉模型的可行性，但开源生成器是否能达到同等效果、存在哪些瓶颈尚未明确。
### 方法关键点
提出OVB开源框架，基于Qwen-Image-2.1的7B扩散生成器，仅用单个共享LoRA和公开数据，即可适配深度估计、语义/实例/指代分割4类视觉任务；所有任务统一遵循task contract规范，预训练前统一校验编码器、指令、解码器的格式。
### 关键结果数字
1. NYUv2深度估计中位数对齐的δ₁稳定在0.89~0.93，未对齐的仅为0.11~0.50，10种子集成可将未对齐δ₁从0.348提升至0.516无需重训
2. 深度与2D分割任务存在LoRA资源竞争，权重融合无法突破该权衡
3. 验证损失与Cityscapes mIoU呈强负相关（Spearman ρ≈-0.9），无法用损失筛选最优checkpoint
