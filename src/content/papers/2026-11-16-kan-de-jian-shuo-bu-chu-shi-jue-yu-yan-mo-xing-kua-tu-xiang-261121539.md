---
title: 'Seen but Unsaid: Locating and Repairing Cross-Image Comparison in Vision-Language
  Models'
title_zh: '"看得见说不出"：视觉语言模型跨图像比较缺陷的定位与修复'
authors:
- Zhaoning Zhang
affiliations:
- University of Toronto
arxiv_id: '2611.21539'
url: https://arxiv.org/abs/2611.21539
pdf_url: https://arxiv.org/pdf/2611.21539
published: '2026-11-16'
collected: '2026-11-17'
category: Multimodal
direction: 多模态大模型 · 低参数量能力修复
tags:
- VLM
- Cross-Image Comparison
- Attention Head
- PEFT
- Semantic Matching
one_liner: 定位VLM跨图像比对的两类故障点，仅微调0.02%参数即可大幅提升跨图匹配准确率
practical_value: '- 电商同款搜图、多模态商品比对场景，可复用「定位任务对应注意力头仅微调Q/K投影」的方案，微调成本远低于全量/通用PEFT

  - 多模态Agent做商品校验、跨图推理任务优化时，可先验证隐藏层是否已包含正确信息，仅修通输出通路即可，无需重训视觉编码器

  - 做多模态模型PEFT选型时，优先定向调整任务相关的小范围注意力头参数，比通用层适配器效率更高、跨任务迁移性更好'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLM在跨图像匹配类任务（如同款比对、语义对应、点匹配）上普遍存在「视觉特征已包含正确信息，但最终输出答案错误」的问题，现有优化方案要么全量微调成本极高，要么通用PEFT效果不达预期。
### 方法关键点
1. 定位到两类核心故障点：一是跨图比对结果已存在于隐藏层但未被输出通路读取，二是语义对应信息停留在视觉token层未传递到答案生成模块；
2. 筛选出16~32个负责跨图比对的专属注意力头，仅微调这些头的Q/K投影，总调整参数量仅占模型的0.02%。
### 关键结果
Qwen3-VL-8B在SPair-71k语义匹配数据集上准确率提升28.3pp，InternVL3.5-8B提升25.1pp，效果优于层匹配、注意力匹配的对照微调方案，且可零样本迁移到HPatches、BLINK等跨图匹配数据集。
